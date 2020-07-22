import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print("server will start on host:", socket.gethostbyname(host))

port = 4000

s.bind((host,port))
s.listen()
addresses = {}
#print(host)
print("Server is ready...")
serverRunning = True
def handle_client(conn):
    try:
        welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % data
        conn.send(bytes(welcome, "utf8"))
        msg = "%s has joined the chat" % data
        broadcast(bytes(msg, "utf8"))
        clients[conn] = data
        while True:
            found = False
            response = 'Number of People Online\n'
            msg1 = conn.recv(1024) 

            if msg1 != bytes("{quit}", "utf8"):
                broadcast(msg1, data+": ")
            else:
                conn.send(bytes("{quit}", "utf8"))
                conn.close()
                del clients[conn]
                broadcast(bytes("%s has left the chat." % data, "utf8"))
                break
    except:
        print("%s has left the chat." % data)
def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


while True:
    conn,addr = s.accept()
    conn.send("Enter username: ".encode("utf8"))
    print("%s:%s has connected." % addr)
    addresses[conn] = addr
    threading.Thread(target = handle_client, args = (conn,)).start()
