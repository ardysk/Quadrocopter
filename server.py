import socket

# Konfiguracja serwera
server_ip = '0.0.0.0'
server_port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"Serwer uruchomiony na {server_ip}:{server_port}")
print("Oczekiwanie na połączenie...")

conn, addr = server_socket.accept()
print(f"Połączono z: {addr}")

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        command = data.decode('utf-8')
        print(f"Otrzymano komendę: {command}")
except KeyboardInterrupt:
    print("Zamykanie serwera...")
finally:
    conn.close()
    server_socket.close()
