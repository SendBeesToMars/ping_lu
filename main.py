
import os
import secret
import fbchat
from fbchat.models import *
import time

starttime = time.time()

hostname = secret.hostname
while True:
    # -c linux, -n windows
    response = os.system("ping -c 1 " + hostname)  # + " > /dev/null 2>&1")

    if response == 0:
        print("sucess")
    else:
        print("failure")
        client = fbchat.Client(secret.username, secret.pw)
        client.send(Message(text="server down :) -bot"), thread_id=secret.friendo,
                    thread_type=ThreadType.USER)
        time.sleep(43200.0 - ((time.time() - starttime) %
                   43200.0))  # 43200 sleep for 12h

    time.sleep(3600.0 - ((time.time() - starttime) % 3600.0))  # 3600 sleep 1h
