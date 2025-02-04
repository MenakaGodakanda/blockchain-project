# blockchain-project

This project is a simple blockchain implementation using Python and Flask. It allows users to create a blockchain, mine new blocks, validate the chain, and retrieve the entire blockchain via API endpoints.

## Overview
<img width="1027" alt="Screenshot 2025-02-04 at 3 25 51 pm" src="https://github.com/user-attachments/assets/80753b16-da5f-4e43-8f07-229bc00ba397" />

### Explanation

#### 1. API Endpoints (node.py)
- User mine a new block via terminal.
- The blockchain updates dynamically.

#### 2. Web Interface (web_interface.py)
- User enter data and click "Mine Block".
- The blockchain updates dynamically.

#### 3. Blockchain (blockchain.py)
- Stores the chain: Manages a list of Block objects.
- Proof of Work: Ensures computational difficulty in block mining.
- Validation: Checks the integrity of the blockchain.

#### 4. Flask Web Server
- For `node_py` provivide RESTful API endpoints:
  - Handles user requests via API endpoints (`/mine`, `/chain`, `/validate`, `/`).
  - Calls blockchain functions to process blocks.

- For `web_interface.py`
  - Handles HTTP Requests.
  - Routes:
    - `/` → Serves the Web Interface.
    - `/mine` → Mines a new block with input data.
    - `/chain` → Retrieves the full blockchain.


## Features

- Create and maintain a blockchain
- Mine new blocks with Proof of Work
- Validate the blockchain
- Retrieve the full blockchain data via REST API

## Technologies Used
- Python 3
- Flask (for REST API)
- hashlib (for cryptographic hashing)

## Installation
### Prerequisites
Make sure you have Python 3 installed on your system. You can check by running:
```
python3 --version
```

### Clone the Repository
```
git clone https://github.com/MenakaGodakanda/blockchain-project.git
cd blockchain-project
```

### Create a Virtual Environment
```
python3 -m venv block
source block/bin/activate
```

### Install Dependencies
```
pip install flask
```

## Running the Application
Start the Flask server:
```
python3 node.py
```
You should see output like:

## API Endpoints
Open a browser and go to `http://localhost:5000`.

### 1. Home
- GET / - Returns a welcome message.

- When you start the server (`python3 node.py`), the blockchain is initialized with a **Genesis Block**:
- The **Genesis Block** is the first block in the blockchain, created with default values.
- Example of the Genesis Block:


### 2. Mine a Block
POST /mine - Mines a new block with provided data.

Request Example:
```
curl -X POST http://127.0.0.1:5000/mine -H "Content-Type: application/json" -d '{"data": "My first mined block"}'
```
Response Example:

### 3. Get the Blockchain
GET /chain - Retrieves the entire blockchain.

Response Example:

### 4. Validate the Blockchain
GET /validate - Checks if the blockchain is valid.
Response Example:

## Web Interface
- Stop running `node.py`.
- The `web_interface.py` script will allow users to mine blocks and view the blockchain in a browser.
Run the Web Interface:
```
python3 web_interface.py
```
### 1. Mine a Block
- Enter data in the input field.
- Click "Mine Block" to create a new block.
- The blockchain updates in real-time.

### 2. View the Blockchain
   - The entire blockchain is displayed on the page.
   - Each block includes **index, data, hash, and previous hash**.

## Block Details
- **Index**: Position of the block in the chain.
- **Previous Hash**: The hash of the previous block, ensuring continuity.
- **Timestamp**: When the block was created.
- **Data**: The user-provided input.
- **Proof**: The proof of work satisfying the difficulty level.
- **Hash**: The unique hash for this block.

## Project Structure
```
blockchain-project/
│── blockchain.py
│── node.py
│── web_interface.py
│── README.md
```

## License
This project is open-source and available under the MIT License.





