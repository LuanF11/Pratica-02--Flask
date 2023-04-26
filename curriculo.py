from flask import Flask,render_template as rt

app = Flask(__name__,template_folder='paginas')

@app.route('/')
def index():
    return rt('index.html')

@app.route('/sobre')
def sobre():
    return rt('sobre.html', titulo='Sobre Mim', texto='Olá! Meu nome é Luan tenho 20 Anos interessado em Tecnologia|Games|Idiomas, Filmes e livros de fantasia e ficção cientifica.')

@app.route('/experiencia')
def experiencia():
    return rt('experiencia.html', titulo='Experiência Profissional', texto='Estágiario como técnico em informática fazendo manutenção de computadores')

@app.route('/formacao')
def formacao():
    return rt('formacao.html', titulo='Formação Acadêmica', texto='Téncino em Informática e cursando Sistema de Informação.')

@app.route('/contato')
def contato():
    return rt('contato.html', titulo='Contato', texto='Segue os contatos',contato='E-mail => luaninfo09@gmail.com',contato2='Telefone => 99646-5465')


if __name__ == '__main__':
    app.run(debug=True)

    