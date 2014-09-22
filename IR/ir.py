import lirc

sockid = lirc.init("myprogram")
print("Ready")

while True:
	code = lirc.nextcode()
	if code: print(code[0])
