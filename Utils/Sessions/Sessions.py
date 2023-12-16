# region Class Sessions

class Sessions:

    def __init__(self):
        pass

    language = "English"
    outputMethod = "Terminal"
    outputPath = "Assets"

    from Utils.Languages.English import Messages as EngMessages
    Messages = EngMessages()

    processes = Messages.process
    system = Messages.system
    menu = Messages.menu
    info = Messages.info

# endregion