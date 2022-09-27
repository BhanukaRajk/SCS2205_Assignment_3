# SCS2205 Computer Networks I
# Take Home Assignment 3

# Name: P. D. P. B. Y. Rajakaruna
# Index Number: 20001411

# import socket module
import socket

# Creating socket
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET - Socket domain (AF_INET for IPv4, AF_INET6 for IPv6)
# AF_STREAM - Socket type

# Display the message socket created
print("Server socket successfully created")

# reserving port
Port = 2728;

# Hosting server - localhost
Host = '127.0.0.1'

# Get local machine name
# host = socket.gethostname()

# binding address (hostname and port number) to the socket
SOCKET.bind((Host, Port))

# display message about the binding process
print("%s and hostname binded to the socket" % (Port))

# Start server(local) and wait for the request for client connection
# 5 is the number of unaccepted connections that the system will allow before binding the new connections
# maximum 3 requests allowed before binding the new connections
SOCKET.listen(5)


print("Now Socket is listening") 



while True:
    
    # establish the connection with client
    connection, address = SOCKET.accept()
    print('Got connection from', str(address))

    request = connection.recv(1024).decode('utf-8') 


    header = request.split(' ')
    
    try:
        currentPath = header[1]
    except IndexError:
        currentPath = '/'
    
    print("Current Path :" + currentPath)

    if currentPath == '/' : 
        currentPath = './htdocs/index.html'
        print("Connected to index.html") 
        

    elif currentPath == '/me/contact' or currentPath == '/me/contact.html':
        currentPath = './htdocs/me/contact.html'
        print("Connected to contact.html") 
        
    try:
        file = open(currentPath)
        fileContent = file.read()
        file.close()

        response = 'HTTP/1.x 200 OK\n\n' + fileContent
        
        
    except:
        response = 'HTTP/1.x 404 Not Found\n\n404 Page Not Found :('
        print("404 Page Not Found")
    
    connection.sendall(response.encode())
    connection.close()

# close the socket
SOCKET.close()