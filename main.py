from libs.cloudflare import CloudFlare
from libs.pushbullet import PushBullet
from libs.helper import *
from libs.wifi import WiFiHelper
from libs.wol import send_magic_packet
import utime
import config


pushpullet = PushBullet(config.PUSHPULLET_API_KEY)


def main():
    # Blink led
    led_blink(5)

    # Connect to WiFi
    wifi = WiFiHelper(config.WIFI_SSID, config.WIFI_PASS)
    wifi.verify_and_connect()

    # Ping server IP, if there is no response, send WOL package and notify PushBullet
    wake_up_server()

    # Check for IP change and update DNS
    update_dns()


def wake_up_server():
    # Ping server
    is_online = check_port_open(config.SERVER_IP, 22)

    # Send magic package if ping failed
    if is_online is False:
        send_magic_packet(config.SERVER_GATEWAY, config.SERVER_MAC_ADDRESS)
        pushpullet.push(
            'note',
            config.PUSHPULLET_NOTIFICATION_TITLE,
            'Server {} is offline. Sending Magic Packet'.format(config.SERVER_IP),
            config.PUSHPULLET_CHANNEL
        )
    else:
        print('Server is online')


def update_dns():
    cloudflare = CloudFlare(config.CLOUDFLARE_API_KEY, config.CLOUDFLARE_ACCOUNT_EMAIL)
    my_ip = get_ip()
    for _config in config.CLOUDFLARE_CONFIG:
        zone_identifier = cloudflare.get_zone_identifier(_config['domain'])
        for record_name in _config['records']:
            record_identifier = cloudflare.get_record_identifier(zone_identifier, record_name)
            if my_ip == record_identifier['ip']:
                # No changes, do nothing
                continue
            status = cloudflare.update_dns_record(zone_identifier, record_identifier['id'], record_name, my_ip)
            if status is True:
                pushpullet.push(
                    'note',
                    config.PUSHPULLET_NOTIFICATION_TITLE,
                    'Update record of {} to IP: {}'.format(record_name, my_ip),
                    config.PUSHPULLET_CHANNEL
                )
            else:
                pushpullet.push(
                    'note',
                    config.PUSHPULLET_NOTIFICATION_TITLE,
                    'IP is changed to {}, but failed to update for record {}.'.format(my_ip, record_name),
                    config.PUSHPULLET_CHANNEL
                )


while True:
    try:
        main()
    except Exception as e:
        print(str(e))
    utime.sleep(config.LOOP_WAIT)

