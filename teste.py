from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa as variáveis de ambiente
TOKEN = os.getenv("TOKEN")
prefixo = os.getenv("PREFIXO")

print(f"Bot Token: {TOKEN}")
print(f"Prefixo: {prefixo}")
