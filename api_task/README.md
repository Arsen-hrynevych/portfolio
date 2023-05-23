### Prerequisites

To run the API, ensure that you have the following:

- Python installed (version 3.7 or above)
- The necessary Python packages installed. You can install them by executing the following command:

  ```
  pip3 install fastapi uvicorn pyairtable
  ```

### Configuration

This API relies on environment variables to store sensitive information. Set the following environment variables before running the API:

- `auth_token`: Your Airtable authentication token.
- `base_id`: The ID of your Airtable base.
- `table_name`: The name of the table in your Airtable base.

### Running the API

1. Clone the repository or download the code files.

2. Navigate to the project directory in your terminal.

3. Execute the following command to start the API:

   ```
   uvicorn main:app --reload
   ```

   The API will start running at `http://localhost:5000`.

### API Endpoints

#### Get Users

- **URL:** `/users`
- **Method:** GET
- **Description:** Retrieves a list of users.
- **Response:** JSON object containing the list of users.

#### Get User

- **URL:** `/users/{id}`
- **Method:** GET
- **Description:** Retrieves a specific user based on their ID.
- **Response:** JSON object containing the user information.

#### Add User

- **URL:** `/users`
- **Method:** POST
- **Description:** Adds a new user.
- **Request Body:** JSON object containing the user's name, email, and status.
- **Response:** JSON object containing the newly created user.

#### Update User

- **URL:** `/users/{id}`
- **Method:** PUT
- **Description:** Updates an existing user based on their ID.
- **Response:** No response body.

#### Remove User

- **URL:** `/users/{id}`
- **Method:** DELETE
- **Description:** Deletes a user based on their ID.
- **Response:** No response body.