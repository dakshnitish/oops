class Patient:
    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):        
        self.name = name

    def getName(self):
        return self.name    

    def setSSN(self,ssn):
        self.ssn = ssn

    def getSSN(self):
        return self.ssn  

p=Patient()
p.setId(1234)
p.setName('nitish')
p.setSSN('123abc3')
print(p.getId())              
print(p.getName())