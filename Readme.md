# API Documentation

## **Base URL**: `/api`

---

### 1\. **Authentication API**

#### **POST /auth/signup**

**Description**: Register a new user.

**Request Body**:

json

Copy code

```json
{   "username": "string",   "password": "string" }
```

**Response**:

- **201 Created**: User successfully registered.
    
    ```json
    {   "message": "User registered successfully",   "accessToken": "string",   "refreshToken": "string" }
    ```
    
- **400 Bad Request**: Username already exists.
    
    ```json
    {   "message": "Username already exists" }
    ```
    
- **500 Internal Server Error**: Server error.
    
    ```json
    {   "message": "Internal server error" }
    ```
    

---

#### **POST /auth/login**

**Description**: Log in a user.

**Request Body**:

json

Copy code

```json
{   "username": "string",   "password": "string" }
```

**Response**:

- **200 OK**: Successful login, returns `accessToken` and `refreshToken`.
    
    ```json
    {   "accessToken": "string",   "refreshToken": "string" }
    ```
    
- **400 Bad Request**: Invalid username or password.
    
    ```json
    {   "message": "Invalid username or password" }
    ```
    
- **500 Internal Server Error**: Server error.
    
    ```json
    {   "message": "Internal server error" }
    ```
    

---

#### **POST /auth/token/refresh**

**Description**: Refresh the access token using a refresh token.

**Request Body**:

json

Copy code

```json
{   "refreshToken": "string" }
```

**Response**:

- **200 OK**: Returns a new `accessToken`.
    
    ```json
    {   "accessToken": "string" }
    ```
    
- **403 Forbidden**: Invalid or missing refresh token.
    
    ```json
    {   "message": "Invalid refresh token" }
    ```
    

---

### 2\. **Social Media API**

#### **POST /sociallinks**

**Description**: Create a new social media profile link.

**Request Body**:

json

Copy code

```json
{   "username": "string",   "github": "string",   "x": "string",  // Formerly Twitter   "telegram": "string",   "linkedin": "string",   "wallet": "string" }
```

**Response**:

- **201 Created**: Profile created successfully.
    
    ```json
    {   "username": "string",   "github": "string",   "x": "string",   "telegram": "string",   "linkedin": "string",   "wallet": "string" }
    ```
    
- **400 Bad Request**: Invalid data.
    
    ```json
    {   "message": "Error message" }
    ```
    

---

#### **GET /sociallinks**

**Description**: Retrieve all social media profiles.

**Response**:

- **200 OK**: List of all profiles.
    
    `[   {     "username": "string",     "github": "string",     "x": "string",     "telegram": "string",     "linkedin": "string",     "wallet": "string"   } ]`
    
- **500 Internal Server Error**: Server error.
    
    ```json
    {   "message": "Error message" }
    ```
    

---

#### **GET /sociallinks/

**Description**: Retrieve a social media profile by username.

**Response**:

- **200 OK**: Profile found.
    
    ```json
    {   "username": "string",   "github": "string",   "x": "string",   "telegram": "string",   "linkedin": "string",   "wallet": "string" }
    ```
    
- **404 Not Found**: Profile not found.
    
    ```json
    {   "message": "Profile not found" }
    ```
    
- **500 Internal Server Error**: Server error.
    
    ```json
    {   "message": "Error message" }
    ```
    

---

#### **DELETE /sociallinks/

**Description**: Delete a social media profile by username.

**Response**:

- **200 OK**: Profile deleted successfully.
    
    ```json
    {   "message": "Profile deleted successfully" }
    ```
    
- **404 Not Found**: Profile not found.
    
    ```json
    {   "message": "Profile not found" }
    ```
    
- **500 Internal Server Error**: Server error.
    
    ```json
    {   "message": "Error message" }
    ```
    

---

#### **PUT /sociallinks/

**Description**: Update a social media profile by username.

**Request Body**:

json

Copy code

```json
{   "github": "string",   "x": "string",   "telegram": "string",   "linkedin": "string",   "wallet": "string" }
```

**Response**:

- **200 OK**: Profile updated successfully.
    
    ```json
    {   "username": "string",   "github": "string",   "x": "string",   "telegram": "string",   "linkedin": "string",   "wallet": "string" }
    ```
    
- **404 Not Found**: Profile not found.
    
    ```json
    {   "message": "Profile not found" }
    ```
    
- **500 Internal Server Error**: Server error.
    
    ```json
    {   "message": "Error message" }
    ```
    

---

### 3\. **User Photo API**

#### **POST /userphoto/upload**

**Description**: Upload a user photo along with `username_1` and `username_2`.

**Request**:

- Multipart/form-data (Image upload):
    - `photo`: File (required)
    - `username_1`: string (required)
    - `username_2`: string (required)

**Response**:

- **201 Created**: User and photo uploaded successfully.
    
    ```json
    {   "message": "User and photo saved successfully",   "data": {     "username_1": "string",     "username_2": "string",     "photoId": "ObjectId"   } }
    ```
    
- **400 Bad Request**: Duplicate combination of `username_1` and `username_2`.
    
    ```json
    {   "message": "This combination of usernames already exists." }
    ```
    
- **500 Internal Server Error**: Server error.
    
    ```json
    {   "message": "Failed to upload photo and save user" }
    ```
    

---

#### **GET /userphoto/

**Description**: Retrieve a photo by `username_1`.

**Response**:

- **200 OK**: Streams the photo.
- **404 Not Found**: User or photo not found.
    
    ```json
    {   "message": "User not found" }
    ```
    
- **500 Internal Server Error**: Server error.
    
    ```json
    {   "message": "Error retrieving user and photo" }
    ```
    

---

#### **GET /userphoto/connections/

**Description**: Retrieve all connections for a given username.

**Response**:

- **200 OK**: List of connections where `username` is either `username_1` or `username_2`.
    
    ```json
    {   "connections": [     {       "username_1": "string",       "username_2": "string"     }   ] }
    ```
    
- **404 Not Found**: No connections found for the given username.
    
    ```json
    {   "message": "No connections found for this username" }
    ```
    
- **500 Internal Server Error**: Server error.
    
    ```json
    {   "message": "Error retrieving connections" }
    ```
    

---

#### **GET /userphoto/photo/

/

**Description**: Retrieve a photo by both `username_1` and `username_2`.

**Response**:

- **200 OK**: Streams the photo if it exists for the given combination of `username_1` and `username_2`.
- **404 Not Found**: No record found for the given usernames.
    
    ```json
    {   "message": "No record found for the given usernames." }
    ```
    
- **500 Internal Server Error**: Server error.
    
    ```json
    {   "message": "Error retrieving photo" }
    ```
