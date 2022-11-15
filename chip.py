class Chip():
    def __init__(self, location, color = None):
        self.location = location
        self.color = color

    def __str__(self):
        return f"Chip @ {(self.location)} that is {self.color}"
    
    def getLocation(self):
        return self.location

    def getColor(self):
        return self.color

    def setLocation(self, location):
        self.location = location

    def setColor(self, color):
        self.color = color
