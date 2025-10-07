import httpx

from tools.fakers import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
user_id = create_user_response_data["user"]["id"]

print('Create user data:', create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
access_token = login_response_data["token"]["accessToken"]

print('Login data:', login_response_data)

# Обновляем данные пользователя
patch_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
headers = {"Authorization": f"Bearer {access_token}"}
patch_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{user_id}", json=patch_payload, headers=headers)
patch_user_response_data = patch_user_response.json()

print('Update user data:', patch_user_response_data)
