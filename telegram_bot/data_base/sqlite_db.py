import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur

    base = sq.connect('todo.db')
    cur = base.cursor()

    if base:
        print('Data base connected!')
    base.execute('CREATE TABLE IF NOT EXISTS to_do_tasks(user_id INT, name TEXT PRIMARY KEY)')
    base.commit()


# async def sql_check_task(state):
#     async with state.proxy() as data:
#         data_values = tuple(data.values())
#         await sql_check_task(data_values)
    # функционал проверки на наличие записи в таблице. в случае, если записи нет, то вызывать метод sql_add_task


async def sql_add_task(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO to_do_tasks VALUES (?, ?)', tuple(data.values()))
        base.commit()


async def sql_show_tasks(message):
    return cur.execute('SELECT name FROM to_do_tasks WHERE user_id = ' + str(message.from_user.id)).fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM to_do_tasks WHERE name == ?', (data,))
    base.commit()
