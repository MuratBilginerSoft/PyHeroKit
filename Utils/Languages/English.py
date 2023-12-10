# region JsonMessages

class Messages():


    menu = {

        "1":  {"process": "1. Text Upper"},
        "1.1": {"process": "1. Transaction with String"},
        "1.2": {"process": "2. Transaction with File (.txt)"},

        "C":  {"process": "Your Choice (1,2,3... Select & Enter): "},

        "L":  {"process": "L. Change Language Settings"},

        "L1": {"process": "1. English"},
        "L2": {"process": "2. Türkçe"},

        "LE": {"process": "Please Select An Language (1 or 2 & Enter): "},

        "E":  {"process": "Press Enter Key To Close"},

        "D":  {"process": "To Continue (D or d & Enter) or To Exit (Enter): "},

        "G": {"process": "To go back (G or g & Enter) - To close (Enter):"},

    }

    process = { 

        "1": {"message": "Enter Your String Expression To Convert: "},
        "2": {"message": "Enter Source File Path: "},
        "3": {"message": "Enter Target File Path: "},
    }

    system = {
        "1": {"message": "Please Select An Option: "},
        "2": {"message": "Invalid Selection..."},
        "3": {"message": "Process Completed..."},
        "4": {"message": "Language Is Set To English..."},
        "5": {"message": "Application Closed..."}
    }

    info = {

        "201": {"message": "Operation Successfully Performed"},

        "401": {"message": "You have not selected a file with the .txt extension..."},
        "402": {"message": "Operation Failed..."},
    }

# endregion