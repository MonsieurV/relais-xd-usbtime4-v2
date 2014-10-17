import serial
import time
import Tkinter
import tkMessageBox

PORT_COM = "/dev/ttyUSB0"

class TestUi(object):
	ON = "ON"
	OFF = "OFF"

	def __init__(self):
		self.state = TestUi.OFF
		self.ser = None

	def start(self):
		try:
			self.ser = serial.Serial(PORT_COM)
			# print(self.ser.name)
			print("Tchou tchou!")
			top = Tkinter.Tk()
			b1 = Tkinter.Button(top, text ="Allumer", command = self.on)
			b1.pack()
			b2 = Tkinter.Button(top, text ="Eteindre", command = self.off)
			b2.pack()
			b3 = Tkinter.Button(top, text ="Switch", command = self.switch)
			b3.pack()
			top.title("L'interupteur chinois")
			top.geometry("300x150")
			top.mainloop()
		finally:
			# print("Close")
			self.ser.close()             # close port

	def off(self):
		print("Off clicked")
		self.ser.write("5501110000000168".decode("hex"))
		self.state = TestUi.OFF

	def on(self):
		print("On clicked")
		self.ser.write("5501120000000169".decode("hex"))
		self.state = TestUi.ON

	def switch(self):
		print("Switch clicked")
		print(self.state)
		if self.state == TestUi.ON:
			self.off()
		else:
			self.on()
	


if __name__ == "__main__":
	test = TestUi()
	test.start()
