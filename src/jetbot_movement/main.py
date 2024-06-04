from jetbot import Robot
import time
import socket
from jetbot_movement import jetbot_movement

def get_val_by_thread(s):
    print(s.recv(1024).decode())

def get_settings():
    port = 6666
    host = socket.gethostbyname(socket.gethostname())
    host = '127.0.1.1'
    print(host)
    return ((host, int(port)))
    
if __name__ == '__main__':
    settings = get_settings()
    s = socket.socket()
    try:
        print(settings)
        s.connect(settings)
    except Exception:
        print(f'Steve Huis said: {ex}')
        pass
    finally:
        print('Fuck u')
        exit()

        Jetbot = jetbot_movement() 

    while True:
        move = get_val_by_thread(s)
        move = list(map(lambda x: float(x), move.split()))
        Jetbot.make_move(move[0], move[1])
