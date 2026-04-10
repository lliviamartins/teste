from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()

    produto = int(data['produto'])
    pagamento = int(data['pagamento'])

    if produto == 3:
        return jsonify({'resultado': 'Operação finalizada.'})

    if produto == 1:
        nome = "Assinatura mensal"
        preco = 120
    elif produto == 2:
        nome = "Assinatura anual"
        preco = 75
    else:
        return jsonify({'resultado': 'Produto inválido!'})

    if pagamento == 1:
        metodo = "PIX/Dinheiro"
        vfinal = preco * 0.90
    elif pagamento == 2:
        metodo = "Débito"
        vfinal = preco * 0.95
    elif pagamento == 3:
        metodo = "Crédito"
        vfinal = preco * 1.10
    else:
        return jsonify({'resultado': 'Pagamento inválido!'})

    return jsonify({
        'resultado': f"""
Produto: {nome}
Pagamento: {metodo}
Valor final: R$ {vfinal:.2f}
"""
    })

if __name__ == '__main__':
    app.run(debug=True)
