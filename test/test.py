import requests

BASE_URL = 'http://localhost:3000/api/auth'  # Base URL for authentication endpoints
PROTECTED_URL = 'http://localhost:3000/api/protected'  # URL for protected route

# Test Sign-up
def test_signup(username, password):
    url = f"{BASE_URL}/signup"
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(url, json=payload)
    if response.status_code == 201:
        print(f"Sign-up successful: {response.json()}")
        return response.json()  # Returns both accessToken and refreshToken
    else:
        print(f"Sign-up failed: {response.status_code} {response.text}")
        return None

# Test Login
def test_login(username, password):
    url = f"{BASE_URL}/login"
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print(f"Login successful: {response.json()}")
        return response.json()  # Returns both accessToken and refreshToken
    else:
        print(f"Login failed: {response.status_code} {response.text}")
        return None

# Test Protected Route
def test_protected_route(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(PROTECTED_URL, headers=headers)
    if response.status_code == 200:
        print(f"Protected route accessed: {response.json()}")
    else:
        print(f"Access to protected route failed: {response.status_code} {response.text}")

# Test Token Refresh
def test_refresh_token(refresh_token):
    url = f"{BASE_URL}/token/refresh"
    payload = {
        "refreshToken": refresh_token
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print(f"Token refreshed successfully: {response.json()}")
        return response.json()['accessToken']  # Returns new access token
    else:
        print(f"Token refresh failed: {response.status_code} {response.text}")
        return None

if __name__ == "__main__":
    # Replace with desired username and password
    username = "john_doe1"
    password = "password123"

    print("1. Sign-up Test")
    signup_response = test_signup(username, password)
    if signup_response:
        access_token = signup_response['accessToken']
        refresh_token = signup_response['refreshToken']

        print("\n2. Protected Route Test with Access Token")
        test_protected_route(access_token)

        print("\n3. Refresh Token Test")
        new_access_token = test_refresh_token(refresh_token)

        if new_access_token:
            print("\n4. Protected Route Test with New Access Token")
            test_protected_route(new_access_token)
    else:
        print("\nSign-up failed. Skipping further tests.")
