from flask import Flask, request, render_template

form = Flask(__name__)

@form.route('/')
def insira():
    return render_template('form.html')

@form.route('/soma', methods=['POST'])
def soma():
    if request.method == 'POST':
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        media = (n1 + n2) / 2
        return f"A média dos números inseridos {n1} e {n2} é {media}"
    else:
        return "Erro: Método de requisição incorreto"

if __name__ == '__main__':
    form.run(debug=True)