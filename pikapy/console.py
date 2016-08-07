import argparse
import sys
from pikapy import *
from pikapy.ptcexceptions import *
from pgoapi import PGoApi
from pgoapi.utilities import f2i
from pgoapi import utilities as util
from pgoapi.exceptions import AuthException
import pprint
import time
import threading
import getopt





def parse_arguments(args):
    """Parse the command line arguments for the console commands.

    Args:
      args (List[str]): List of string arguments to be parsed.

    Returns:
      Namespace: Namespace with the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description='Pokemon Trainer Club Account Creator'
    )
    parser.add_argument(
        '-u', '--username', type=str, default=None,
        help='Username for the new account (defaults to random string).'
    )
    parser.add_argument(
        '-p', '--password', type=str, default=None,
        help='Password for the new account (defaults to random string).'
    )
    parser.add_argument(
        '-e', '--email', type=str, default=None,
        help='Email for the new account (defaults to random email-like string).'
    )
    parser.add_argument(
        '--email-tag', action='store_true',
        help='Add the username as a tag to the email (i.e addr+tag@mail.com).'
    )
    parser.add_argument(
        '-c','--count', type=int,default=1,
        help='Number of accounts to generate.'
    )
    return parser.parse_args(args)


def entry():
    """Main entry point for the package console commands"""
    args = parse_arguments(sys.argv[1:])
    try:
    # Create the random account
        account_info = random_account(
            args.username, args.password, args.email, args.email_tag, args.count
        )

        # Display the account credentials
        print('Created new account:')
        print('  Username:  {}'.format(account_info[USERNAME]))
        print('  Passwrd:  {}'.format(account_info[PASSWORD]))
        print('  Email   :  {}'.format(account_info[EMAIL]))

        # Accept Terms Service
        
        accept_tos(account_info[USERNAME], account_info[PASSWORD])

        # Append usernames 
        with open("usernames.txt", "a") as ulist:
            ulist.write(account_info[USERNAME]+"\n")
            ulist.close()
            
        with open("pokemaparguments.txt", "a") as plist:
            plist.write(" -u " + account_info[USERNAME])
            plist.close()
        print('Usernames stored in usernames.txt and formated ones in pokemaparguments.txt ')
        time.sleep(2)

    # Handle account creation failure exceptions
    except PTCInvalidPasswordException as err:
        print('Invalid password: {}'.format(err))
    except (PTCInvalidEmailException, PTCInvalidNameException) as err:
        print('Failed to create account! {}'.format(err))
    except PTCException as err:
        print('Failed to create account! General error:  {}'.format(err))

def accept_tos(username, password):
        api = PGoApi()
        api.set_position(40.7127837, -74.005941, 0.0)
        api.login('ptc', username, password)
        time.sleep(2)
        req = api.create_request()
        req.mark_tutorial_complete(tutorials_completed = 0, send_marketing_emails = False, send_push_notifications = False)
        response = req.call()
        print('Accepted Terms of Service for {}'.format(username))
