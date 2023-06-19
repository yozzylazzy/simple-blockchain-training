from flask import Flask, render_template, request
from blockchain import Blockchain, Block
import time
import json

# --- Generate Blockchain ---
blockchain = Blockchain()
blockchain.add_block(Block(1, time.time(), 'Block Sector A', '2020130002'))
blockchain.add_block(Block(2, time.time(), 'Block Sector B', '2020130001'))
blockchain.add_block(Block(3, time.time(), 'Block Sector C', '2020130017'))

# --- Web 3.0 App ---
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', blockchain=blockchain)

@app.route("/blocks")
def blocks():
    return render_template('blocks.html', blockchain=blockchain)

@app.route("/add_block")
def add_block():
    new_block = Block(blockchain.get_length() + 1, time.time(), request.args.get('sector'), request.args.get('student_id'))
    blockchain.add_block(new_block)
    return render_template('add_block.html', blockchain=blockchain, new_block=new_block)

@app.route("/validate")
def validate():
    return render_template('validate.html', blockchain=blockchain)

@app.route("/validate_block")
def validate_block():
    block = blockchain.get_block(int(request.args.get('block_id')))
    return render_template('validate_block.html', blockchain=blockchain, block=block)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
