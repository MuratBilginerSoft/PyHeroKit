# region Import Packages

import sys

# endregion

# region Exit Class

class Exit:

    # region Init

    def __init__(self):
        pass

    # endregion

    # region Main

    def main(self, choice):

        # region GoBack
                
        if choice == 'G' or choice == 'g':
            from Promt.Starter.RunPromt.RunPromt import RunPromt
            userPromt = RunPromt()
            userPromt.main()
        
        # endregion
            
        # region Exit

        elif choice == '':
            sys.exit()

        # endregion
    
    # endregion

# endregion