import os
import csv
import colorama

from datetime import datetime
from colorama import Fore, Back, Style


def user_login(user_info, csv_file):
	'''
	This function checks to see if a user is in the database and logs him/her in
	'''

	with open(csv_file, mode='r') as file:
		reader = csv.DictReader(file)
		users = list(reader)

		for user in users:
			if user_info.get('email') == user['email'] and user_info.get('password') == user['password']:
				print('{}[{}] {}USER IS SIGNED IN SUCCESSFULLY!!'.format(Fore.GREEN, 
					datetime.now(), Fore.WHITE + Style.BRIGHT))
				break
			print('{}[{}] {}Invalid Credentials'.format(Fore.RED, datetime.now(), 
				Fore.WHITE + Style.BRIGHT))
