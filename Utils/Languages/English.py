# region JsonMessages

class Messages():


    menu = {

        "1":  {"process": "1. Text Upper"},
        "1.1": {"process": "1. Transaction with String"},
        "1.2": {"process": "2. Transaction with File (.txt)"},

        "2": {"process": "2. Read Txt File Content"},
        "3": {"process": "3. Find String Character Count"},
        "4": {"process": "4. Show Folder Content"},
        "5": {"process": "5. Delete Files With The Extension In The Folder"},
        "6": {"process": "6. Delete Subfolders In The Folder"},
        "7": {"process": "7. Change File Extension In The Folder"},

        "C":  {"process": "Your Choice (1,2,3... Select & Enter): "},

        "L":  {"process": "L. Change Language Settings"},
        "O": {"process": "O. Change Output Method Settings"},

        "L1": {"process": "1. English"},
        "L2": {"process": "2. Türkçe"},

        "O1": {"process": "1. Terminal"},
        "O2": {"process": "2. File"},

        "LE": {"process": "Please Select An Language (1 or 2 & Enter): "},
        "OE": {"process": "Please Select An Output Method (1 or 2 & Enter): "},

        "E":  {"process": "Press Enter Key To Close"},

        "D":  {"process": "Home (A or a) - Same Operation (D or d & Enter) -  Close (Enter):"},

        "G": {"process": "To go back (G or g & Enter) - To close (Enter):"},

        "S": {"process": "Your Files Above Will Be Affected by Deletion Do You Want to Continue (E or e & Enter): "},

    }

    process = { 

        "1": {"message": "Enter Your String Expression To Convert: "},
        "2": {"message": "Enter Source File Path: "},
        "3": {"message": "Enter Target File Path: "},
        "4": {"message": "Enter your String Expression: "},
        "5": {"message": "Enter Folder Path(C:\\Users\\UserName\\Masaüstü gibi): "},
        "6": {"message": "Enter File Extension(png etc.): "},
        "7": {"message": "Enter Folder Name To Delete: "},
        "8": {"message": "Enter File Extension To Change(webp etc.): "},
        "9": {"message": "Enter New File Extension(png etc.): "},
        "10": {"message": "Should Subfolders Be Affected? (Y/N): "},
    }

    system = {
        "1": {"message": "Please Select An Option: "},
        "2": {"message": "Invalid Selection..."},
        "3": {"message": "Process Completed..."},
        "4": {"message": "Language Is Set To English..."},
        "5": {"message": "Application Closed..."},
        "6": {"message": "Output Method"},
        "7": {"message": "Language"},
        "8": {"message": "Character Count: "},
        "9": {"message": "Letter Count: "},
        "10": {"message": "Space Count: "},
        "11": {"message": "Punctuation Count: "},
        "12" : {"message": "Folder Count: "},
        "13" : {"message": "File Count: "},
        "14": {"message": "File Type: "},
        "15": {"message": "File Type Count: "},
        "16": {"message": "Deleted File List: "},
        "17": {"message": "File List to Delete: "},
        "18": {"message": "Folder List to Delete: "},
        "19": {"message": "Deleted Folder List: "},
        "20": {"message": "Folder Count: "},
        "21": {"message": "To Be Affected File List: "},
        "22": {"message": "Affected Folder List: "},
        
    }

    info = {

        "201": {"message": "Operation Successfully Performed"},
        "202": {"message": "File Read"},
        "203": {"message": "File Created"},
        "204": {"message": "File Deleted"},
        "205": {"message": "Folder Deleted"},

        "301": {"message": "Operation Is Continuing Please Wait..."},
        "302": {"message": "Progress: "},

        "401": {"message": "You have not selected a file with the .txt extension..."},
        "402": {"message": "Operation Failed..."},
        "403": {"message": "The File Does Not Exist..."},
        "404": {"message": "The Folder Does Not Exist..."},
        "405": {"message": "The Entered Path Is Not A Folder..."},
        "406": {"message": "Operation Aborted..."},

        "501": {"message": "Scanning File: "},
        "502": {"message": "Scanning Folder: "},
    }

# endregion