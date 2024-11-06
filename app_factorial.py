from flask import Flask, jsonify

app = Flask(__name__)

#Calcular factorial
def calcular_factorial(n):
    if (n < 0):
        return {"error": "El número debe ser positivo"}
    elif (n == 0 or n == 1):
        return 1
    else:
        return n * calcular_factorial(n-1)

#Página de resultados
@app.route('/<int(signed=True):n>', methods=['GET'])
def factorial(n):
    retorno = calcular_factorial(n)

    if retorno is None:
        return {"error": "Es none"}
    else:
        return jsonify(retorno)

if __name__ == '__main__':
    app.run(debug=True)