import requests

def make_get_request(url):
    """make a GET request to the specified URL."""
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

def make_post_request(url, data):
    """make a POST request to the specified URL with given data."""
    response = requests.post(url, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

if __name__ == "__main__":
    # usage of GET and POST requests
    print("Making GET request to http://localhost:8000")
    make_get_request('http://localhost:8000')
    
    print("\nMaking POST request to http://localhost:8000 with data {'key': 'value'}")
    make_post_request('http://localhost:8000', data={'Name': 'alice'})
