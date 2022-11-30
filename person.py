class Person():
    def __init__(self, name, userName, password, wins = 0):
        self.name = name
        self.userName = userName
        self.password = password
        self.wins = wins

    def getName(self):
        return self.name

    def getUserName(self):
        return self.userName

    def getPassword(self):
        return self.password

    def setName(self, name):
        self.name = name
    
    def setUserName(self, userName):
        self.userName = userName
    
    def setPassword(self, password):
        self.password = password
