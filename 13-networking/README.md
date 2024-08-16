
This repo provides examples of basic networking operations using Python. It includes implementations for TCP communication using sockets and making HTTP requests. 

1. **Socket Communication**: Demonstrates how to create a simple TCP server and client using Python's `socket` library.
2. **HTTP Requests**: Shows how to perform HTTP GET and POST requests using the `requests` library.

## Files

### 1. Socket Communication (`sockets.py`)

#### Description
This script contains two main functions:
- **`start_server(host='localhost', port=65432)`**: Starts a TCP server that listens on the specified `host` and `port`. The server echoes back any data it receives from clients.
- **`start_client(host='localhost', port=65432, message='Hello, World!')`**: Connects to a TCP server at the specified `host` and `port`, sends a message, and prints the response from the server.

#### How to Use
1. **Run the Server:**
   - Open a terminal and execute the script to start the server:
     ```bash
     python sockets.py
     ```
   - The server will start and listen for incoming connections.

2. **Run the Client:**
   - The client is automatically started by the script after the server starts. It will connect to the server, send a message, and print the server's response.

#### Example Output

```bash
Server listening on localhost:65432
Connected by ('127.0.0.1', 54321)
Received: Hello, World!
Received from server: Hello, World!
```


### 2. HTTP Requests (`http_requests.py`)

#### Description
This script demonstrates how to perform HTTP requests using the `requests` library:
- **`make_get_request(url)`**: Makes a GET request to the specified `url` and prints the status code and response text.
- **`make_post_request(url, data)`**: Makes a POST request to the specified `url` with the given `data` and prints the status code and response text.

#### How to Use
1. **Ensure a Local Server is Running:**
   - You need a server running on `http://localhost:8000`. You can use Python's built-in HTTP server for testing:
     ```bash
     python -m http.server 8000
     ```

2. **Run the Script:**
   - Execute the script to perform GET and POST requests:
     ```bash
     python http_requests.py
     ```

#### Example Output

```bash

Making GET request to http://localhost:8000
Status Code: 200
Response Text: (Response from the local server)

Making POST request to http://localhost:8000 with data {'key': 'value'}
Status Code: 200
Response Text: (Response from the local server)

```
