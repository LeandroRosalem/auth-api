from flask import Flask, request, jsonify

app = Flask(__name__)

# Salvar último code recebido (em memória para este exemplo)
last_code = ""

@app.route("/callback")
def callback():
    global last_code
    code = request.args.get("code")
    last_code = code
    return jsonify({"code": code})

@app.route("/ultimo-code")
def get_last_code():
    return jsonify({"code": last_code})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
