import json

class FileWrite:


    def __init__(self) -> None:
        pass

    def main(self, filePath, data):

        pass
    
    def writeJson(self, filePath, key, value):

        with open(filePath, 'r+', encoding='utf-8') as file:
            
            data = json.load(file)
            data[str(key)] = value  
            file.seek(0) 
            json.dump(data, file, indent=4, ensure_ascii=False)  
            file.truncate()