import socket
import threading

messages = []  # Глобальный список сообщений

def handle_client(client_socket, addr):
    print(f"Пользователь с адресом: {addr} подключился к серверу")
    try:
        data = client_socket.recv(1024).decode().strip()
        if data:
            print(f"Пользователь с адресом: {addr} отправил сообщение: {data}")
            messages.append(data)
            client_socket.send('\n'.join(messages).encode())
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(10)
    print("TCP сервер запущен на localhost:12345")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    main()

