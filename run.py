import requests, os

def random():
 print(f'[!] Wait Slur..')
 os.system('python3 31r.py')
 
def wp():
 print(f'[!] Wait Slur..')
 os.system('python3 31w.py')
 

print('''-=[ ROBH TOOLS ]=-

     [Menu]
[1] Shell Scanner ( ALL WEBSITE )
[2] Shell Scanner ( Wordpress Only )
[3] Keluar
''')
menu = input('[?] Silahkan pilih menu : ')

if menu == '1':
 random()
elif menu == '2':
 wp()
elif menu == '3':
 print('[?] Keluar..')
 sys.exit()
else:
 print('[?] Perintah tidak diketahui..')
 sys.exit()
