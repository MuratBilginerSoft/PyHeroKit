# region Import Packages

from colorama import init, Fore

# endregion

init(autoreset=True)

# region Menus Class

class Menus:

    # region Init

    def __init__(self):
        pass

    # endregion

    # region Start Menu Partial

    startMenuPartial = [

        {"type" : "Divider",  "text" : "*",  "color" : Fore.YELLOW},
        {"type" : "Line",     "text" : "*",  "color" : Fore.YELLOW},
        {"type" : "System",   "text" : "1",  "color" : Fore.YELLOW},
        {"type" : "Line",     "text" : "*",  "color" : Fore.YELLOW},

        

    ]

    # endregion

    # region End Menu Partial

    endMenuPartial = [
            
            {"type" : "Line",     "text" : "*",  "color" : Fore.YELLOW},
            {"type" : "Divider",  "text" : "*",  "color" : Fore.YELLOW}
    
    ]

    # endregion

    # region Language Menu
        
    languageMenu = [

        *startMenuPartial,

        {"type" : "Menu",     "text" : "L1", "color" : Fore.BLUE},
        {"type" : "Menu",     "text" : "L2", "color" : Fore.MAGENTA},
        {"type" : "Line",     "text" : "*",  "color" : Fore.YELLOW},
        {"type" : "Menu",     "text" : "E",  "color" : Fore.CYAN},
        
        *endMenuPartial
    
    ]

    # endregion

    # region Main Menu

    mainMenu = [

        *startMenuPartial,

        {"type" : "Menu",     "text" : "1", "color" : Fore.GREEN},
        {"type" : "Line",     "text" : "*",  "color" : Fore.YELLOW},

        {"type" : "Menu",     "text" : "L", "color" : Fore.CYAN},
        {"type" : "Line",     "text" : "*",  "color" : Fore.YELLOW},
        {"type" : "Menu",     "text" : "E",  "color" : Fore.CYAN},

        *endMenuPartial

        
    ]

    # endregion

    # region ProcessOne Detail Menu

    processOneDetail = [

        *startMenuPartial,

        {"type" : "Menu",     "text" : "1.1", "color" : Fore.GREEN},
        {"type" : "Menu",     "text" : "1.2", "color" : Fore.GREEN},
        {"type" : "Line",     "text" : "*",  "color" : Fore.YELLOW},
        {"type" : "Menu",     "text" : "G", "color" : Fore.GREEN},

        *endMenuPartial

    ]

    # endregion

# endregion


