from loader import *
from  sqliteMode import *


@app.route('/registrations', methods=['POST'])
def registrations():
    """route for  register users"""
    try:
        idUser = GenerateAlfNumStr(10)
        idBalance = GenerateAlfNumStr(10)
        INNSI = f'"{idUser}", "{request.json["name"]}", "{request.json["numb"]}", "{request.json["id_tg"]}", "{request.json["surname"]}"'
        check = InsertData(T="users", V=INNSI)

        con.commit()
        if len(check) > 1:
            return jsonify({"action": "success", "id": idUser})
        else:
            return jsonify({"action": "errorData"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})


@app.route('/profile/change_info', methods=['POST'])
def profile_change_info():
    """route for change user info"""
    try:
        tg_id = request.json['tg_id']
        client_name = request.json['name']
        client_email = request.json['email']
        client_phone = request.json['phone']
        updateable_table = "('name', 'email', 'phone')"
        values = f'"{client_name}", "{client_email}", "{client_phone}"'
        check = UpdateData("clients", updateable_table, values, "tg_id", tg_id)
        if len(check) > 1:
            return jsonify({"action": "success"})
        return jsonify({"action": "errorData"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData 2"})
