from flask import Flask, jsonify, request
from blockchain import Blockchain, Block
import time

app = Flask(__name__)

# Instantiate blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['POST'])
def mine_block():
    data = request.json.get("data", "Default Data")
    previous_block = blockchain.get_latest_block()
    proof = blockchain.proof_of_work(previous_block.hash)
    new_block = Block(len(blockchain.chain), previous_block.hash, time.time(), data, proof)
    blockchain.add_block(new_block)
    return jsonify({"message": "Block mined", "block": new_block.__dict__}), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [block.__dict__ for block in blockchain.chain]
    return jsonify({"length": len(chain_data), "chain": chain_data}), 200

@app.route('/validate', methods=['GET'])
def validate_chain():
    for i in range(1, len(blockchain.chain)):
        current = blockchain.chain[i]
        previous = blockchain.chain[i - 1]
        if current.previous_hash != previous.hash or \
           not blockchain.is_valid_proof(current.proof, current.previous_hash):
            return jsonify({"valid": False, "error": "Invalid chain"}), 400
    return jsonify({"valid": True}), 200

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Blockchain API is running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

