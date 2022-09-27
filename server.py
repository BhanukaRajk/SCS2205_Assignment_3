#----------------------------------#
# SCS2205 Computer Networks I
# Take Home Assignment 3
#----------------------------------#

#----------------------------------#
# Name: P. D. P. B. Y. Rajakaruna
# Index Number: 20001411
#----------------------------------#

#----------------------------------#
# web server: This PC
# Client: Web browser
#----------------------------------#


# import socket module and sys module
import socket
import sys

# Creating the socket
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET - Socket domain (AF_INET corresponds for IPv4, AF_INET6 corresponds for IPv6)
# AF_STREAM - Socket type (TCP)

# Display the message socket created
print("Server socket successfully created")

# reserving a port
Port = 2728

# Hosting server address - localhost
Localhost = "127.0.0.1"

# Get local machine name
# host = socket.gethostname()



# Try to bind address (hostname and port number) to the socket
try:
    SOCKET.bind((Localhost, Port))

except socket.error as msg:
    # Display error message and exit
    print("# Binding failed!")
    sys.exit(1)



# display message about the binding process
print(Port, "(Port) and",  Localhost, "(Hostname) binded to the socket")

# Start server(local) and wait for the request for client connection
# SOCKET.listen(number of clients can interact) - 6th client will be dropped
SOCKET.listen(5)
print("Socket is listening for a request") 



# The loop stops only if we interrupt it or an error occurs
while True:
    
    # Establish the connection
    # accept() returns two objects; socket-client object and the address.
    connection, address = SOCKET.accept()

    # Display the Localhost address and the port
    print("Got connection from", address)

    # Maximum data packet size is 1024 bytes. Others not acceptable
    request = connection.recv(1024).decode("utf-8") 

    # Get the browser url
    try:
        FilePath = request.split(" ")[1]

    except IndexError:
        response = "HTTP/1.1 400 Bad Request :("
        #FilePath = "/"
    
    # Print the path of current file
    print("Current Path :" + FilePath)



    # If the client requests index.html page, send it to the client
    if FilePath == "/" : 
        FilePath = "./htdocs/index.html"

        # Indicate that the file has been sent
        print("Connected to index.html") 
        
    # If the client requests contact.html page, send it to the client
    elif FilePath == "/me/contact" or FilePath == "/me/contact.html":
        FilePath = "./htdocs/me/contact.html"

        # Indicate that the file has been sent
        print("Connected to contact.html") 
        


    try:
        # Trying to open the file in requested path
        File = open(FilePath)

        # Reading the content of file
        Content = File.read()

        # Closing the file
        File.close()

        # Provide response with the contents of the file
        response = "HTTP/1.1 200 OK\n\n" + Content
        
    # If the file/page not founded in requested path
    except:
        # Provide the page not found 404 error
        response = "HTTP/1.1 404 Not Found\n\n404 Page Not Found :("

        # Display the error message via console
        print("404 Page Not Found")
    


    # send the encoded(by utf-8) response to the client
    connection.sendall(response.encode())

    # Closing the connection betweeen server and client
    connection.close()

# closing socket
SOCKET.close()