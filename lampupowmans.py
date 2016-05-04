import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin_lampu = [13,15,16]
pin_terminal = 18
#13 atas
#15 tengah
#16 bawah
#18 terminal
for i in range(len(pin_lampu)):
	GPIO.setup(pin_lampu[i], GPIO.OUT)
GPIO.setup(pin_terminal, GPIO.OUT)

def lampu_off(pin):
	GPIO.output(pin, 0)

def lampu_on(pin):
	GPIO.output(pin, 1)

#lampu_off(pin_lampu[3])
#lampu_on(pin_lampu[3])
#lampu_on(pin_terminal)
