# region Import Packages

from MidWare.BrainyKit.PrintTerminal.PrintTerminal import PrintTerminal
from MidWare.BrainyKit.Message.Message import Message

# endregion

# region PrintPromt Class

class PrintPromt:

    # region Init

    def __init__(self):

        # region Create Objects
        
        self.PrintTerminals = PrintTerminal()
        self.Messages = Message()
        
        # endregion
    
    # endregion
        
    # region Main

    def main(self, menu, count):

        _, system, menuMessage, _ = self.Messages.messageLanguage()

        print()

        for item in menu:

            if item["type"] == "Divider":
                print(item["color"] + item["text"] * int(count))
            elif item["type"] == "System":
                self.PrintTerminals.main(f"*   {system[str(item['text'])]['message']}", item["color"], count)
            elif item["type"] == "Menu":
                self.PrintTerminals.main(f"*   {menuMessage[str(item['text'])]['process']}", item["color"], count)
            elif item["type"] == "Line":
                self.PrintTerminals.main(item["text"], item["color"], count)
            else:
                pass

        print()

    # endregion 
    
# endregion