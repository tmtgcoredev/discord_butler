import discord
import os

if os.environ['CI']:
    print('Looks like GitHub!')
else:
    print('Maybe running locally?')
