import string

class WakOnLan():
    def __init__(self):
        self.MacAddress = None
        #self.Password = None
    
    def Validate(self):
        if not isinstance(self.MacAddress, str):
            return False
        
        newMac = ""

        for char in self.MacAddress:
            if char in string.hexdigits:
                newMac += char
        
        if len(newMac) != 12:
            return False
        
        self.MacAddress = newMac
        return True
    
    def Assemble(self):
        if not self.Validate():
            return None
        
        pdu = b''
        i = 0
        while i < 6:
            pdu += bytes.fromhex("FF")
            i += 1
        
        j = 0
        while j < (16):
            pdu += bytes.fromhex(self.MacAddress)
            j += 1
        
        return pdu
    
    def Dissasemble(self, pdu):
        pass
    #Not implemented yet