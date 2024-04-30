<h4>**Criando formulário com WTForms, Flask-WTF e sintaxe do Jinja pra formulários**</h4>

No formulário anterior usamos o **request.form** para acessar diretamente os dados do formulário. Quando utilizamos **request.form** precisamos fazer manualmente a validação dos dados recebidos e o tratamento de erros.

Por outro lado, ao utilizar o **Flask-WTF** com **classes** de formulário, como **FlaskForm** podemos definir os campos do formulário e as validações de forma mais organizada. Além disso, o Flask-WTF lida automaticamente com a validação dos dados do formulário e a geração de mensagens de erro.

A sintaxe de formulário oferecida pelo Jinja permite que a gente insira  os elementos do formulário, como quantidade de caracteres, requerido, formato de e-mail, etc, diretamente.
Isso ajuda a garantir que os dados inseridos pelo usuário sejam válidos antes de serem processados.

A sintaxe fornecida pelo **Jinja** para renderização de campos de formulário é bastante simples e direta:

<h4>Formulário de Registro:</h4>

    <form method="POST" action="/register">
        {{ form.hidden_tag() }}
        <div>
            {{ form.username.label }} {{ form.username(size=20) }}
        </div>
        <div>
            {{ form.email.label }} {{ form.email(size=20) }}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>


O **Jinja** é um mecanismo de template para Python. Ele é usado principalmente em frameworks web como Flask e Django para renderizar modelos HTML.