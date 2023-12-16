# region Import Packages

import os

# endregion

# region FolderControl Class

class FolderControl:

    # region Init

    def __init__(self) -> None:
        pass

    # endregion

    # region Main

    def main(self, folderPath: str):

        if not os.path.exists(folderPath):
            return 404
        
        if not os.path.isdir(folderPath):
            return 405
        
        return 200
    
    # endregion

# endregion