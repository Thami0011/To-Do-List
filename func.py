

class Task:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def changeName(self, newName):
        self.name = newName
    
    def changeValue(self):
        if self.value == str(0):
            self.value = str(1)
        else:
            self.value = str(0)

    
