## What is Flask?

[Flask](https://flask.palletsprojects.com/) is a lightweight WSGI web application framework in Python. It is designed to be simple and easy to use, allowing developers to build web applications quickly with minimal setup. Flask provides tools and libraries for routing, templating, and handling HTTP requests and responses. It is often used for building web APIs and small to medium-sized web applications.

## Getting Started

To run this example, follow these steps:

### Prerequisites

- Python 3.x installed on your machine.
- `pip` (Python package installer) available.

### Installation

1. **Clone the repository** (if applicable):
   
2. **Install Flask**:
    ```bash
    pip install flask
    ```

### Running the Application

1. **Run the Flask application**:
    ```bash
    python flask_example.py
    ```

2. **Access the application**:
    - Open a web browser and go to `http://127.0.0.1:5000/` to see the welcome message.
    - Access `http://127.0.0.1:5000/api/greet?name=test` to see a JSON response with a personalized greeting.

### Usage

- **Root URL (`/`)**: Displays a simple welcome message.
- **API Endpoint (`/api/greet`)**: Accepts a query parameter `name` and returns a JSON object with a greeting message.

