from flask import Flask, render_template, request, redirect, url_for, jsonify
from blockchain import Blockchain, Block
import time

app = Flask(__name__)

# Instantiate blockchain
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html', blockchain=blockchain.chain)

@app.route('/mine', methods=['POST'])
def mine():
    data = request.form.get("data", "Default Data")
    previous_block = blockchain.get_latest_block()
    proof = blockchain.proof_of_work(previous_block.hash)
    new_block = Block(len(blockchain.chain), previous_block.hash, time.time(), data, proof)
    blockchain.add_block(new_block)
    return redirect(url_for('index'))

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [block.__dict__ for block in blockchain.chain]
    return jsonify({"length": len(chain_data), "chain": chain_data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# Create index.html template
index_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Blockchain Web Interface</title>
    <script>
        async function mineBlock() {
            const data = document.getElementById("data").value;
            await fetch("/mine", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: "data=" + encodeURIComponent(data)
            });
            location.reload();
        }
    </script>
</head>
<body>
    <h1>Simple Blockchain</h1>
    <form onsubmit="event.preventDefault(); mineBlock();">
        <input type="text" id="data" name="data" placeholder="Enter data" required>
        <button type="submit">Mine Block</button>
    </form>
    <h2>Blockchain</h2>
    <ul>
        {% for block in blockchain %}
        <li>Index: {{ block.index }} | Data: {{ block.data }} | Hash: {{ block.hash }}</li>
        {% endfor %}
    </ul>
</body>
</html>
'''

# Save index.html to templates directory
import os
os.makedirs("templates", exist_ok=True)
with open("templates/index.html", "w") as f:
    f.write(index_html)

