from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/calculadora')
def exibir_calculadora():
    return render_template('calculadora.html')


@app.route('/processar', methods=['POST'])
def calcular():

    numero1 = float(request.form['numero1'])
    numero2 = float(request.form['numero2'])
    operacao = request.form['operacao']

    resultado = ""

    if operacao == 'adicao':
        resultado = numero1 + numero2

    elif operacao == 'subtracao':
        resultado = numero1 - numero2

    elif operacao == 'multiplicacao':
        resultado = numero1 * numero2

    elif operacao == 'divisao':

        if numero2 == 0:
            resultado = "Não é possível dividir por 0!"

        else:
            resultado = numero1 / numero2

    return render_template('calculadora.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
