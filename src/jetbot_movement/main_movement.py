from jetbot import Robot
import time
import socket
from jetbot_movement import jetbot_movement
import sys


def get_val_by_thread(s):
    return s.recv(1024).decode()


def get_settings():
    port = 6666
    host = socket.gethostbyname(socket.gethostname())
    host = "192.168.0.185"
    print(host)
    return ((host, int(port)))


if __name__ == '__main__':
    Jetbot = jetbot_movement()
    settings = get_settings()
    s = socket.socket()
    try:
        print(settings)
        s.connect(settings)
    except Exception as ex:
        print(f'Steve Huis said: {ex}')
        sys.exit()

    while True:
        try:
            move = get_val_by_thread(s)
            print(f'move: {move}')
            move = list(map(lambda x: float(x), move.split(' ')))
            Jetbot.make_move(move[0], move[1])
        except:
            Jetbot.make_move(0, 0)
            print("I am dead")