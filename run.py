import requests, json, colorama, time, sys
from colorama import init, Fore, Style, Back
from getpass import getpass

class Interface:

	def __init__(self):

		# initialize colors
		colorama.init()
		print(Style.BRIGHT, end='\b')

		self.username     = ""
		self.password     = ""

		self.hiddenspaces = "  "

		self.filled       = False

	def printC(self, msg:str, color:Fore):
		return print(self.hiddenspaces + color + msg + Fore.RESET)

	def welcome(self):
		print(
f"""

  {Back.MAGENTA}{Fore.WHITE}┌                                ┐{Back.RESET}
  {Style.DIM}{Fore.BLACK}{Back.MAGENTA} INSTAGRAM DIRECT MESSAGE CLEANER {Back.RESET}
  {Fore.BLACK}{Back.MAGENTA}       GITHUB.COM/ASHILLES        {Back.RESET}{Style.BRIGHT}
  {Back.MAGENTA}{Fore.WHITE}└                                ┘{Back.RESET}{Fore.RESET}

  Thanks for using this tool.
  Follow me on twitter {Fore.CYAN}@ASH1LLES{Fore.RESET}, S/O {Fore.CYAN}@0fve2{Fore.RESET}.
""")

	def inputs(self):

		# Username loop
		while len(self.username) < 1:
			try:

				self.username = input(self.hiddenspaces + "Username : ")
				if(len(self.username) > 0):
					break
				else:
					self.printC("Username is not filled correctly!", Fore.RED)

			except KeyboardInterrupt:
				sys.exit()

			except:
				pass

		# Password loop
		self.printC('[Password is hidden]', Fore.BLUE)
		while len(self.password) < 6:
			try:
				self.password = getpass(self.hiddenspaces + "Password : ")
				if(len(self.password) >= 6):
					break
				else:
					self.printC("Password must be at least 6 characters!", Fore.RED)

			except KeyboardInterrupt:
				sys.exit()

			except:
				pass

		if(len(self.username) > 0 and len(self.password) >= 6):
			self.filled = True

if __name__ == "__main__":
	
	interface = Interface()
	interface.welcome()
	interface.inputs()
