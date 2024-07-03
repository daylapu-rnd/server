from loader import *
from  sqliteMode import *
from _datetime import datetime


@app.route('/admin/get_orders/by_status', methods=['GET'])
def get_users_by_status():
    """route for getting orders by status"""
    try:
        status = request.json['status']
        order_data = SelectData("orders", "status", status)
        if len(order_data) > 0:
            return jsonify({"action": "success", "data": order_data})
        return jsonify({"action": "error", "data": {}})
    except Exception as e:
        log_error(e)
        return jsonify({"action": "errorData"})