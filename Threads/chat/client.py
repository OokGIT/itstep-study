import socket
import threading
import config
nickname = input("Введите совё имя: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((config.HOST, config.PORT))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'send_nick':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except():
            print("Error!")
            client.close()
            break


def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
