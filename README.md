# Utilities for Home Server
Poor man's tools for home server.

## Uses

This tools will help you:
- Detect if server is offline and send magic packet to wake up server
- Detect if public IP changed, update DNS record using cloudflare API
- Logging and notification using Pushbullet API

## Installation
This tool requires an ESP8266 board [flashed Micropython firmware](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html).

For me, I'm using NodeMCU board, like 6$.

Next, update `config.py` with correct information

In case you can not connect WiFi, you might want to open `libs/wifi.py` and change that static IP configuration

```
self.sta_if.ifconfig(('192.168.1.19', '255.255.255.0', '192.168.1.1', '8.8.8.8'))
```

You can flash code using various programs like [ESPlorer](https://esp8266.ru/esplorer/), Pycharm with Micropython plugin.

## References
Learn more about micropython
- https://docs.micropython.org/en/latest/esp8266/index.html