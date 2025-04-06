# Application control functions

import os
import webbrowser

def open_chrome():
    """
    Opens Google Chrome browser.
    
    Usage: Launch Chrome, Open Chrome browser, Start Chrome
    """
    webbrowser.open("https://www.google.com")

def open_firefox():
    """
    Opens Firefox browser.
    
    Usage: Launch Firefox, Open Firefox browser, Start Firefox
    """
    webbrowser.open("https://www.mozilla.org")

def open_calculator():
    """
    Opens the calculator application.
    
    Usage: Open calculator, Launch calc, Start calculator app
    """
    if os.name == 'nt':  # Windows
        os.system("calc")
    elif os.name == 'posix':  # macOS or Linux
        if os.uname().sysname == 'Darwin':  # macOS
            os.system("open -a Calculator")
        else:  # Linux
            os.system("gnome-calculator")

def open_notepad():
    """
    Opens the notepad/text editor application.
    
    Usage: Open notepad, Launch text editor, Start notepad
    """
    if os.name == 'nt':  # Windows
        os.system("notepad")
    elif os.name == 'posix':  # macOS or Linux
        if os.uname().sysname == 'Darwin':  # macOS
            os.system("open -a TextEdit")
        else:  # Linux
            os.system("gedit")

def open_file_explorer():
    """
    Opens the file explorer/finder.
    
    Usage: Open file explorer, Launch finder, Open file manager
    """
    if os.name == 'nt':  # Windows
        os.system("explorer")
    elif os.name == 'posix':  # macOS or Linux
        if os.uname().sysname == 'Darwin':  # macOS
            os.system("open .")
        else:  # Linux
            os.system("xdg-open .")