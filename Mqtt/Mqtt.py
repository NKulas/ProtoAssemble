from MqttEnums import Command
import math

class Mqtt():
    def __init__(self):
        self.Command = None
        self.Duplicate = False
        self.QualityOfService = None
        self.Retain = False

        self.RemainingLength = None
        #Variable length header

        self.Content = None
    
    def Validate(self):
        if not isinstance(self.Command, Command):
            return False
        
        if not isinstance(self.Duplicate, bool):
            return False
        
        if isinstance(self.QualityOfService, int):
            if not (self.QualityOfService >= 0 and self.QualityOfService <= 2):
                return False
        else:
            return False

        if not isinstance(self.Retain, bool):
            return False

    def Assemble(self):
        '''if not self.Validate():
            return None'''
        
        pdu = b''

        control = ConvertDecimalToBinary(int(self.Command), 4) + str(int(self.Duplicate)) + ConvertDecimalToBinary(self.QualityOfService, 2) + str(int(self.Retain))
        pdu += int(control, 2).to_bytes(1, byteorder="big")

        return pdu

    def Disassemble(self):
        pass

def ConvertDecimalToBinary(decimalNumber, minimumPlaces=0):
    places = 0
    continuePlaces = True
    while continuePlaces:
        if pow(2, places + 1) > decimalNumber:
            continuePlaces = False
        else:
            places += 1
    
    if places < minimumPlaces - 1:
        places = minimumPlaces - 1

    result = ""
    while places >= 0:
        factor = pow(2, places)

        result += str(math.floor(decimalNumber / factor))
        decimalNumber = decimalNumber % factor
        places -= 1
    
    return result