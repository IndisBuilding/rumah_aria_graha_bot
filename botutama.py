import sys
from time import sleep, strftime
import telepot
import lampupowmans


global pin_lampu
pin_lampu = lampupowmans.pin_lampu


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Pesan diterima: %s' % command


    if command == "Menu" or command == "menu" or command == "/menu":
        bot.sendMessage(chat_id, \
	"Silakan pilih menu yang tersedia: \n"\
	"1. Lampu atas \n"\
	"2. Lampu tengah \n"\
	"3. Lampu bawah ")
        bot.sendMessage(chat_id, "Pilih digit [1-3] diikuti on atau off.")
        bot.sendMessage(chat_id, "Misal : 3 on")
        bot.sendMessage(chat_id, "Atau klik menu cepat yang tampil di setiap bagian bawah!")

    if command == "1 on":
        lampupowmans.lampu_on(pin_lampu[0])
        file = open("status1.txt", "w")
        file.write("menyala")
        file.close()
        bot.sendMessage(chat_id, "lampu atas powmans \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
    elif command == "1 off":
        lampupowmans.lampu_off(pin_lampu[0])
        file = open("status1.txt", "w")
        file.write("mati")
        file.close()
        bot.sendMessage(chat_id, "lampu atas powmans \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
    if command == "2 on":
        lampupowmans.lampu_on(pin_lampu[1])
        file = open("status2.txt", "w")
        file.write("menyala")
        file.close()
        bot.sendMessage(chat_id, "lampu tengah powmans \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
    elif command == "2 off":
        lampupowmans.lampu_off(pin_lampu[1])
        file = open("status2.txt", "w")
        file.write("mati")
        file.close()
        bot.sendMessage(chat_id, "lampu tengah powmans \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
    if command == "3 on":
        lampupowmans.lampu_on(pin_lampu[2])
        file = open("status3.txt", "w")
        file.write("menyala")
        file.close()
        bot.sendMessage(chat_id, "lampu bawah powmans \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
    elif command == "3 off":
        lampupowmans.lampu_off(pin_lampu[2])
        file = open("status3.txt", "w")
        file.write("mati")
        file.close()
        bot.sendMessage(chat_id, "lampu bawah powmans \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))

    if command == "/1":
        status1 = open("status1.txt", "r").read()
        bot.sendMessage(chat_id, "Status sebelumnya --> %s" % (status1))
        if status1 == "mati":
            lampupowmans.lampu_on(pin_lampu[0])
            file = open("status1.txt", "w")
            file.write("menyala")
            file.close()
            bot.sendMessage(chat_id, "lampu atas powmans \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status1 = open("status1.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status1))
        elif status1 == "menyala":
            lampupowmans.lampu_off(pin_lampu[0])
            file = open("status1.txt", "w")
            file.write("mati")
            file.close()
            bot.sendMessage(chat_id, "lampu atas powmans \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status1 = open("status1.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status1))

    elif command == "/2":
        status2 = open("status2.txt", "r").read()
        bot.sendMessage(chat_id, "Status sebelumnya --> %s" % (status2))
        if status2 == "mati":
            lampupowmans.lampu_on(pin_lampu[1])
            file = open("status2.txt", "w")
            file.write("menyala")
            file.close()
            bot.sendMessage(chat_id, "lampu atas powmans \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status2 = open("status2.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status2))
        elif status2 == "menyala":
            lampupowmans.lampu_off(pin_lampu[1])
            file = open("status2.txt", "w")
            file.write("mati")
            file.close()
            bot.sendMessage(chat_id, "lampu atas powmans \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status2 = open("status2.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status2))

    elif command == "/3":
        status3 = open("status3.txt", "r").read()
        bot.sendMessage(chat_id, "Status sebelumnya --> %s" % (status3))
        if status3 == "mati":
            lampupowmans.lampu_on(pin_lampu[2])
            file = open("status3.txt", "w")
            file.write("menyala")
            file.close()
            bot.sendMessage(chat_id, "lampu atas powmans \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status3 = open("status3.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status3))
        elif status3 == "menyala":
            lampupowmans.lampu_off(pin_lampu[2])
            file = open("status3.txt", "w")
            file.write("mati")
            file.close()
            bot.sendMessage(chat_id, "lampu atas powmans \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status3 = open("status3.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status3))


    if command == 'status' or command == 'Status' or command == "/status":
        status1 = open('status1.txt', 'r').read()
        status2 = open('status2.txt', 'r').read()
        status3 = open('status3.txt', 'r').read()
        
        bot.sendMessage(chat_id, \
        "Status kondisi perangkat listrik saat ini --> \n"\
        "1. Lampu atas		--> %s\n" \
        "2. Lampu tengah	--> %s\n" \
        "3. Lampu bawah		--> %s\n" % (status1, status2, status3))


    elif command == 'kata kunci':
        bot.sendMessage(chat_id, "abang sayang adek :)")
        bot.sendMessage(chat_id, "adek juga sayang abang :*")

    bot.sendMessage(chat_id, "/menu \t /status \t /1 \t /2 \t /3")

bot = telepot.Bot('178732152:AAFBCunAYIFuFBuVOgDCzR6Rgb7BbXTVypQ')
bot.message_loop(handle)
print 'Mendengarkan ...'

while 1:
    sleep(10)
