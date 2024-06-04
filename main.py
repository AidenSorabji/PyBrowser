# |-----------------------|
# |      Web Browser      |
# |      By SpaceN64      |
# |-----------------------|

# Imports
from http import HTTPStatus
import webbrowser as wb
import time as t
import random as r
from random import choice
import datetime
import calendar
import zoneinfo

print("Loading...")
t.sleep(1.5)

# Specifics
url = ["URL", "Url", "url"]
exit = ["exit", "Exit", "exit()", "Exit()"]
random = ["Random", "random"]
websites = ["https://www.google.com", "https://github.com", "https://twitter.com", "https://apple.com", "https://youtube.com"]
cmdss = ["CMDS", "Cmds", "cmds", "Commands", "commands"]

def cmds():
    print("""
    
    1. url - Go to a website or server (Must include "https://" without the quotation marks)
    
    2. random - Go to a random website
    
    3. exit - Exit out of PyBrowser
    """)




# Intro
print("""
  _____         ____                                  
 |  __ \       |  _ \                                 
 | |__) |   _  | |_) |_ __ _____      _____  ___ _ __ 
 |  ___/ | | | |  _ <| '__/ _ \ \ /\ / / __|/ _ \ '__|
 | |   | |_| | | |_) | | | (_) \ V  V /\__ \  __/ |   
 |_|    \__, | |____/|_|  \___/ \_/\_/ |___/\___|_|   
         __/ |                                        
        |___/                                         
""")
t.sleep(1.3)

# Main Code
print("""
Welcome to PyBrowser! 

This is a semi-working browser made in python3 using python's "Webbrowser" module.

Don't expect this to work really good, as i literally make this during school when we
were doing presentations lmao

Type cmds for commands, and refer to the repo for help.

""")



def restart():
    type = input(">>> ")
    if type in url:
        print("")
        url_input = input("""Input your URL (include the https)
        
>>> """) 
        wb.open_new_tab(url_input)
        restart()
    elif type in random:
        ras = r.choice(websites)
        wb.open_new_tab(ras)
    elif type in cmdss:
        cmds()
        print("")
    elif type in exit:
        exit()
    else:
        print("")
        restart()

    restart()
restart()
