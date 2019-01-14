import socket
import threading
import time
from stats import Stats

class Tello:
    def __init__(self, debug=True):
        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))

        self.tello_ip = '192.168.10.1'
        self.tello_port = 8889
        self.tello_address = (self.tello_ip, self.tello_port)
        self.log = []

        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.MAX_TIME_OUT = 15.0
        self.debug = debug
        self.command()

    def send_command(self, command: str, query: bool =False):
        self.log.append(Stats(command, len(self.log)))

        self.socket.sendto(command.encode('utf-8'), self.tello_address)
        if self.debug is True:
            print('Sending command: {}'.format(command))

        start = time.time()
        while not self.log[-1].got_response():
            now = time.time()
            difference = now - start
            if difference > self.MAX_TIME_OUT:
                print('Connection timed out!')
                break
        if self.debug is True and query is False:
            print('Response: {}'.format(self.log[-1].get_response()))

    def _receive_thread(self):
        while True:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                self.log[-1].add_response(self.response)
            except socket.error as exc:
                print('Socket error: {}'.format(exc))
    
    def get_log(self):
        return self.log

    def command(self):
        self.send_command('command')
    
    def takeoff(self):
        self.send_command('takeoff')

    def land(self):
        self.send_command('land')

    def wait(self, delay: float):
        if self.debug is True:
            print('Waiting {} seconds...'.format(delay))
        self.log.append(Stats('wait', len(self.log)))
        time.sleep(delay)
    
    def up(self, dist: int):
        self.send_command('up {}'.format(dist))

    def down(self, dist: int):
        self.send_command('down {}'.format(dist))

    def left(self, dist: int):
        self.send_command('left {}'.format(dist))

    def right(self, dist: int):
        self.send_command('right {}'.format(dist))
        
    def forward(self, dist: int):
        self.send_command('forward {}'.format(dist))

    def back(self, dist: int):
        self.send_command('back {}'.format(dist))

    def rotate(self, degr: int):
        if degr <= 0:
            self.send_command('cw {}'.format(degr))
        else:
            degr = -1 * degr
            self.send_command('ccw {}'.format(degr))

    def flip(self, direc: str):
        self.send_command('flip {}'.format(direc))

    def set_speed(self, speed: int):
        self.send_command('speed {}'.format(speed))

    def get_speed(self):
        self.send_command('Speed?', True)
        return self.log[-1].get_response()

    def get_battery(self):
        self.send_command('Battery?', True)
        return self.log[-1].get_response()

    def get_time(self):
        self.send_command('Time', True)
        return self.log[-1].get_response()
    
