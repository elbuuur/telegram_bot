# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram import types
#
# class FSMAdmin(StatesGroup):
#     task_add = State()
#     task_delete = State()
#
#
# # начало диалога добавления задачи в список
# @dp.message_handler(commands='Добавить задачу', state=None)
# async def cm_start(message : types.Message):
#     await FSMAdmin.task_add.set()
#     await message.reply('Опишите новую задачу')
#
#
# # ловим ответ и пишем в словарь
# @dp.message_handler(state=FSMAdmin.task_add)
# async def load_task(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['task'] = message.text
#
#
#     async with state.proxy() as data:
#         await message.reply(str(data))
#     await state.finish()
