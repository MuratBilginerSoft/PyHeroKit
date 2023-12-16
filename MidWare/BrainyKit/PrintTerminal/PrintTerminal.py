# region Import Packages
import time
from colorama import init, Fore

init(autoreset=True)

# endregion

# region PrintTerminal Class

class PrintTerminal:

    # region DocString

    """

    This module, PrintTerminal, is responsible for handling the terminal printing operations of the application.

    It provides functions to print messages to the terminal in a formatted and structured manner. This includes printing menu options, user prompts, and other information.

    Main Function Parameters:
    
        message (str): The message to be printed. The message is left-justified and padded to a length of 50 characters.
        
        color (Fore): The color of the message. Defaults to Fore.RESET.

    Usage:
        import PrintTerminal
        PrintTerminal.main("Hello, World!", Fore.RED)

    """
    # endregion

    # region Init

    def __init__(self):
        pass

    # endregion

    # region Main

    def main(self, message, color=Fore.RESET, count=0):

        message = message.ljust(count)
        message = message[:count-1] + '*' + message[count:]
        print(color + message)
    
    # endregion
        
    # region Normal Print

    def normalPrint(self, message, color=Fore.RESET):

        print("\n")
        print(color + str(message))
    
    # endregion
    
    # region Same Line Print
        
    def sameLinePrint(self, message, color=Fore.RESET):
        
        print(f"\r{color}{str(message)}", end="")
        time.sleep(0.1)

    # endregion
        
    def progressPrint(self, count, color=Fore.RESET):
        
        print("\r" + " " * 200, end="")
        print(f"\r{color}Progress: {count}%", end="")
        time.sleep(0.1)
        
# endregion