import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    primos = "A Jessica está cansada hoje e ta passando isso pra mim"
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host='0.0.0.0', port=port)