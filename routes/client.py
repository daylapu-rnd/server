from loader import *
from  sqliteMode import *
from _datetime import datetime


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


@app.route('/consent/save_response', methods=['POST'])
def saveUserConsent():
    """
    Route for saving user's consent response.

    Expects JSON data with the following fields:
    - id_tg: Telegram ID of the user (int)
    - response: User's response ('accept' or 'decline')
    - timestamp: Timestamp of the response (string)

    Returns:
    - {"action": "success"} if data is successfully saved.
    - {"action": "errorData"} if there is an error during the process.
    """
    try:
        id_agreement = GenerateAlfNumStr(7)
        user_tg_id = request.json["user_tg_id"]
        response = request.json["response"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Example of inserting data into your database (modify as per your database structure):
        status = InsertData("agreement", f'"{id_agreement}","{user_tg_id}", "{response}", "{timestamp}"')

        if len(status) > 0:

            return jsonify({"action": "success"})
        else:
            return jsonify({"action": "errorData"})
    except Exception as e:
        return jsonify({"action": "errorData"})




@app.route('/consent/get_response', methods=['POST'])
def getUserConsent():
        """
        Route for retrieving user's consent response.

        Expects JSON data with the following fields:
        - id_tg: Telegram ID of the user (int)

        Returns:
        - {"action": "success", "data": {"response": <response>, "timestamp": <timestamp>}}
          if data is successfully retrieved.
        - {"action": "errorData"} if there is an error during the process.
        """
        try:
            user_tg_id = request.json["user_tg_id"]
            # Example of retrieving data from your database (modify as per your database structure):
            response_data = SelectData(T="agreement", C= "user_tg_id", V= user_tg_id)
            if response_data:
                response = response_data["response"]
                timestamp = response_data["datetime"]
                id_agreement = response_data["id_agreement"]

                return jsonify({"action": "success", "data": {"response": response, "datetime": timestamp, "id_agreement":id_agreement}})
            else:
                return jsonify({"action": "errorData", "data": {"response": None, "datetime": None}})
        except Exception as e:
            return jsonify({"action": "errorData"})