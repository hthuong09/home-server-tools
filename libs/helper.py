import urequests as requests
import socket
import machine
import utime


def get_ip():
    res = requests.get('http://ipv4.icanhazip.com/')
    return res if res is None else res.text.strip()


def check_port_open(ip, port):
    s = socket.socket()
    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False


def led_blink(time):
    pin = machine.Pin(2, machine.Pin.OUT)
    while time > 0:
        pin.value(0);
        utime.sleep_ms(200)
        pin.value(1)
        utime.sleep_ms(500)
        time = time - 1
