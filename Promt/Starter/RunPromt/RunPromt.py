# region Import Packages

import sys
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

        from Promt.Starter.PrintPromt.PrintPromt import PrintPromt
        from MidWare.Routes.Menu.Menu import Menu

        PrintPromt().main(Menu().mainMenu, 80)

        choice = input(f"{Fore.YELLOW}{self.menu['C']['process']} ")

        return choice

    # endregion

    # region Process

    def run(self, choice):

        # region Text Upper

        if choice == '1':

            from Promt.Process.TextUpperPromt.TextUpperPromt import TextUpperPromt
            TextUpperPromt().main()
        
        # endregion
            
        # region Text Reader
        
        elif choice == '2':

            from Promt.Process.TxtReaderPromt.TxtReaderPromt import TxtReaderPromt
            TxtReaderPromt().main()
        
        # endregion
        
        # region Text Counter
            
        elif choice == '3':

            from Promt.Process.TextCounterPromt.TextCounterPromt import TextCounterPromt
            TextCounterPromt().main()  
        
        # endregion
            
        # region File Type Counter
            
        elif choice == '4':

            from Promt.Process.FileTypeCounterPromt.FileTypeCounterPromt import FileTypeCounterPromt
            FileTypeCounterPromt().main()
        
        # endregion
            
        # region Delete Ext File
            
        elif choice == '5':

            from Promt.Process.DeleteExtFilePromt.DeleteExtFilePromt import DeleteExtFilePromt
            DeleteExtFilePromt().main()
        
        # endregion
            

        # region Delete Subfolder
            
        elif choice == '6':

            from Promt.Process.DeleteSubfolderPromt.DeleteSubfolderPromt import DeleteSubfolderPromt
            DeleteSubfolderPromt().main()
        
        # endregion

        # region Change Language
            
        elif choice == 'L' or choice == 'l':
            
            from MidWare.Settings.Language.Language import Language
            Language().main()
            self.main()
        
        # endregion
        
        # region Change Output Method
            
        elif choice == 'O' or choice == 'o':

            from MidWare.Settings.OutputMethod.OutputMethod import OutputMethod
            OutputMethod().main()
            self.main()
        
        # endregion
            
        # region Exit
            
        else:

            from MidWare.BrainyKit.PrintTerminal.PrintTerminal import PrintTerminal
            PrintTerminal().normalPrint(f"{self.system['5']['message']} ", Fore.RED)
            sys.exit()
        
        # endregion
        
        # region Continue Process
        from Promt.Process.ContinuePromt.ContinuePromt import ContinuePromt 
        ContinuePromt().main(choice)
        
        # endregion

    # endregion

    # region Message Language    
    
    def MessageLanguage(self):
        
        from MidWare.BrainyKit.Message.Message import Message
        self.processes, self.system, self.menu, self.info = Message().messageLanguage()
    
    # endregion
   
# endregion