import requests

url = "http://192.168.68.50:5001/path"
data = {
    "obstacles": [
        {"x": 0, "y": 9, "id": 1, "d": 2},
        {"x": 19, "y": 14, "id": 5, "d": 6}
    ]
}
response = requests.post(url, json=data)
response = requests.post(url, json=data)

# Check if the response contains content
if response.status_code == 200:
    try:
        print(response.json())  # Print the JSON response
    except ValueError:
        print("Response is not in JSON format")
        print(response.text)  # Print raw text to debug
else:
    print(f"Request failed with status code {response.status_code}")
import requests

url = "http://192.168.68.50:5001/image"
files = {"file": ("image_name.jpeg", open("image_path.jpeg", "rb"))}
response = requests.post(url, files=files)
response = requests.post(url, json=data)

# Check if the response contains content
if response.status_code == 200:
    try:
        print(response.json())  # Print the JSON response
    except ValueError:
        print("Response is not in JSON format")
        print(response.text)  # Print raw text to debug
else:
    print(f"Request failed with status code {response.status_code}")