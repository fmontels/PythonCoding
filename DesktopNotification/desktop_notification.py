import time
import time
from plyer import notification


if __name__ == "__main__":
    notification.notify(
        title="ALERT!!!",
        message="Take a break! It has been an hour!",
        timeout=5,
    )
