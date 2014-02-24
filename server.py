'''
developed by
George Macrae 2014

'''


from socket import *
import threading
import sys

def handler(clientsocket, clientaddr):

    while 1:
        data = '' 
        data = clientsocket.recv(1024)

        datal = data.split(':')
        if datal[3] != 'move':
            print data
        if datal[2] == 'p1':        
            p2_socket.send(data)
        else:
            p1_socket.send(data)

        
 
if __name__ == "__main__":
 
    host = gethostbyname(gethostname())
    
    port = 9999
    addr = (host, port)
 
    print host
    serversocket = socket(AF_INET, SOCK_STREAM)
 
    serversocket.bind(addr)
    print "Server is listening for matchup_sockets\n"

    serversocket.listen(2)
    

    global p1_socket
    global p2_socket
    p1_socket = ''
    p2_socket = ''
    
    i = 0;
    while i<2:
        
        clientsocket, clientaddr = serversocket.accept()
        if not p1_socket :
            p1_socket = clientsocket
            # p1_socket.send("p1")
            print str(p1_socket)
        else:
            p2_socket = clientsocket
            p2_socket.send("p2")
            p1_socket.send("p1")
            
            print str(p2_socket)

        h_thread = threading.Thread(target = handler, args = (clientsocket, clientaddr))
        h_thread.start()
        i = i+1