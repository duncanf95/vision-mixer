import socket
import sqlite3
import time
import datetime
import random
import pyautogui

conn = sqlite3.connect('real_test.db')
cur = conn.cursor()


def Main():
    host = ''
    port = 5000
    input_type = ''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))


    s.listen(1)
    c, addr = s.accept()
    print("connection from: "+str(addr))
    while True:
        data = c.recv(1024)

        if not data:
            break

        print("from connected user: "+data.decode('utf-8'))
        print("sending: " + data.decode('utf-8'))
        #input_type = Get_Type(data.decode('utf-8'))


        c.sendall(data)

    c.close
    cur.close()
    conn.close()


def Get_Type(ID):
    cur.execute('SELECT Type FROM Inputs WHERE ID = ?', ID)
    data = cur.fetchone()
    return data[0]


def Press(ID):
    Key = Get_Key(ID)
    #time.sleep(4)
    pyautogui.keyDown(self.function)
    time.sleep(1)
    pyautogui.keyUp(self.function)


def Get_Key(ID):
    cur.execute('SELECT Input_Data FROM Inputs WHERE ID = ?', ID)
    data = cur.fetchone()
    return data[0]


if __name__ == '__main__':
    Main()
