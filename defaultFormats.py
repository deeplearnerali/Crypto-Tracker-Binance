import sys
import colorama
import logging

from colorama import Fore, Style, Back

# simple initialization
logging.basicConfig(level=logging.ERROR, filename=f"SimpleCryptoTracker.log",
    format="%(asctime)s:%(message)s")


colorama.init(autoreset=True)
# some simple classes
class Colors:
    RED: str =  f"{Style.BRIGHT}{Fore.RED}"
    GREEN: str =  f"{Style.BRIGHT}{Fore.GREEN}"
    YELLOW: str = f"{Style.BRIGHT}{Fore.YELLOW}"
    MAGENTA: str = f"{Style.BRIGHT}{Fore.MAGENTA}"
    CYAN: str = f"{Style.BRIGHT}{Fore.CYAN}"
    WHITE: str = f"{Style}{Fore.WHITE}"
    BLACK: str = f"{Style.BRIGHT}{Fore.BLACK}"

# GLOBAL variables
C = Colors()
LINE = f"\n\n{C.RED}{'_'*63}\n\n"
FORMAT = sys.getfilesystemencoding()