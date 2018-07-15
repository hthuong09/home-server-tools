# CONFIGURATIONS

# PushPullet
PUSHPULLET_API_KEY = ''
PUSHPULLET_CHANNEL = 'server-notification'
PUSHPULLET_NOTIFICATION_TITLE = 'System Monitor [NodeMCU]'

# Cloudflare
CLOUDFLARE_API_KEY = ''
CLOUDFLARE_ACCOUNT_EMAIL = ''
CLOUDFLARE_CONFIG = [
    {
        'domain': 'example.me',
        'records': [
            'sub1.example.me',
            'sub2.example.me'
        ]
    }
]

# Wifi Connection
WIFI_SSID = ''
WIFI_PASS = ''

# Time wait each loop
LOOP_WAIT = 600  # 10 minutes

# Server Info
SERVER_IP = ''
SERVER_GATEWAY = ''
SERVER_MAC_ADDRESS = ''
