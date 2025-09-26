import socket

def send_message(message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    client.send(message.encode())
    response = client.recv(1024).decode()
    client.close()
    return response

def main():
    # Первое сообщение
    message1 = "Привет, сервер!"
    response1 = send_message(message1)
    print("Ответ на первое сообщение:")
    print(response1)

    # Второе сообщение в новом соединении
    message2 = "Как дела?"
    response2 = send_message(message2)
    print("Ответ на второе сообщение:")
    print(response2)

if __name__ == "__main__":
    main()
