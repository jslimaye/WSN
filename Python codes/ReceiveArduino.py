import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
from time import sleep
import spidev
from sendData import connection

GPIO.setmode(GPIO.BCM)

pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)

radio.setPayloadSize(32)
radio.setChannel(0x64)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1, pipes[1])
radio.printDetails()
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
    
    print("AireQua=",air," temp=",temp)
    connection(temp,air)
	
    sleep(10)
    
