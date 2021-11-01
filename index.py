import discord
import os

if os.getenv('GALAWAN'):
    print('Looks like GitHub!')
else:
    print('Maybe running locally?')
