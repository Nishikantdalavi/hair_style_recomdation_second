import requests

# Example JSON data
data = {"key": "value"}

# Set the headers
headers = {"Content-Type": "application/json"}

# Make the POST request with JSON data and headers
response = requests.post("http://127.0.0.1:5000", json=data, headers=headers)

# Print the response
print(response.text)
