import sqlite3


def criar_tabela(db_name):
    database_connect = sqlite3.connect(db_name)
    cursor = database_connect.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cadastros (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(255) NOT NULL UNIQUE,
        email VARCHAR(255) NOT NULL UNIQUE,
        telefone INT(15) NOT NULL UNIQUE
    )''')

    database_connect.commit()

    database_connect.close()
