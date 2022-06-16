import os
import requests
import time
import time

from genericExceptions import NotImplementedException, InvalidTypeException
from defaultFormats import*
from mainMenu import*


title = "\n"*10+f"{'    '*10}{title}".replace("█", f"{C.CYAN}█").replace('╚', f'{C.RED}╚').replace('║', f'{C.RED}║').replace('╔', f'{C.RED}╔').replace('═', f'{C.RED}═').replace('╗', f'{C.RED}╗').replace('╝', f'{C.RED}╝')

# All the functions used
def clear_screen() -> None: os.system("cls" if os.name == "nt" else "clear")
def print_err(err: str) -> None:
    """ Prints generic error messages"""

    clear_screen()
    print(f"{C.GREEN} [!] {C.RED}The following error occured {C.YELLOW}'{err}'")
    time.sleep(2.5)
    clear_screen()
def set_title(title: str) -> None:
    """ set the console window's title"""
    if os.name == "nt":
        os.system(f"title {title}")
    else:
        print(f'"\033]0;{title}\007" "$1"')
        clear_screen()
def play_beep() -> bool:
    """ Plays a beeping noise to get attention of user when the set min and max crypto price has been reached """
    try:
        if os.name == "nt": # is a window's operating system
            import winsound
            frequency = 2000
            duration = 690
            winsound.Beep(frequency, duration)
        else: # unix or mac operating system
            import pygame
            pygame.init()
            pygame.mixer.init()
            for _ in range(10):
                sounda= pygame.mixer.Sound("beepNoise.wav")
                sounda.play()
        return True
    except Exception as err:
        print_err(f"when trying to play the beep -> {err}") # not advanced, but otherwise, use the logging decorator
        return False
def track_crypto(crypto_name: str, max_price: int = 0, min_price: int = 0) -> None:
    """ Tracks the crypto from binance of a given crypto name"""
    set_title(f"Crypto price tracker  Current price of {crypto_name}: ")
    while True:
        try:
            crypto = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto_name}"
            crypto_data = requests.get(url=crypto, timeout=3) 
            crypto_json = crypto_data.json()

            if "Invalid symbol" in str(crypto_json):
                print(f"{C.GREEN} [!] {C.RED}The crypto name: {C.YELLOW}'{crypto_name}' {C.RED}was invalid for binance's API")
                time.sleep(2.5)
                return
            
            crypto_price: float = float(crypto_json['price'])
            clear_screen()
            print(f"{C.RED} [+] {C.GREEN}The price of one {crypto_name} is: {C.YELLOW}${crypto_price:,.2f}")

            if ( (int(crypto_price) >= max_price or int(crypto_price) <= min_price) and (min_price != 0 and max_price != 0) ):
                print(f"{C.GREEN} [!] {C.RED} A crypto minimum or maximum price was met ! ")
                play_beep()
                time.sleep(5)

            time.sleep(1)
            clear_screen()

    
        except TimeoutError as err:
            clear_screen()
            print_err(f"When trying to track crypto {crypto_name} request timed out , API may be down...  ")
            print(f"retrying...")
            time.sleep(1.5)

        except Exception as err:
            print_err(f"In track_crypto for crypto {crypto_name} -> {err}") # reccommended to use logging decorator, but you said not advanced so wtv
            print(f"retrying...")
            time.sleep(1.5)

def print_menu(menu: list) -> None:
    """ Prints the menu from a given list """
    try:
        if type(menu) != list:
            raise InvalidTypeException
        clear_screen()
        print(f"{title}")
        print(f"{LINE}\n")
        for element in menu:
            print(f"{'  '*10}{C.RED} [{element[0]}] {C.GREEN} {element[1]} / {C.YELLOW}{element[-1]}")
        print(f"{LINE}\n")
    except Exception as err:
        err = f"In print_menu -> {err}"
        print_err(err)
        logging.ERROR(err)
def main() -> None:
    """ Runs all the functions and asks for user input"""
    while True:
        try:
            clear_screen()
            print(f"{C.RED} [+] {C.GREEN}Choose one of the following cryptos to view price")

            print_menu(menu)

            crypto_option = int(input("Enter a number: ").strip().rstrip())
            if crypto_option not in range(1, len(menu)):
                raise NotImplementedException

            clear_screen()
            print(f"{C.RED} [+] {C.GREEN} Enter the MAXIMUM price alert for the crypto in USD denomination, 0 for none: ")
            max_price: int = int(input("[+] ").strip().rstrip())

            clear_screen()
            print(f"{C.RED} [+] {C.GREEN} Enter the MINIMUM price alert for the crypto in USD denomination, 0 for none: ")
            min_price: int = int(input("[+] ").strip().rstrip())

            track_crypto(crypto_name=f"{menu[crypto_option-1][-1]}USDT", max_price=max_price, min_price=min_price)

            return
        except Exception as err:
            clear_screen()
            print(f"{err}")
            print(f"Invalid Option '{crypto_option}' ! Please choose one of the choices above...")
            time.sleep(2.5)
if __name__ == "__main__":
    main()
