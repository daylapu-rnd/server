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
        case 'clients':
            columns = 'client_id TEXT, tg_id TEXT, name TEXT, email TEXT, phone TEXT'
        case 'orders':
            columns = '''order_id TEXT, client_id TEXT, pet_id TEXT, servise_type TEXT, start_date TEXT, start_time TEXT, end_date TEXT, end_time TEXT, service_details TEXT,
            options TEXT, region TEXT, city TEXT, district TEXT, street TEXT, house TEXT, building TEXT, apartament TEXT, status TEXT'''
        case 'pets':
            columns = 'pet_id TEXT, client_id TEXT, pet_name TEXT, pet_type TEXT, sex TEXT, bitrhday TEXT, features TEXT, sterilization INT'
        case 'executors':
            columns = 'executor_id TEXT, city TEXT, second_name TEXT, first_name TEXT, patronymic TEXT, email TEXT, link TEXT, about TEXT, phone'
        case 'executor_payment':
            columns = 'payment_exec_id TEXT, executor_id, payment_date TEXT, summ TEXT'
        case 'executor_passport':
            columns = 'passport_id TEXT, executor_id TEXT, series TEXT, numb TEXT, date_of_issue TEXT, plase_of_registration TEXT, division_code TEXT, marital_status TEXT'
        case _:
            raise ValueError(f"Unknown table name '{table_name}'")
    cur.execute(f"CREATE TABLE {table_name}({columns})")


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


def DeleteData(T, V, C):
    """Delete data into the database"""
    try:
        cur.execute(f'DELETE FROM {T} WHERE {V} = ?', (C,))
        con.commit()
        return[1, 2]
    except Exception as e:
        log_error(e)
        return []



def SelectData(T, C, V, S="*"):
    """Sending data from the database"""
    try:
        cur.execute(f'SELECT {S} FROM {T} WHERE {C} = "{V}"')
        return [dict(zip([key[0] for key in cur.description], row)) for row in cur.fetchall()][0]
    except Exception as e:
        log_error(e)
        return []



def UpdateData(T, U, S, C, V):
    """Edit data from the database"""
    try:
        cur.execute(f'UPDATE {T} SET {U} = ({S}) WHERE {C} = "{V}"')
        con.commit()
        return[1, 2]
    except Exception as e:
        log_error(e)
        return[]



def SelectAllDataWithConditions(T, C, V, S="*"):
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
        log_error(e)
        return []

def SelectAllData(T, S="*"):
    """Sending an array of data from a database"""
    try:
        cur.execute(f'SELECT {S} FROM {T}')
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