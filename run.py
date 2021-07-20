import requests, json, colorama, time, sys
from colorama import init, Fore, Style, Back

class Interface:

	def __init__(self):

		# initialize colors
		colorama.init()
		print(Style.BRIGHT, end='\b')

		self.username     = ""
		self.password     = ""

		self.hiddenspaces = " " * 2

		self.filled       = False

		self.deleted      = 0

	def printC(self, msg:str, color:Fore, end="\n"):
		return print(self.hiddenspaces + color + msg + Fore.RESET, end=end)

	def welcome(self):
		print(
f"""
{self.hiddenspaces}{Back.MAGENTA}{Fore.WHITE}┌                                ┐{Back.RESET}
{self.hiddenspaces}{Style.DIM}{Fore.BLACK}{Back.MAGENTA} INSTAGRAM DIRECT MESSAGE CLEANER {Back.RESET}
{self.hiddenspaces}{Fore.BLACK}{Back.MAGENTA}       GITHUB.COM/ASHILLES        {Back.RESET}{Style.BRIGHT}
{self.hiddenspaces}{Back.MAGENTA}{Fore.WHITE}└                                ┘{Back.RESET}{Fore.RESET}

{self.hiddenspaces}This work is licensed under a Creative Commons\n{self.hiddenspaces}Attribution-NonCommercial 4.0 International License

{self.hiddenspaces}Follow me on twitter {Fore.CYAN}@ASH1LLES{Fore.RESET}, S/O {Fore.CYAN}@0fve2{Fore.RESET}.
""")

	def pause(self):
		try:
			input()
		except:
			sys.exit()

	def inputs(self):

		# Username loop
		while len(self.username) < 1:
			try:

				print(self.hiddenspaces + "Username : ", end=Fore.YELLOW)
				self.username = input("")
				print(end=Fore.RESET)
				if(len(self.username) > 0):
					break
				else:
					self.printC("Username is not filled correctly.", Fore.RED)

			except KeyboardInterrupt:
				sys.exit()

			except:
				pass

		# Password loop
		while len(self.password) < 6:
			try:
				print(self.hiddenspaces + "Password : ", end=Fore.YELLOW)
				self.password = input("")
				print(end=Fore.RESET)
				if(len(self.password) >= 6):
					break
				else:
					self.printC("Password must be at least 6 characters.", Fore.RED)

			except KeyboardInterrupt:
				sys.exit()

			except:
				pass

		if(len(self.username) > 0 and len(self.password) >= 6):
			self.filled = True

class Instagram:

	def __init__(self):

		self.authenticated = False

		self.url           = "https://i.instagram.com"

		self.endpoints     = {
			"login":"/accounts/login/ajax/",
			"logout":"/accounts/logout/",
			"inbox":"/api/v1/direct_v2/inbox/?limit=500&thread_message_limit=1",
			"hide": "/api/v1/direct_v2/threads/%s/hide/"
		}

		self.session       = requests.session()
		self.headers       = {
			"Accept": "*/*",
			"Accept-Encoding": "gzip, deflate",
			"Accept-Language": "en-US",
			"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 123.1.0.26.115 (iPhone11,8; iOS 14_6; en_US; en-US; scale=2.00; 828x1792; 190542906)",
			"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			"X-IG-Capabilities": "3brTvw==",
			"X-IG-Connection-Type": "WIFI"
		}
		self.csrf          = ""

		self.account       = None

		self.threads       = []

	def getCSRF(self):
		try:
			self.session.headers = self.headers
			self.session.headers.update({'Referer': self.url})
			getcsrf = self.session.get(self.url, timeout=10)
			self.csrf = getcsrf.cookies['csrftoken']
			self.session.headers.update({'X-CSRFToken': self.csrf})
		except:
			interface.printC(f"\r{interface.hiddenspaces}Failed getting CSRF token, make sure\n{interface.hiddenspaces}you are connected to the internet.", Fore.RED), interface.pause(), sys.exit()		

	def login(self):

		if(len(self.csrf) < 1):
			self.getCSRF()

		try:

			self.account = self.session.post(self.url + self.endpoints['login'], data={"username":interface.username,"password":interface.password}, allow_redirects=True)
			response = self.account.json()

			if(response['status'] == "ok"):
				if "authenticated" in response:
					if response['authenticated'] == False:
						return False, "Incorrect username or password"
					elif(response['authenticated'] == True):
						self.authenticated = True
						return True, self.authenticated
			elif('spam' in response or 'message' in response and response['message'] == 'Please wait a few minutes before you try again.'):
				return False, "Too many requests, try again later."
			else:
				return False, "Please verify this login and make sure 2FA is disabled"

		except Exception as e:
			return False, f"Could not connect to Instagram. {e}"

		return False, f"\r{interface.hiddenspaces}Error logging in."

	def validate(self):

		interface.printC("Instagram login credentials", Fore.RESET)

		while not self.authenticated:

			interface.inputs()
			print()
			print(f"{interface.hiddenspaces}{Fore.MAGENTA}*{Fore.RESET} Logging in..", end='')
			LOGIN = self.login()
			if(not LOGIN[0]):
				interface.username = ""
				interface.password = ""
				interface.printC(f"\r{interface.hiddenspaces}{LOGIN[1]}", Fore.RED)
			else:
				interface.printC(f"\r{interface.hiddenspaces}{Back.GREEN} OK ! {Back.RESET}{' '* 10}", Fore.RESET, end='')
				break

	def clean(self):

		print(f"\r{interface.hiddenspaces}{Fore.BLUE}Press enter to start {Fore.RESET}", end='')
		input()
		print()

		data = self.session.get(self.url + self.endpoints['inbox'])
		dataJSON = data.json()

		if(len(dataJSON['inbox']['threads']) < 1): # Check if inbox is not empty
			return interface.printC(f"\r{interface.hiddenspaces}The inbox is empty.. Press enter key to exit", Fore.RED), interface.pause(), sys.exit()

		print(f"{interface.hiddenspaces}{Back.GREEN} OK ! {Back.RESET} {Back.RED} {dataJSON['viewer']['username']} {Back.RESET} {Back.CYAN} {len(dataJSON['inbox']['threads'])} 💬 {Back.RESET}{' '*7}\n")
		for thread in dataJSON['inbox']['threads']:
			self.threads.append(thread['thread_id'])

		headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-length': '0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'sessionid={self.account.cookies["sessionid"]}; shbid={data.cookies["shbid"]}; shbts={data.cookies["shbts"]}; rur={self.account.cookies["rur"]}',
            'origin': 'https://www.instagram.com',
            'pragma': 'no-cache',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'x-asbd-id': '437806',
            'x-csrftoken': self.csrf,
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '3e97309db180'
		}

		for thread in self.threads:
			try:
				response = self.session.post(self.url + self.endpoints['hide'] % thread, headers=headers)
				if(response.status_code == 200):
					interface.deleted += 1
				interface.printC(f"{interface.deleted}/{len(self.threads)} Deleting DMs..", Fore.RESET, end='\r')
				time.sleep(1.2)
			except KeyboardInterrupt:
				sys.exit()
			except:
				pass

		print(" " * 30)

		interface.printC(f"Results\n{interface.hiddenspaces}{Back.RED} Deleted {interface.deleted} out of {len(self.threads)} DMs {Back.RESET}", Fore.RESET, end='')
		input(" ")

if __name__ == "__main__":
	
	interface = Interface()
	interface.welcome()

	instagram = Instagram()

	instagram.validate()

	instagram.clean()
