from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "backend running"}), 200

@app.route("/compute", methods=["POST"])
def compute():
    data = request.json
    result = data.get("value", 0) * 6 
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
