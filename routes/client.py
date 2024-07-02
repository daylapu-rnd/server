from loader import *
from  sqliteMode import *


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


@app.route('/client/profile', methods=['POST'])
def ProfileCommand():
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



@app.route('/client/orders/get_orders', methods=['POST'])
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
