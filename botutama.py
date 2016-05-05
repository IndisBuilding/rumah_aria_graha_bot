import sys
from time import sleep, strftime
import telepot
import lampu, terminal


global pin_lampu, pin_terminal
pin_lampu    = lampu.pin_lampu
pin_terminal = terminal.pin_terminal


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Pesan diterima: %s' % command


    if command == "Menu" or command == "menu" or command == "/menu":
        bot.sendMessage(chat_id, \
	"Silakan pilih menu yang tersedia: \n"\
	"1. Kos Lampu Luar \n"\
	"2. Kos Lampu Dalam Cewek \n"\
	"3. Kos Lampu Dalam Cowok \n"\
        "4. Dispenser Cewek \n"\
        "5. Dispenser Cowok")
        bot.sendMessage(chat_id, "Ketik digit [1-5] diikuti on atau off.")
        bot.sendMessage(chat_id, "Misal : 1 on")
        bot.sendMessage(chat_id, "Atau klik menu cepat yang tampil di setiap bagian bawah!")

    if command == "1 on":
        lampu.lampu_on(pin_lampu[0])
        file = open("status1.txt", "w")
        file.write("menyala")
        file.close()
        bot.sendMessage(chat_id, "Kos Lampu Luar \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
    elif command == "1 off":
        lampu.lampu_off(pin_lampu[0])
        file = open("status1.txt", "w")
        file.write("mati")
        file.close()
        bot.sendMessage(chat_id, "Kos Lampu Luar \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
    if command == "2 on":
        lampu.lampu_on(pin_lampu[1])
        file = open("status2.txt", "w")
        file.write("menyala")
        file.close()
        bot.sendMessage(chat_id, "Kos Lampu Dalam Cewek \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
    elif command == "2 off":
        lampu.lampu_off(pin_lampu[1])
        file = open("status2.txt", "w")
        file.write("mati")
        file.close()
        bot.sendMessage(chat_id, "Kos Lampu Dalam Cewek \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
    if command == "3 on":
        lampu.lampu_on(pin_lampu[2])
        file = open("status3.txt", "w")
        file.write("menyala")
        file.close()
        bot.sendMessage(chat_id, "Kos Lampu Dalam Cowok \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
    elif command == "3 off":
        lampu.lampu_off(pin_lampu[2])
        file = open("status3.txt", "w")
        file.write("mati")
        file.close()
        bot.sendMessage(chat_id, "Kos Lampu Dalam Cowok \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
    if command == "4 on":
        terminal.terminal_on(pin_terminal[0])
        file = open("status4.txt", "w")
        file.write("menyala")
        file.close()
        bot.sendMessage(chat_id, "Dispenser Cewek \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
    elif command == "4 off":
        terminal.terminal_off(pin_terminal[0])
        file = open("status4.txt", "w")
        file.write("mati")
        file.close()
        bot.sendMessage(chat_id, "Dispenser Cewek \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
    if command == "5 on":
        terminal.terminal_on(pin_terminal[1])
        file = open("status5.txt", "w")
        file.write("menyala")
        file.close()
        bot.sendMessage(chat_id, "Dispenser Cowok \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
    elif command == "5 off":
        terminal.terminal_off(pin_terminal[1])
        file = open("status5.txt", "w")
        file.write("mati")
        file.close()
        bot.sendMessage(chat_id, "Dispenser Cowok \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))

    if command == "/1" or command == "Kos Lampu Luar":
        status1 = open("status1.txt", "r").read()
        bot.sendMessage(chat_id, "Status sebelumnya --> %s" % (status1))
        if status1 == "mati":
            lampu.lampu_on(pin_lampu[0])
            file = open("status1.txt", "w")
            file.write("menyala")
            file.close()
            bot.sendMessage(chat_id, "Kos Lampu Luar \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status1 = open("status1.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status1))
        elif status1 == "menyala":
            lampu.lampu_off(pin_lampu[0])
            file = open("status1.txt", "w")
            file.write("mati")
            file.close()
            bot.sendMessage(chat_id, "Kos Lampu Luar \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status1 = open("status1.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status1))

    elif command == "/2" or command == "Kos Lampu Dalam Cewek":
        status2 = open("status2.txt", "r").read()
        bot.sendMessage(chat_id, "Status sebelumnya --> %s" % (status2))
        if status2 == "mati":
            lampu.lampu_on(pin_lampu[1])
            file = open("status2.txt", "w")
            file.write("menyala")
            file.close()
            bot.sendMessage(chat_id, "Kos Lampu Dalam Cewek \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status2 = open("status2.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status2))
        elif status2 == "menyala":
            lampu.lampu_off(pin_lampu[1])
            file = open("status2.txt", "w")
            file.write("mati")
            file.close()
            bot.sendMessage(chat_id, "Kos Lampu Dalam Cewek \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status2 = open("status2.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status2))

    elif command == "/3" or command == "Kos Lampu Dalam Cowok":
        status3 = open("status3.txt", "r").read()
        bot.sendMessage(chat_id, "Status sebelumnya --> %s" % (status3))
        if status3 == "mati":
            lampu.lampu_on(pin_lampu[2])
            file = open("status3.txt", "w")
            file.write("menyala")
            file.close()
            bot.sendMessage(chat_id, "Kos Lampu Dalam Cowok \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status3 = open("status3.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status3))
        elif status3 == "menyala":
            lampu.lampu_off(pin_lampu[2])
            file = open("status3.txt", "w")
            file.write("mati")
            file.close()
            bot.sendMessage(chat_id, "Kos Lampu Dalam Cowok \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status3 = open("status3.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status3))

    elif command == "/4" or command == "Dispenser Cewek":
        status4 = open("status4.txt", "r").read()
        bot.sendMessage(chat_id, "Status sebelumnya --> %s" % (status4))
        if status4 == "mati":
            terminal.terminal_on(pin_terminal[0])
            file = open("status4.txt", "w")
            file.write("menyala")
            file.close()
            bot.sendMessage(chat_id, "Dispenser Cewek \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status4 = open("status4.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status4))
        elif status4 == "menyala":
            terminal.terminal_off(pin_terminal[0])
            file = open("status4.txt", "w")
            file.write("mati")
            file.close()
            bot.sendMessage(chat_id, "Dispenser Cewek \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status4 = open("status4.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status4))

    elif command == "/5" or command == "Dispenser Cowok":
        status5 = open("status5.txt", "r").read()
        bot.sendMessage(chat_id, "Status sebelumnya --> %s" % (status5))
        if status5 == "mati":
            terminal.terminal_on(pin_terminal[1])
            file = open("status5.txt", "w")
            file.write("menyala")
            file.close()
            bot.sendMessage(chat_id, "Dispenser Cowok \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status5 = open("status5.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status5))
        elif status5 == "menyala":
            terminal.terminal_off(pin_terminal[1])
            file = open("status5.txt", "w")
            file.write("mati")
            file.close()
            bot.sendMessage(chat_id, "Dispenser Cowok \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status5 = open("status5.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status5))


    if command == 'status' or command == 'Status' or command == "/status":
        status1 = open('status1.txt', 'r').read()
        status2 = open('status2.txt', 'r').read()
        status3 = open('status3.txt', 'r').read()
        status4 = open('status4.txt', 'r').read()
        status5 = open('status5.txt', 'r').read()
        
        bot.sendMessage(chat_id, \
        "Status kondisi perangkat listrik saat ini --> \n"\
        "1. Kos Lampu Luar 		--> %s\n"\
        "2. Kos Lampu Dalam Cewek 	--> %s\n"\
        "3. Kos Lampu Dalam Cowok 	--> %s\n"\
        "4. Dispenser Cewek 		--> %s\n"\
        "5. Dispenser Cowok		--> %s" % (status1, status2, status3, status4, status5))


    #bot.sendMessage(chat_id, "/menu \n \t\t\t\t /status \n /1 \n\t /2 \n /3 \n\t /4 \t /5")
    show_keyboard = {'keyboard': [['Kos Lampu Luar'], ['Kos Lampu Dalam Cewek', 'Kos Lampu Dalam Cowok'], ['Dispenser Cewek', 'Dispenser Cowok'], ['Menu', 'Status']]}
    bot.sendMessage(chat_id, 'Pilih menu cepat :', reply_markup=show_keyboard)

bot = telepot.Bot('186043755:AAG5sPLEjMfXwUiC3Rxj5H99P5mMoQJvpq8')
bot.message_loop(handle)
print 'Mendengarkan ...'

while 1:
    sleep(10)
