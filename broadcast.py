import socket
import threading
from tinydb import TinyDB, Query
import json
from ipm import get_wifi_ip_address
{"ser":1}
# Broadcast i      in kullan      lacak IP adresi ve port numaras
BROADCAST_IP = '192.168.1.255'  #    ^vrnek bir yay      n IP adresi
BROADCAST_PORT = 6007  #    ^vrnek bir yay      n port numaras
ip = get_wifi_ip_address()
db = TinyDB ("res.json")

print(ip)
def receive_broadcast():
    # Broadcast soketi olu   ^=turma
    recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    recv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    recv_socket.bind((BROADCAST_IP, BROADCAST_PORT))

    while True:
        data, addr = recv_socket.recvfrom(1024)
        decoded_data = data.decode()

        json_data = json.loads(decoded_data)
        if ip != addr[0]:

            db.insert(json_data)
            print("Alınan veri:", json_data)
        # Gelen JSON verisine g      re bir i   ^=lem yapabilirsiniz

def send_broadcast(param):
    # Broadcast soketi olu   ^=turma
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
         
       # json_data = json.dumps(message)
    send_socket.sendto(param.encode(), (BROADCAST_IP, BROADCAST_PORT))
# Veri alma i   ^=lemini ba   ^=latma
receive_thread = threading.Thread(target=receive_broadcast)
receive_thread.start()


