import network


class WiFiHelper:
    def __init__(self, ssid, password):
        self.MAX_RETRIES = 5
        self.sta_if = network.WLAN(network.STA_IF)
        self.ssid = ssid
        self.password = password

    # Connect to wifi using give ssid and password
    def connect(self):
        self.sta_if.active(True)
        self.sta_if.ifconfig(('192.168.1.19', '255.255.255.0', '192.168.1.1', '8.8.8.8'))
        self.sta_if.connect(self.ssid, self.password)
        print(self.sta_if.ifconfig())

    # Verify if we connect internet yet
    def verify_connection(self):
        return self.sta_if.isconnected()

    # Verify and connect to internet if we haven't connected yet
    def verify_and_connect(self):
        if self.verify_connection():
            return True

        self.connect()

    def get_ifconfig(self):
        return self.sta_if.ifconfig()

    def disconnect(self):
        self.sta_if.disconnect()

