import socket

#conexao da rede 
host = ''

#porta onde o servidor irá escutar
port = 1234

#criar o socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Associar os socket a uma porta
s.bind((host, port))

while True:
    print('waiting to receive message')
    data, adress = s.recvfrom(1024)
    
    print('received: ' + data.decode() + '\nfrom:' + str(adress[0]) + '\nlistening on port: ' + str(adress[1]))