from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "yatish", "email": "yatishdurga@gmail.com"},
    {"id": 2, "name": "satish", "email": "satish@gmail.com"}
]

@app.route("/get_user", methods=['GET'])
def get_user():
    return users 

@app.route("/get_user_id/<int:id>",methods=['GET'])
def get_user_by_id(id):
    user=next((item for item in users if item ["id"]==id),None)
    if user:
        return jsonify(user)
    return None

if __name__ == '__main__':
    app.run(debug=True)
