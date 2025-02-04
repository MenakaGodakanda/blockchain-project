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
![Screenshot 2025-02-04 032335](https://github.com/user-attachments/assets/c889d0a1-e30c-4022-beb5-a250713f227b)

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
![Screenshot 2025-02-04 142650](https://github.com/user-attachments/assets/fc58fd55-3f34-4c0c-99b9-3c055eeecc52)

## API Endpoints
Open a browser and go to `http://localhost:5000`.

### 1. Home
- GET / - Returns a welcome message.
![Screenshot 2025-02-04 154615](https://github.com/user-attachments/assets/fc7ec80b-0694-4a35-a2c8-6cdbfb3d8813)

- When you start the server (`python3 node.py`), the blockchain is initialized with a **Genesis Block**:
- The **Genesis Block** is the first block in the blockchain, created with default values.
- Example of the Genesis Block:
![Screenshot 2025-02-04 154653](https://github.com/user-attachments/assets/861b94a1-23b2-41ce-ba13-b8f7b7ce9dca)


### 2. Mine a Block
POST /mine - Mines a new block with provided data.

Request Example:
```
curl -X POST http://127.0.0.1:5000/mine -H "Content-Type: application/json" -d '{"data": "My first mined block"}'
```
Response Example:
![Screenshot 2025-02-04 154702](https://github.com/user-attachments/assets/f29d76a9-4d01-43bc-922b-844e727ca89d)

### 3. Get the Blockchain
GET /chain - Retrieves the entire blockchain.

Response Example:
![Screenshot 2025-02-04 154710](https://github.com/user-attachments/assets/d61a958e-69fe-43e6-8615-a7faf17ef152)

### 4. Validate the Blockchain
GET /validate - Checks if the blockchain is valid.
Response Example:
![Screenshot 2025-02-04 155218](https://github.com/user-attachments/assets/3d6e6729-e33d-4c62-b5b6-21a4576e459e)

## Web Interface
- Stop running `node.py`.
- The `web_interface.py` script will allow users to mine blocks and view the blockchain in a browser.
Run the Web Interface:
```
python3 web_interface.py
```
![Screenshot 2025-02-04 153257](https://github.com/user-attachments/assets/7b9c57e6-86d5-45f0-beb1-331ad7f1e617)

### 1. Mine a Block
- Enter data in the input field.
- Click "Mine Block" to create a new block.
- The blockchain updates in real-time.
![Screenshot 2025-02-04 154222](https://github.com/user-attachments/assets/ca666b94-5f00-4f5d-8bc3-0e1809d02e5f)
![Screenshot 2025-02-04 154231](https://github.com/user-attachments/assets/d65ebe05-cabf-4fcf-b080-af4053679f3e)

### 2. View the Blockchain
   - The entire blockchain is displayed on the page.
   - Each block includes **index, data, and hash**.
![Screenshot 2025-02-04 154243](https://github.com/user-attachments/assets/21df8d77-80fa-44f3-9bae-c64fd37ac405)

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





