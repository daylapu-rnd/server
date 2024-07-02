from loader import *
from sqliteMode import *

@app.route('/registrations', methods=['POST'])
def registrations():
    """route for  register users"""
    try:
        clientID = GenerateAlfNumStr(10)
        INNSI = f'"{clientID}", "{request.json["id_tg"]}", "{request.json["name"]}", "{request.json["email"]}", "{request.json["phone"]}"'

        check = InsertData('clients', INNSI)
        con.commit()
        if len(check) > 1:
            return jsonify({"action": "success", "id": clientID})
        else:
            return jsonify({"action": "errorData"})
    except Exception as e:
        return jsonify({"action": "errorData"})