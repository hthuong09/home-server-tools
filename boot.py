import config
from libs.pushbullet import PushBullet

pushpullet = PushBullet(config.PUSHPULLET_API_KEY)
pushpullet.push(
    'note',
    config.PUSHPULLET_NOTIFICATION_TITLE,
    'System Starting... Start monitoring...',
    config.PUSHPULLET_CHANNEL
)
