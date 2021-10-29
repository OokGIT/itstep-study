import socket

HOST = '127.0.0.1'
PORT = 48049
ENCODING = "utf-8"
FRAME = 64
SAVE_FILE = 'new_file.csv'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, address = s.accept()
    file = open(SAVE_FILE, "w")
    data = conn.recv(FRAME).decode(ENCODING)
    while data:
        file.write(data)
        data = conn.recv(FRAME).decode(ENCODING)
    file.close()
    conn.close()
