import socket

HOST = '127.0.0.1'
PORT = 48049
ENCODING = "utf-8"
FRAME = 64
OPEN_FILE = 'test_send.csv'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((HOST, PORT))
    file = open(OPEN_FILE, "r")
    data = file.read(FRAME)
    while data:
        c.send(data.encode(ENCODING))
        data = file.read(FRAME)
    c.close()
    file.close()
