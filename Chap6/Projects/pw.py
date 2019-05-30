#! python3

# A basic password manager !VERY INSECURE!

passwords = {'email': 'emailpa55',
             'blog': 'blogpa55',
             'luggage': 'luggagepa55'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account name ' + account)
