import sqlite3 as sq


def sql_start():
    global base, cur

    base = sq.connect('todo.db')
    cur = base.cursor()

    if base:
        print('Data base connected!')
    base.execute('CREATE TABLE IF NOT EXISTS {}(user_id INT, name TEXT PRIMARY KEY)'.format('to_do_tasks'))
    base.commit()


async def sql_check(state):
    async with state.proxy() as data:
        data_values = tuple(data.values())
        added_task = await sql_check_task(data_values) #таска уже была добавлена

        if added_task:
            return False
        else:
            await sql_add_task(data_values)
            return True


async def sql_check_task(data_values):
    result = cur.execute('SELECT name FROM to_do_tasks WHERE user_id = ? AND name = ?', (data_values[0], data_values[1])).fetchone()
    return isinstance(result, tuple)


async def sql_add_task(data_values):
    cur.execute('INSERT INTO to_do_tasks VALUES (?, ?)', data_values)
    base.commit()


async def sql_show_tasks(message):
    return cur.execute('SELECT name FROM to_do_tasks WHERE user_id = ?', (message.from_user.id,)).fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM to_do_tasks WHERE name == ?', (data,))
    base.commit()

