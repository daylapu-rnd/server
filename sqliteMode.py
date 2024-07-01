from loader import *


def TableExists(table_name):
    """Check if a table exists in the database"""
    cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    if cur.fetchone()[0] == 1:
        return True
    else:
        return False


def CreateTable(table_name):
    """Create a table in the database"""
    columns = ""
    match table_name:
        case 'users':
            columns = 'id TEXT PRIMARY KEY, name TEXT, numb TEXT, id_tg TEXT, surname TEXT'

        case _:
            raise ValueError(f"Unknown table name '{table_name}'")
    cur.execute(f"CREATE TABLE {table_name}({columns})")


def UpdateData(T, U, S, C, V):
    """Edit data from the database"""
    try:
        cur.execute(f'UPDATE {T} SET {U} = ({S}) WHERE {C} = "{V}"')
        con.commit()
        return[1, 2]
    except Exception as e:
        print(e)
        return[]


def InsertData(T, V, C=""):
    """Entering data into the database"""
    try:
        if not TableExists(T):
            CreateTable(T)
        cur.execute(f'INSERT INTO {T} {C} VALUES({V})')
        con.commit()
        return [1, 2]
    except Exception as e:
        print(e)
        return []

