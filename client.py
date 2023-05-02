import socket


# Endereço destino
host = 'localhost'

# Porta destino
port = 1234

# Criando os socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('CTRL+X to exit \n')
msg = input()

while msg != '|x18':
    # enviar os dados
    s.sendto(msg.encode(), (host, port))
    msg = input()
    
print('Closing socket')
s.close()