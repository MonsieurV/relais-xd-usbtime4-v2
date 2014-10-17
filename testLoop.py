import serial
import time

PORT_COM = "/dev/ttyUSB0"
SLEEP_PERIOD = 2

def off(ser):
	ser.write("5501110000000168".decode("hex"))

def on(ser):
	ser.write("5501120000000169".decode("hex"))

ON = "ON"
OFF = "OFF"

if __name__ == "__main__":
	try:
		ser = serial.Serial(PORT_COM)  # open first serial port
		print(ser.name)          # check which port was really used
		print("Blind blind blind!")
		state = ON
		on(ser)
		while True:
			if state == ON:
				off(ser)
				print("Off")
				state = OFF
			else:
				on(ser)
				print("On")
				state = ON
			time.sleep(SLEEP_PERIOD)
	finally:
		print("Close")
		ser.close()             # close port
