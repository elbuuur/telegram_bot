from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from create_bot import dp, bot
from keyboards import keyboard_client
from data_base import sqlite_db


class FSMAdmin(StatesGroup):
    task_add = State()


async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет! Начнем составлять список задач? \n Нажми на кнопку "Добавить задачу"', reply_markup=keyboard_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \n https://t.me/ToDoBegemotBot')


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is None:
        return
    await state.finish()
    await message.answer('Океюшки, отмена')


async def add_task(message : types.Message):
    await FSMAdmin.task_add.set()
    await message.answer('Введите название задачи:')


async def load_task(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.from_user.id
        data['task'] = message.text

    check_task = await sqlite_db.sql_check(state)

    if check_task:
        await bot.send_message(message.from_user.id, 'Задача добавлена в общий список задач. Вы великолепны!')
    else:
        await bot.send_message(message.from_user.id, 'Ох, такая задача в списке уже имеется.')

    await state.finish()


async def show_tasks(message : types.Message):
    tasks = await sqlite_db.sql_show_tasks(message)

    if bool(tasks) == False:
        await bot.send_message(message.from_user.id, 'Ваш список задач пуст. \nНачните работу с ботом используя команду /start')
    else:
        counter = 1

        await bot.send_message(message.from_user.id, text='Момент, подгружаем все задачи...')

        for task in tasks:
            await bot.send_message(message.from_user.id, text=f'{counter} : {task[0]}',
                                   reply_markup=InlineKeyboardMarkup().
                                   add(InlineKeyboardButton('Отметить выполненной', callback_data=f'del {task[0]}')))
            counter += 1


async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} - выполнена. Ура!', show_alert=True)
    await callback_query.message.delete()


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(add_task, commands='Добавить_задачу')
    dp.register_message_handler(load_task, state=FSMAdmin.task_add)
    dp.register_message_handler(show_tasks, commands='Просмотр_списка')
    dp.register_callback_query_handler(del_callback_run, Text(startswith='del '))
