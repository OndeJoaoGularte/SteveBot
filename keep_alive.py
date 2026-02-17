from flask import Flask
from threading import Thread
import os # Precisamos disso para ler a porta do Render

app = Flask('')

@app.route('/')
def home():
    return "SteveBot is alive!"

def run():
    # O Render nos dá a porta pela variável de ambiente 'PORT'. 
    # Se não houver uma (como no seu PC), ele usa a 8080 por padrão.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()