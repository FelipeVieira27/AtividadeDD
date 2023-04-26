from flask import Flask, request, render_template

form = Flask(__name__)

@form.route('/')
def insira():
    return render_template('form.html')

@form.route('/media', methods=['GET', 'POST'])
def media():
    if request.method == 'POST':
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        n3 = float(request.form['n3'])
        media = (n1 + n2 + n3) / 3
        return f"A média dos números inseridos {n1}, {n2} e {n3} é igual a {media}"
    else:
        return "Erro: Método de requisição incorreto"

if __name__ == '__main__':
    form.run(debug=True)