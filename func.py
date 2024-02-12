

class Task:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def changeName(self, newName):
        self.name = newName
    
    def changeValue(self):
        if self.value == False:
            self.value = True
        else:
            self.value = False

    
