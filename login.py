import os, sys

print ("\033[1;32mEnter Username And Password")
print ("\033[1;31;1mWant The Pass ? Pm me 0895620119462")
username = 'rvms'      
password = 'gansasw'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mWelcome To My Tools", 
			sys.exit()

		else:
			print "\n\033[1;36mPassword Salah Goblok!!!\033[00m"
			print "Back Login\n"
			restart()

	else:
		print "\n\033[1;36mSorry Invalid Username !!!\033[00m"
		print "Back Login\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
