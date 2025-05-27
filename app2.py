from flask import Flask, request
import requests
import decode
import encode

app = Flask(__name__)

private_key_b = ""
public_key_a = ""

@app.route('/webhook', methods=['POST'])
def receba():
    encoded = request.json['mensagem']
    decoded = decode.decode(encoded)
    print(f"Mensagem recebida: {decoded}")
    return {"status":"ok"}

@app.route('/send', methods=['POST'])
def enviar():
    decoded = request.json['mensagem']
    encoded = encode.encode(decoded)
    requests.post("http://localhost:5000/webhook", json={"mensagem":encoded})
    return {"status":"sent"}

if __name__ == '__main__':
    app.run(port=5001)