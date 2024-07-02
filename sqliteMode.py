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
            columns = 'client_id TEXT, tg_id TEXT, name TEXT, email TEXT, phone TEXT'
        case 'orders':
            columns = '''order_id TEXT, client_id TEXT, pet_id TEXT, service_type TEXT, start_date TEXT, start_time TEXT, end_date TEXT, end_time TEXT, service_details TEXT,
                    options TEXT, region TEXT, city TEXT, district TEXT, street TEXT, house TEXT, building TEXT, apartment TEXT, status TEXT'''
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
        log_error(e)
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
        log_error(e)
        return []


def SelectAllData(T, C, V, S="*"):
    """Sending an array of data from a database"""
    try:
        cur.execute(f'SELECT {S} FROM {T} WHERE {C} = "{V}"')
        data = cur.fetchall()
        newList = [
            [
                dict(zip([key[0] for key in cur.description], row))
                for row in data
            ][i]
            for i in range(len(data))
        ]
        return newList
    except Exception as e:
        return []


def SelectData(T, C, V, S="*"):
    """Sending data from the database"""
    try:
        cur.execute(f'SELECT {S} FROM {T} WHERE {C} = "{V}"')
        return [dict(zip([key[0] for key in cur.description], row)) for row in cur.fetchall()][0]
    except Exception as e:
        return []