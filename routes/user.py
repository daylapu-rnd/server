from loader import *

@app.route('/registrations', methods=['POST'])
def registrations():
    """route for  register users"""
    try:
        idUser = GenerateAlfNumStr(10)
        idBalance = GenerateAlfNumStr(10)
        INNSI = f'"{idUser}", "{request.json["name"]}", "{request.json["numb"]}", "{request.json["id_tg"]}", "{request.json["surname"]}"'
        check = InsertData(T="users", V=INNSI)

        #set to balance 500 points
        startBalanceData = f'"{idBalance}", "{idUser}", "{float(500)}" '
        startBalance = InsertData(T="balance", V=startBalanceData)

        con.commit()
        if len(check) > 1 and len(startBalance) > 1:
            return jsonify({"action": "success", "id": idUser})
        else:
            return jsonify({"action": "errorData"})
    except Exception as e:
        return jsonify({"action": "errorData"})
