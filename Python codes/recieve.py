import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
from time import sleep
import spidev
from sendData import connection
import threading
import time

GPIO.setmode(GPIO.BCM)
global pipes
pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]

class myThread (threading.Thread):
	def __init__(self, channel, pipe, delay):
		threading.Thread.__init__(self)
		self.delay = delay
		self.channel = channel
		self.pipe = pipe
	def run(self):
   
		radio = NRF24(GPIO, spidev.SpiDev())
		radio.begin(0, 17)

		radio.setPayloadSize(32)
		if self.channel == 64:		
			radio.setChannel(0x64)
		else:
			radio.setChannel(0x70)
		radio.setDataRate(NRF24.BR_1MBPS)
		radio.setPALevel(NRF24.PA_MIN)

		radio.setAutoAck(True)
		radio.enableDynamicPayloads()
		radio.enableAckPayload()
		
		global pipes
		radio.openReadingPipe(1, pipes[self.pipe])
		#radio.printDetails()
		radio.startListening()

		while(1):
			# ackPL = [1]
			while not radio.available(0):
				sleep(1/100)
			receivedMessage = []
			radio.read(receivedMessage, radio.getDynamicPayloadSize())
			print("Received: {}".format(receivedMessage))

			print("Translating the receivedMessage into unicode characters")
			string = ""
			for n in receivedMessage:
			# Decode into standard unicode set
				if (n>=32 and n<= 126):
					string += chr(n)
			print("Out received message decodes to: {}".format(string))
			air = string[:3]
			temp = float(string[4:9])
			
			print("AireQua=",air," temp=",temp," Channel = ",channel)
			connection(temp,air)
			
			sleep(self.delay)
		

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(64, 0, 5)
thread2 = myThread(70, 1, 2.1)

# Start new Threads
thread1.start()
thread2.start()



