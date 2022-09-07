import os
from flask import Flask, request, abort, render_template

app = Flask(__name__)

@app.route('/calc')
def calculadoraweb():
    valor1=request.args.get('val1')
    valor2=request.args.get('val2')
    operacao=request.args.get('operacao')

    print(operacao)

    try:
        val1 = int(valor1)
    except:
        abort(404)

    try:
        val2 = int(valor2)
    except:
        abort(404)


    if (operacao == "soma"):
        Calculo = val1 + val2
    elif (operacao == "subtracao"):
        Calculo = val1 - val2
    elif (operacao == "divisao"):
        if(val2 == 0 & val1 == 0):
            abort(422)
        else:
            Calculo = val1 / val2
    elif (operacao == "multiplicacao"):
        Calculo = val1 * val2
    else:
        abort(404)

    return str(Calculo)
    #Para serialização, o retorno sempre será string

@app.route('/') 
def main(): #declara a função
    return render_template('calculadora.html') #coloca o arquivo onde deve buscar as informações


@app.route('/calcula',methods=['POST','GET'])#define o metodo que sera utilizado e a função (calc) que sera utilizada
def calculaform(): #define a função que será utilizada
    valor1=request.form['v1'] #informa as variaveis
    valor2=request.form['v2'] 
    operacao=request.form['operacao']

    print(operacao) #imprimi a operação que foi feita

    try:
        val1 = int(valor1) #declara que o valor deve ser transformado em inteiro
    except:
        abort(404)

    try:
        val2 = int(valor2) #declara que o valor deve ser transformado em inteiro
    except:
        abort(404)

#declara as operações que existem e o que elas devem executar
    if (operacao == "soma"): 
        Calculo = val1 + val2
    elif (operacao == "subtracao"):
        Calculo = val1 - val2
    elif (operacao == "divisao"):
        if(val2 == 0 & val1 == 0):
            abort(422)
        else:
            Calculo = val1 / val2
    elif (operacao == "multiplicacao"):
        Calculo = val1 * val2
    else:
        abort(404)

    return str(Calculo) #retorna o valor da conta
    #Para serialização, o retorno sempre será string

@app.route('/hello/')
@app.route('/hello/<name>')

if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 5005)) #declara a porta onde aparecerá o formulãrio para fazer a soma
    app.run(host='127.0.0.1', port=port) #declara o localhost que aparecera a conta
