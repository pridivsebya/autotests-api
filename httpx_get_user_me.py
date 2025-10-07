import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "mymail1@mail.ru",
    "password": "пароль123"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученный ответ и статус
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

# Если логин успешен, берем токен и делаем запрос к /users/me
if login_response.status_code == 200 and "token" in login_response_data and "accessToken" in login_response_data["token"]:
    access_token = login_response_data["token"]["accessToken"]
    headers = {"Authorization": f"Bearer {access_token}"}
    response_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
    print("User info response:", response_me.json())
    print("Status Code:", response_me.status_code)
else:
    print("Login failed, не удалось получить accessToken")


