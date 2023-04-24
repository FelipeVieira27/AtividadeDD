from flask import Flask, request, render_template

forms = Flask(__name__)

@forms.route('/')
def inserir():
    return render_template("forms.html")

@forms.route('/soma', methods=['POST, GET'])
def soma():
    if request.method == 'POST':
        n1 = int(request.form['n1'])
        n2 = int(request.form["n2"])
        media = (n1 + n2) / 2
    else:
        n1 = int(request.form['n1'])
        n2 = int(request.form["n2"])
        media = (n1 + n2) / 2
    return f"A média dos números inseridos {n1, n2} é {media}"

if __name__ == '__main__':
    forms.run(host='0.0.0.0', port=5000)