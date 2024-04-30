from flask import Flask
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config['SECRET_KEY'] = 'CHAVE_SECRETA'  # Defina a chave secreta diretamente

# Configurar o Flask-WTF para usar a chave secreta da aplicação Flask
csrf = CSRFProtect(app)

if __name__ == '__main__':
    app.run(debug=True)