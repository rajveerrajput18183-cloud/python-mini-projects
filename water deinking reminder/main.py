import time
from plyer import notification

while True:
    notification.notify(
        title="notificaton for raj",
        message= "time to drink water",
        timeout=10
    )
    time.sleep(3600)