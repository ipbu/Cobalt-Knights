import replit
import time
import colorama

def ctxt(text, color):
    match color:
        case "red":
            color = colorama.Fore.RED
        case "yellow":
            color = colorama.Fore.YELLOW
        case "green":
            color = colorama.Fore.GREEN
        case "cyan":
            color = colorama.Fore.CYAN
        case "blue":
            color = colorama.Fore.BLUE
        case "magenta":
            color = colorama.Fore.MAGENTA
    return color + text
def tprint(text, time=1):
    time.sleep(time)
    print(text)
def eclear():
    input("PRESS [ENTER] TO CONTINUE")
    replit.clear()
