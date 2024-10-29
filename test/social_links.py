import requests
import json

BASE_URL = 'http://localhost:3000/api/sociallinks'  # Adjust the URL if necessary

# Test Data
test_data = {
    "username": "developerTest",
    "github": "https://github.com/developerTest",
    "linkedin": "https://linkedin.com/in/developerTest",
    "x": "https://x.com/developerTest"
}

updated_data = {
    "github": "https://github.com/updatedDeveloperTest",
    "linkedin": "https://linkedin.com/in/updatedDeveloperTest"
}

# CREATE: Test POST /api/sociallinks
def create_social_link():
    response = requests.post(BASE_URL, json=test_data)
    if response.status_code == 201:
        print("Profile created successfully:", response.json())
    else:
        print("Failed to create profile:", response.text)

# READ: Test GET /api/sociallinks
def get_all_links():
    response = requests.get(BASE_URL)
    print("Response Status Code:", response.status_code)
    print("Raw Response Text:", response.text)  # Print raw response

    if response.status_code == 200:
        try:
            print("All Profiles:", response.json())
        except ValueError:
            print("Failed to parse JSON")
    else:
        print("Failed to fetch profiles:", response.text)

# READ: Test GET /api/sociallinks/:username
def get_links_by_username(username):
    response = requests.get(f"{BASE_URL}/{username}")
    if response.status_code == 200:
        print(f"Profile for {username}:", response.json())
    else:
        print(f"Failed to fetch profile for {username}:", response.text)

# UPDATE: Test PUT /api/sociallinks/:username
def update_social_link(username):
    response = requests.put(f"{BASE_URL}/{username}", json=updated_data)
    if response.status_code == 200:
        print(f"Profile for {username} updated:", response.json())
    else:
        print(f"Failed to update profile for {username}:", response.text)

# DELETE: Test DELETE /api/sociallinks/:username
def delete_social_link(username):
    response = requests.delete(f"{BASE_URL}/{username}")
    if response.status_code == 200:
        print(f"Profile for {username} deleted:", response.json())
    else:
        print(f"Failed to delete profile for {username}:", response.text)

# Test all operations
if __name__ == "__main__":
    print("Testing Create Operation:")
    create_social_link()

    print("\nTesting Get All Links:")
    get_all_links()

    print("\nTesting Get Profile by Username:")
    get_links_by_username("developerTest")

    print("\nTesting Update Operation:")
    update_social_link("developerTest")

    print("\nTesting Delete Operation:")
    delete_social_link("developerTest")

    print("\nTesting Get All Links after Deletion:")
    get_all_links()
