from colorama import init, Fore, Style

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

    def normalPrint(self, message, color=Fore.RESET):

        print("\n")
        print(color + str(message))
    
    # endregion