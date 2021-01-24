import string

class WakeOnLan():
    def __init__(self):
        self.MacAddress = None
        self.Password = None
    
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

        if self.Password != None:
            if not isinstance(self.Password, str):
                return False

            if not (len(self.Password) == 8 or len(self.Password) == 12):
                return False
        
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
        
        if self.Password != None:
            pdu += bytes.fromhex(self.Password)
        
        return pdu
    
    def Dissasemble(self, pdu):
        macBytes = bytearray()
        i = 6
        while i < 12:
            macBytes.append(pdu[i])
            i += 1
        self.MacAddress = macBytes.hex()

        passwordBytes = bytearray()
        j = 102
        while j < len(pdu):
            passwordBytes.append(pdu[j])
            j += 1
        if (len(passwordBytes) > 0):
            self.Password = passwordBytes.hex()