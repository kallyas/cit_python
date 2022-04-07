from flask import Flask, render_template, request, jsonify
from tuesday_quiz import User, Blockchain

app = Flask(__name__)

blockchain = Blockchain()
user = User()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user.login(username, password):
            return dashboard(username=username)
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/dashboard', methods=['GET'])
def dashboard(username):
    return render_template('index.html', username=username)

@app.route('/logout', methods=['GET'])
def logout():
    render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user.create_user(username, password):
            return render_template('login.html')
        else:
            return render_template('signup.html', error='Username already exists')
    else:
        return render_template('signup.html')


@app.route('/send-money', methods=['POST'])
def send_money():
    data = request.get_json()
    if data['sender'] == data['recipient']:
        return jsonify({'error': 'Sender and recipient cannot be the same'}), 400
    if blockchain.get_balance(data['sender']) < data['amount']:
        return jsonify({'error': 'Insufficient funds {}'.format(blockchain.get_balance(data['sender']))}), 400
    blockchain.new_transaction(data['sender'], data['recipient'], data['amount'])
    return jsonify({'message': 'Transaction added to the blockchain'}), 201

@app.route('/recieve-money/<string:address>', methods=['POST'])
def recieve_money(address):
    return jsonify({'balance': blockchain.get_balance(address)}), 200

@app.route('/deposit-money', methods=['POST'])
def deposit_money():
    data = request.get_json()
    blockchain.new_transaction(data['sender'], data['recipient'], data['amount'])
    return jsonify({'message': 'Transaction added to the blockchain'}), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes)
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
