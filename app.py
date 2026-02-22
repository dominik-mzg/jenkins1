from flask import Flask
import os

app = Flask(__name__)

@app.get('/')
def home():
    api_key = os.getenv('MY_API_KEY', 'brak-klucza')
    return f"<h1>Aplikacja Flask działa!</h1><p>Klucz: {api_key}</p>"

if __name__ == '__main__':
    # Ważne: host='0.0.0.0' pozwala Dockerowi wystawić apkę na zewnątrz
    app.run(host='0.0.0.0', port=5000)
