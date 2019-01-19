import socket
import threading
import time
from easytello.stats import Stats

class Tello:
    def __init__(self, tello_ip: str='192.168.10.1', debug: bool=True):
        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))

        self.tello_ip = tello_ip
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
    
    def wait(self, delay: float):
        if self.debug is True:
            print('Waiting {} seconds...'.format(delay))
        self.log.append(Stats('wait', len(self.log)))
        time.sleep(delay)
    
    def get_log(self):
        return self.log

    # Controll Commands
    def command(self):
        self.send_command('command')
    
    def takeoff(self):
        self.send_command('takeoff')

    def land(self):
        self.send_command('land')

    def streamon(self):
        self.send_command('streamon')

    def streamoff(self):
        self.send_command('streamoff')

    def emergency(self):
        self.send_command('emergency')
    
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

    def cw(self, degr: int):
        self.send_command('cw {}'.format(degr))
    
    def ccw(self, degr: int):
        self.send_command('ccw {}'.format(degr))

    def flip(self, direc: str):
        self.send_command('flip {}'.format(direc))

    def go(self, x: int, y: int, z: int, speed: int):
        self.send_command('go {} {} {} {}'.format(x, y, z, speed))

    def curve(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, speed: int):
        self.send_command('curve {} {} {} {} {} {} {}'.format(x1, y1, z1, x2, y2, z2, speed))

    # Set Commands
    def set_speed(self, speed: int):
        self.send_command('speed {}'.format(speed))

    def rc_control(self, a: int, b: int, c: int, d: int):
        self.send_command('rc {} {} {} {}'.format(a, b, c, d))

    def set_wifi(self, ssid: str, passwrd: str):
        self.send_command('wifi {} {}'.format(ssid, passwrd))

    # Read Commands
    def get_speed(self):
        self.send_command('speed?', True)
        return self.log[-1].get_response()

    def get_battery(self):
        self.send_command('battery?', True)
        return self.log[-1].get_response()

    def get_time(self):
        self.send_command('time', True)
        return self.log[-1].get_response()

    def get_height(self):
        self.send_command('height?', True)
        return self.log[-1].get_response()
    
    def get_temp(self):
        self.send_command('temp?', True)
        return self.log[-1].get_response()

    def get_attitude(self):
        self.send_command('attitude?', True)
        return self.log[-1].get_response()

    def get_baro(self):
        self.send_command('baro?', True)
        return self.log[-1].get_response()

    def get_acceleration(self):
        self.send_command('acceleration?', True)
        return self.log[-1].get_response()
    
    def get_tof(self):
        self.send_command('tof?', True)
        return self.log[-1].get_response()

    def get_wifi(self):
        self.send_command('wifi?', True)
        return self.log[-1].get_response()
    
