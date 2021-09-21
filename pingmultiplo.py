import os
import time
print('#' *41)
print('### Testador de IP''s e Hosts MULTIPLOS ###')
print('#' *41)
print('\nBy. Mr.Arthur (EU MESMO)')

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('\nVerificando o IP: ', ip )
        print('-' *60)
        os.system('ping -n 2 ' + ip)
        print('-' * 60)
        time.sleep(5)

time.sleep(2)
os.system('pause')