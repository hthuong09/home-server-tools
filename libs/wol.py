import usocket as socket
import ustruct as struct


def wakeonlan(ip, macaddress):
    try:
        send_magic_packet(ip, macaddress)
    except:
        print('Failed to send magic package')


def send_magic_packet(ip, macaddress):
    if len(macaddress) == 12:
        pass
    elif len(macaddress) == 17:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, '')
    else:
        raise ValueError('Incorrect MAC address format')

    # Pad the synchronization stream
    data = b'FFFFFFFFFFFF' + (macaddress * 16).encode()
    send_data = b''

    # Split up the hex values in pack
    for i in range(0, len(data), 2):
        send_data += struct.pack(b'B', int(data[i: i + 2], 16))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((ip, 9))
    sock.send(send_data)
    sock.close()