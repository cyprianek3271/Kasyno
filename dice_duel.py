import random
import time
kartony  = [
    'gr1', 'gr2', 'gr3'
]

for i in range(1,12):
    random.shuffle(kartony)
    print(kartony)
    time.sleep(1)
