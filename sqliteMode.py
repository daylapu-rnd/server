from loader import *




# def TableExists(table_name):
#     """Check if a table exists in the database"""
#     cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
#     if cur.fetchone()[0] == 1:
#         return True
#     else:
#         return False
#
#
# def CreateTable(table_name):
#     """Create a table in the database"""
#     columns = ""
#     match table_name:
#         case 'users':
#             columns = 'id TEXT PRIMARY KEY, name TEXT, numb TEXT, id_tg TEXT, surname TEXT'
#         case 'trips':
#             columns = 'user_id TEXT, typeofmembers TEXT, tripsdates TEXT, tripstimes TEXT, direction_name TEXT, route_number INTEGER, pointa INTEGER, pointb INTEGER, id_trip TEXT, number_of_passengers INTEGER, status TEXT'
#         case 'transactions':
#             columns = 'id TEXT PRIMARY KEY, user_id, summ TEXT, date_time TEXT, type_of_transaction TEXT'
#         case 'drivers':
#             columns = 'user_id TEXT, brand TEXT, colour TEXT, numbcar TEXT, car_id TEXT'
#         case 'balance':
#             columns = 'id TEXT PRIMARY KEY, user_id TEXT, summ TEXT'
#         case 'agreedTrips':
#             columns = 'agreeing_trips_id TEXT, driver_trip_id TEXT, maximum_number_of_passengers INTEGER, number_of_passengers INTEGER, ids_trips TEXT, status TEXT'
#         case 'agreement':
#             columns = 'id_agreement TEXT, user_tg_id TEXT, response INT, datetime TEXT'
#         case 'is_become_driver':
#             columns = 'id_become TEXT, id_user TEXT, status INTEGER, datetime TEXT'
#         case _:
#             raise ValueError(f"Unknown table name '{table_name}'")
#     cur.execute(f"CREATE TABLE {table_name}({columns})")


def UpdateData(T, U, S, C, V):
    """Edit data from the database"""
    try:
        cur.execute(f'UPDATE {T} SET {U} = ({S}) WHERE {C} = "{V}"')
        con.commit()
        return[1, 2]
    except Exception as e:
        return[]



