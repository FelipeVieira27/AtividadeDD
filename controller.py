from flask import Flask, request

fomulario = Flask(__name__)

@formulario.route('/soma', methods=['POST'])
def escrever_numero():
    if request.method == 'POST':
        n1 = request.form['n1']
        n2 = request.form["n2"]
        potenciacao = n1 ** n2
    return "Seu resultado é: ", potenciacao

if __name__ == '__main__':
    formulario.run(host='0.0.0.0', port=5000)