from MidWare.PrintTerminal.PrintTerminal import PrintTerminal
from Utils.Languages.English import Messages as EngMessages
from Utils.Languages.Türkçe import Messages as TrMessages

class CreatePromt:

    def __init__(self):
        
        self.PrintTerminals = PrintTerminal()
        self.Messages = EngMessages()

        self.processes = self.Messages.process
        self.system = self.Messages.system
        self.menu = self.Messages.menu
        self.info = self.Messages.info

    def main(self, language, menu, count):
        
        self.changeLanguage(language)
        self.printPromt(menu, count)
        
    # region Change Language   
     
    def changeLanguage(self, language):

        if language == 'English':
            self.Messages = EngMessages()
        elif language == 'Türkçe':
            self.Messages = TrMessages()
        else:
            self.Messages = EngMessages()
        
        self.processes = self.Messages.process
        self.system = self.Messages.system
        self.menu = self.Messages.menu
        self.info = self.Messages.info
        
    # endregion

    # region Choice Process

    def printPromt(self, menu, count):

        print()

        for item in menu:

            if item["type"] == "Divider":
                print(item["color"] + item["text"] * int(count))
            elif item["type"] == "System":
                self.PrintTerminals.main(f"*   {self.system[str(item['text'])]['message']}", item["color"], count)
            elif item["type"] == "Menu":
                self.PrintTerminals.main(f"*   {self.menu[str(item['text'])]['process']}", item["color"], count)
            elif item["type"] == "Line":
                self.PrintTerminals.main(item["text"], item["color"], count)
            else:
                pass

        print()

    # endregion