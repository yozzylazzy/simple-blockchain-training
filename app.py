from flask import Flask, render_template, request, jsonify
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

# create jsonify
def to_json(block):
    return {
        "Block #{}".format(block.index),
        "Timestamp: {}".format(block.timestamp),
        "Data: {}".format(block.data),
        "Previous Hash: {}".format(block.previous_hash),
        "Hash: {}".format(block.hash)   
    }

@app.context_processor
def inject_blockchain():
    return {"blockchain": blockchain}

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, load_dotenv=True)
