# region Import Packages

import sys

from Promt.Starter.PrintPromt.PrintPromt import PrintPromt

from Promt.Process.FileTypeCounterPromt.FileTypeCounterPromt import FileTypeCounterPromt
from Promt.Process.DeleteExtFilePromt.DeleteExtFilePromt import DeleteExtFilePromt

from Promt.Process.TextCounterPromt.TextCounterPromt import TextCounterPromt
from Promt.Process.TextUpperPromt.TextUpperPromt import TextUpperPromt
from Promt.Process.TxtReaderPromt.TxtReaderPromt import TxtReaderPromt
from Promt.Process.ContinuePromt.ContinuePromt import ContinuePromt

from MidWare.BrainyKit.PrintTerminal.PrintTerminal import PrintTerminal
from MidWare.BrainyKit.Message.Message import Message

from MidWare.Routes.Menu.Menu import Menu

from MidWare.Settings.OutputMethod.OutputMethod import OutputMethod
from MidWare.Settings.Language.Language import Language

from colorama import init, Fore

init(autoreset=True)

# endregion

# region RunPromt Class

class RunPromt:

    # region DocString

    """
    
    """

    # endregion

    # region Init

    def __init__(self) -> None:

        # region Create Objects

        self.FileTypeCounterPromts = FileTypeCounterPromt()
        self.DeleteExtFilePromts = DeleteExtFilePromt()
        self.TextCounterPromts = TextCounterPromt()
        self.TextUpperPromts = TextUpperPromt()
        self.TxtReaderPromts = TxtReaderPromt()
        self.ContinuePromts = ContinuePromt()

        self.PrintTerminals = PrintTerminal()
        self.OutputMethods = OutputMethod()
        self.PrintPromts = PrintPromt()
        self.Languages = Language()
        self.Messages = Message()
        self.Menus = Menu()

        # endregion

        # region Variables

        self.processes = None 
        self.system = None
        self.menu = None 
        self.info = None

        # endregion
        
    # endregion

    # region Main

    def main(self):
        
        self.MessageLanguage()
        choice = self.choiceProcess()
        self.run(choice)

    # endregion
 
    # region Choice Process

    def choiceProcess(self):

        self.PrintPromts.main(self.Menus.mainMenu, 80)

        choice = input(f"{Fore.YELLOW}{self.menu['C']['process']} ")

        return choice

    # endregion

    # region Process

    def run(self, choice):

        # region Text Upper

        if choice == '1':
            self.TextUpperPromts.main()
        
        # endregion
            
        # region Text Reader
        
        elif choice == '2':
            self.TxtReaderPromts.main()
        
        # endregion
        
        # region Text Counter
            
        elif choice == '3':
            self.TextCounterPromts.main()  
        
        # endregion
            
        # region File Type Counter
            
        elif choice == '4':
            self.FileTypeCounterPromts.main()
        
        # endregion
            
        # region Delete Ext File
            
        elif choice == '5':

            self.DeleteExtFilePromts.main()
        
        # endregion

        # region Change Language
            
        elif choice == 'L' or choice == 'l':

            self.Languages.main()
            self.main()
        
        # endregion
        
        # region Change Output Method
            
        elif choice == 'O' or choice == 'o':

            self.OutputMethods.main()
            self.main()
        
        # endregion
            
        # region Exit
            
        else:
            self.PrintTerminals.normalPrint(f"{self.system['5']['message']} ", Fore.RED)
            sys.exit()
        
        # endregion
        
        # region Continue Process
            
        self.ContinuePromts.main(choice)
        
        # endregion

    # endregion

    # region Message Language    
    
    def MessageLanguage(self):

        self.processes, self.system, self.menu, self.info = self.Messages.messageLanguage()
    
    # endregion
   
# endregion