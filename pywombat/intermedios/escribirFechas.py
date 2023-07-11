import time
from datetime import datetime

if __name__ == '__main__':
    with open('dates.txt', 'a') as file:

        while True:
            time.sleep(1)
            file.write(str(datetime.now()) + '\n')