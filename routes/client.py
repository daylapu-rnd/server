from loader import *
from  sqliteMode import *
from _datetime import datetime


@app.route('/client/registrations', methods=['POST'])

def registrations():
    """route for  register users"""
    try:
        clientID = GenerateAlfNumStr(10)
        INNSI = f'"{clientID}", "{request.json["tg_id"]}", "{request.json["name"]}", "{request.json["email"]}", "{request.json["phone"]}"'

        check = InsertData('clients', INNSI)
        con.commit()
        if len(check) > 1:
            return jsonify({"action": "success", "id": clientID})
        else:
            return jsonify({"action": "errorData"})
    except Exception as e:
        log_error(e)
        print(e)
        return jsonify({"action": "errorData"})


@app.route('/client/profile/change_info', methods=['POST'])
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
        return jsonify({"action": "errorData"})


@app.route('/admin/get_all', methods=['POST'])
def AdminGetAll():
    """
        Admin route for retrieving all users.
        """
    try:
        # Example of retrieving data from your database (modify as per your database structure):
        user_data = SelectAllAllData("users", "*")
        if user_data:
            return jsonify({"action": "success", "data": user_data})
        else:
            return jsonify({"action": "errorData", "data": "error"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})

@app.route('/client/profile', methods=['POST'])
def ProfileClientCommand():
    """
        Admin route for retrieving all users.
    """
    request_id = request.json["tg_id"]
    try:
        # Example of retrieving data from your database (modify as per your database structure):
        user_data = SelectData("clients", "tg_id", request_id)
        if user_data:
            return jsonify({"action": "success", "data": user_data})
        return jsonify({"action": "errorData", "data": f"error"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})


@app.route('/user/profile', methods=['POST'])
def ProfileUserCommand():
    """
        Admin route for retrieving all users.
    """
    request_id = request.json["tg_id"]
    try:
        # Example of retrieving data from your database (modify as per your database structure):
        user_data = SelectData("users", "tg_id", request_id)
        if user_data:
            return jsonify({"action": "success", "data": user_data})
        return jsonify({"action": "errorData", "data": f"error"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})


@app.route('/client/get_orders', methods=['POST'])
def get_orders():
    """route for get all orders of client"""
    request_id = request.json["client_id"]
    try:
        orders_data = SelectAllData("orders", "client_id", request_id)
        if orders_data:
            return jsonify({"action": "success", "data": orders_data})
        return jsonify({"action": "errorData", "data": f"error"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})


@app.route('/client/orders/create_order', methods=['POST'])
def create_order():
    """route for create order"""
    new_order_id = GenerateAlfNumStr(10)
    values = f'"{new_order_id}", "{request.json["client_id"]}", "{request.json["pet_id"]}", "{request.json["service_type"]}", "{request.json["start_date"]}", "{request.json["start_time"]}", "{request.json["end_date"]}", "{request.json["end_time"]}", "{request.json["service_details"]}", "{request.json["options"]}", "{request.json["region"]}",  "{request.json["city"]}", "{request.json["district"]}", "{request.json["street"]}", "{request.json["house"]}", "{request.json["building"]}", "{request.json["apartment"]}", "{request.json["status"]}"'
    print(values)
    try:
        check = InsertData(T="orders", V=values)
        if len(check) > 1:
            return jsonify({"action": "success"})
        return jsonify({"action": "error"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})


@app.route('/client/orders/get_order', methods=['POST'])
def get_order():
    """route for get order by order_id"""
    order_id = request.json["order_id"]
    try:
        order_data = SelectData("orders", "order_id", order_id)
        if order_data:
            return jsonify({"action": "success", "data": order_data})
        return jsonify({"action": "errorData", "data": f"error"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})


@app.route('/client/orders/update_order_info', methods=['POST'])
def update_order_info():
    """route for update order info"""
    try:
        order_id = request.json["order_id"]
        service_type = request.json['service_type']
        start_date = request.json['start_date']
        start_time = request.json['start_time']
        end_date = request.json['end_date']
        end_time = request.json['end_time']
        service_details = request.json['service_details']
        options = request.json['options']
        region = request.json['region']
        city = request.json['city']
        district = request.json['district']
        street = request.json['street']
        house = request.json['house']
        building = request.json['building']
        apartment = request.json['apartment']
        status = request.json['status']

        updateable_table = "('service_type', 'start_date', 'start_time', 'end_date', 'end_time', 'service_details', 'options', 'region', 'city', 'district', 'street', 'house', 'building', 'apartment', 'status')"
        values = f'"{service_type}", "{start_date}", "{start_time}", "{end_date}", "{end_time}", "{service_details}", "{options}", "{region}", "{city}", "{district}", "{street}", "{house}", "{building}", "{apartment}", "{status}"'
        check = UpdateData("orders", updateable_table, values, "order_id", order_id)
        if len(check) > 1:
            return jsonify({"action": "success"})
        return jsonify({"action": "errorData 1"})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})


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

