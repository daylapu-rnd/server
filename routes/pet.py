from loader import *
from  sqliteMode import *

@app.route('/pets/addPet', methods=['POST'])
def addPet():
    """route for  register users"""
    try:
        petID = GenerateAlfNumStr(10)
        INNSI = f'''"{petID}", "{request.json["client_id"]}", "{request.json["pet_name"]}", "{request.json["pet_type"]}", "{request.json["sex"]}",
                        "{request.json["bitrhday"]}", "{request.json["features"]}", "{request.json["sterilization"]}"'''

        check = InsertData('pets', INNSI)
        con.commit()
        if len(check) > 1:
            return jsonify({"action": "success", "id": petID})
        else:
            return jsonify({"action": "errorData"})
    except Exception as e:
        log_error(e)
        print(e)
        return jsonify({"action": "errorData"})
    
@app.route('/pets/getOne', methods=['POST'])
def getOnePet():
    """route for reading user data"""
    try:
        data = SelectData("pets", "pet_id", request.json["pet_id"])
        return jsonify({"action": "success", "data": data})
    except Exception as e:
        return jsonify({"action": "errorData"})
    
@app.route('/pets/removePet/<pet_id>', methods=['DELETE'])
def removePet(pet_id):
    """route for reading user data"""
    try:
        data = DeleteData("pets", "pet_id", pet_id)
        return jsonify({"action": "success"})
    except Exception as e:
        return jsonify({"action": "errorData"})
    
