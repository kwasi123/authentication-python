import re
import colorama

from colorama import Fore, Back, Style
from datetime import datetime

class Validator:

  colorama.init(autoreset=True)

  error_messages = {
  'email': 'email_is_not_valid', 
  'username': 'username_is_not_valid', 
  'password': 'password_is_not_valid'
  }

  def validate_email(email):
    try:
      assert type(email) == str, 'Email should be a string.'

      pattern = r'^[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$'
      result = re.search(pattern, email)

      if result is not None:
        return 'valid'
      print('{}[{}] {}{}'.format(Fore.RED, datetime.now(), Fore.WHITE 
        + Style.BRIGHT, Validator.error_messages.get('email')))

    except ValueError:
        print('{}[{}] {}{}'.format(Fore.RED, datetime.now(), Fore.WHITE 
          + Style.BRIGHT, Validator.error_messages.get('email')))
  
  def validate_username(username):
    try:
      if len(username) > 7:
        pattern = r'[a-zA-Z0-9_]+'
        result = re.search(pattern, username)
        return 'is_valid'
      print('{}[{}] {}Username should be a minimum of 8 characters'.format(
        Fore.RED, datetime.now(), Fore.WHITE + Style.BRIGHT))
      print('{}[{}] {}Username should be alphanumeric and can only contain an underscore'.format(
        Fore.RED, datetime.now(), Fore.WHITE + Style.BRIGHT))

    except:
      print('{}[{}] {}{}'.format(Fore.RED, datetime.now(), Fore.WHITE 
        + Style.BRIGHT, Validator.error_messages.get('username')))

  def validate_password(password):
    try:
      if len(password) > 7:
        pattern = r'[a-zA-Z0-9_$% ]+'
        result = re.search(pattern, password)
        return 'is_valid'
      print('{}[{}] {}Password should be a minumum of 8 characters'.format(Fore.RED, 
        datetime.now(), Fore.WHITE + Style.BRIGHT))
    
    except:
      print('{}[{}] {}{}'.format(Fore.RED, datetime.now(), Fore.WHITE 
        + Style.BRIGHT, Validator.error_messages.get('password')))
