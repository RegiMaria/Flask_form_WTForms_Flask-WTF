from flask import render_template
from app.forms import RegistrationForm
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Lógica de processamento do formulário aqui
        return 'Formulário enviado com sucesso!'
    return render_template('register.html', form=form)