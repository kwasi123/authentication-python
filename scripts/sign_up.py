#!/usr/bin/python

import os
import sys
import csv
import colorama

from colorama import Fore, Back, Style
from datetime import datetime
from validate import Validator


def check_user_input(user_info):
	'''
	This function checks if the input user gave was correct and does not exist in the database.
	'''
	
	if Validator.validate_email(user_info.get('email')) and Validator.validate_username(user_info.get('username')) and Validator.validate_password(user_info.get('password1')):
		if user_info.get('password1') == user_info.get('password2'):
			return user_info
		print('{}[{}] {}Passwords do not match'.format(Fore.RED, datetime.now(), Fore.WHITE + Style.BRIGHT))


def sign_up(user_info, csv_file):
	'''
	This function checks if user_info exists in the database.
	If not, it adds the user to the database.
	'''

	check_user_input(user_info)

	with open(csv_file, mode='r') as file:
		reader = csv.DictReader(file)
		reader_list = list(reader)

		emails = []
		usernames = []
		passwords = []

		# print(reader_list)

		for record in reader_list:
			emails.append(record.get('email'))
			usernames.append(record.get('username'))
			passwords.append(record.get('password'))

		if user_info.get('email') not in emails and user_info.get('username') not in usernames and user_info.get('password1') not in passwords:
			with open(csv_file, mode='a') as file:
				writer = csv.writer(file)
				writer.writerow(user_info.values())

				print('{}[{}] {}USER ADDED SUCCESSFULLY!!'.format(Fore.GREEN, datetime.now(), Fore.WHITE + Style.BRIGHT))

		elif user_info.get('email') in emails:
			print('{}[{}] {}Email already exists'.format(Fore.RED, datetime.now(), Fore.WHITE + Style.BRIGHT))

		elif user_info.get('username') in usernames:
			print('{}[{}] {}Username already exists'.format(Fore.RED, datetime.now(), Fore.WHITE + Style.BRIGHT))

		elif user_info.get('password1') in passwords:
			print('{}[{}] {}Password already exists'.format(Fore.RED, datetime.now(), Fore.WHITE + Style.BRIGHT))

