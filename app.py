from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/callback")
def callback():
    # Captura o código da URL
    code = request.args.get("code")

    if not code:
        return "Erro: parâmetro 'code' não encontrado na URL", 400

    # Retorno simples como texto para o KNIME ou navegador
    return f"Code recebido: {code}"

@app.route("/")
def home():
    return "Servidor da API Tiny rodando."

if __name__ == "__main__":
    import os  # <-- ESSENCIAL (esse era o erro anterior)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
