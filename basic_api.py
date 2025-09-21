from flask import Flask, jsonify, request

app = Flask(__name__)

datas = [
    {"id": 1, "name": "arka", "role": "eepy"}
]

@app.route('/')
def home():
    return jsonify({"message": "Home page of team meow API"})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(datas)

@app.route('/api', methods=['GET'])
def api_page():
    return jsonify({"message" : "This is API page for team Meow"})

@app.route('/api/data', methods=['POST'])
def create_data():
    data = request.get_json()
    datas.append(data)
    return jsonify({"message": "Data received!", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True)