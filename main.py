import secret
import socket
import fbchat
from fbchat.models import Message
import time

starttime = time.time()

hostname = secret.hostname
def main():
	while True:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			result = sock.connect_ex((hostname, 80))
		
		if result == 0:
			print("sucess")
		else:
			print("failure")
			client = fbchat.Client(secret.username, secret.pw)
			client.send(Message(text="server down :) -bot"), thread_id=secret.friendo,
						thread_type=ThreadType.USER)
			time.sleep(43200.0 - ((time.time() - starttime) %
					   43200.0))  # 43200 sleep for 12h

		time.sleep(3600.0 - ((time.time() - starttime) % 3600.0))  # 3600 sleep 1h

if __name__ == "__main__":
    main()