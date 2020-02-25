from flask import Flask , render_template

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tetris', 'Passatempo', 'GBA')
    jogo2 = Jogo('Mario', 'Aventura', 'SNES')
    jogo3 = Jogo('Pkemon', 'Aventura', 'GBA')

    lista = [jogo1,jogo2,jogo3]
    return render_template('lista.html', titulo='Jogoteca', jogos=lista)

app.run()