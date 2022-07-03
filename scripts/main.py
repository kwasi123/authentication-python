#!/usr/bin/python

import sys
import datetime

from colorama import Fore, Back, Style
from sign_up import sign_up
from sign_in import user_login


def main():
	'''
	This is the main function of the program.
	'''

	sign_up_info = dict()
	sign_in_info = dict()

	filename = sys.argv[1]

	print(f'{Fore.WHITE}{Style.BRIGHT}----------WELCOME TO FSOCIETY----------')

	print(f'{Fore.GREEN}[+] {Fore.WHITE}{Style.BRIGHT}1. Create new account.')
	print(f'{Fore.GREEN}[+] {Fore.WHITE}{Style.BRIGHT}2. Login to your account.')
	print(f'{Fore.GREEN}[+] {Fore.WHITE}{Style.BRIGHT}Press \'q\' to quit.')

	user_input = input(f'{Fore.GREEN}> {Fore.WHITE}{Style.BRIGHT}')

	print('---------------------------------------')


	if user_input.lower() == '1':
		sign_up_info['email'] = input(f'{Fore.GREEN}[+] {Fore.WHITE}{Style.BRIGHT}Email: ')
		sign_up_info['username'] = input(f'{Fore.GREEN}[+] {Fore.WHITE}{Style.BRIGHT}Username: ')
		sign_up_info['password1'] = input(f'{Fore.GREEN}[+] {Fore.WHITE}{Style.BRIGHT}Password: ')
		sign_up_info['password2'] = input(f'{Fore.GREEN}[+] {Fore.WHITE}{Style.BRIGHT}Re-type Password: ')	

		sign_up(sign_up_info, filename)

	elif user_input.lower() == '2':
		sign_in_info['email'] = input(f'{Fore.GREEN}[+] {Fore.WHITE}{Style.BRIGHT}Email: ')
		sign_in_info['password'] = input(f'{Fore.GREEN}[+] {Fore.WHITE}{Style.BRIGHT}Password: ')

		user_login(sign_in_info, filename)

	elif user_input.lower() == 'q':
		sys.exit(0)

	else:
		print(f'{Fore.WHITE}{Back.RED}[!] {Fore.RED}Sorry Wrong')


if __name__ == '__main__':
	main()
