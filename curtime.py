import time, os

while True:
    os.system("clear")
    current_time = time.strftime("%H:%M:%S")
    print(f"\033[96m\033[1m\n CURRENT TIME\n [{current_time}]\033[0m")
    time.sleep(1)
