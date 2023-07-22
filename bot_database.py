import sqlite3 as sql



async def connect_to_sql():
    con = sql.connect("register.db")
    cur = con.cursor()
    return con, cur


async def create_tables():
    con, cur = await connect_to_sql()

    cur.execute("""CREATE TABLE IF NOT EXISTS students(
                fio TEXT,
                age INTEGER,
                phone_number TEXT
    )""")


async def create_student(fio, age, phone_number):
    con, cur = await connect_to_sql()

    cur.execute("INSERT INTO students VALUES (?, ?, ?)", (fio, age, phone_number))

    con.commit()
    con.close()



async def get_all_students():
    con, cur = await connect_to_sql()

    data=cur.execute("SELECT * FROM students").fetchall()
    return data

