class Tree:
    def __init__(self, nodeValue, children = []):
        self.nodeValue = nodeValue
        self.children = children

    def getNodeValue(self):
        return self.nodeValue

    def setNodeValue(self, nodeValue):
        self.nodeValue = nodeValue
    
    def addChild(self, child):
        self.children.append(child)

    def addChildren(self, children):
        self.children.extend(children)

    def removeChild(self, childIndex):
        self.children.pop(childIndex)
