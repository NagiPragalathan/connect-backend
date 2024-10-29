import requests

BASE_URL = 'http://localhost:3000/api/userphoto'

image_path = r"C:\Users\Admin\Downloads\OIP.jpeg"

def upload_user_photo(image_path, username_1, username_2):
    url = f'{BASE_URL}/upload'
    
    files = {'photo': open(image_path, 'rb')}
    data = {
        'username_1': username_1,
        'username_2': username_2
    }

    response = requests.post(url, files=files, data=data)

    if response.status_code == 201:
        print("Upload Successful:", response.json())
    else:
        print("Upload Failed:", response.text)


def get_user_photo_by_username_1(username_1):
    url = f'{BASE_URL}/{username_1}'

    response = requests.get(url)

    if response.status_code == 200:
        filename = f'{username_1}_photo.jpg'
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Photo retrieved and saved as {filename}")
    else:
        print("Failed to retrieve photo:", response.text)


def get_connections_by_username(username):
    url = f'{BASE_URL}/connections/{username}'

    response = requests.get(url)

    if response.status_code == 200:
        connections = response.json().get('connections')
        print(connections)
        print(f"Connections for {username}:")
        for conn in connections:
            print(f"{conn['username_1']} is connected with {conn['username_2']}")
    else:
        print("Failed to retrieve connections:", response.text)


if __name__ == "__main__":
    print("Testing Upload User Photo:")
    upload_user_photo(image_path, 'usertest2', 'usertest1')

    print("\nTesting Retrieve User Photo by Username_1:")
    get_user_photo_by_username_1('usertest2')

    print("\nTesting Retrieve Connections by Username:")
    get_connections_by_username('usertest2')
