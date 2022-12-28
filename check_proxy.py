import requests
import threading
import queue

q = queue.Queue()
valid_proxies = []

usr_proxy = str(input("Enter your proxy > "))

try:
	with open(usr_proxy, 'r') as f:
		print(f"Loading {usr_proxy}\n")
		proxies = f.read().split('\n')
		for p in proxies:
			q.put(p)
except FileNotFoundError:
	print(f"There is no file name {usr_proxy}\n")
	with open('proxy_list.txt', 'r') as f:
		print(f"Loading Default Proxy List\n")
		proxies = f.read().split('\n')
		for p in proxies:
			q.put(p)
	


def check_proxies():
	global q
	while not q.empty():
		proxy = q.get()
		try:
			res = requests.get("http://ipinfo.io/json",
				proxies = {'http':proxy,
							'https':proxy})
		except:
			continue
		if res.status_code == 200:
			print(proxy)

for _ in range(10):
	threading.Thread(target=check_proxies).start()