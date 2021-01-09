from SipEnums import Method, ContentType, TransportType
from Via import Via
from From import From
from To import To
from Contact import Contact

class SipRequest():
    def __init__(self):
        self.Method = None
        self.FinalDestinationExtension = None
        self.FinalDestinationDomain = None
        self.Version = "SIP/2.0"

        self.Via = []

        self.From = From()
        self.To = To()
        self.Contact = Contact()

        self.CallId = None
        self.SequenceNumber = None
        self.MaxForwards = None
        self.UserAgent = None

        self.ContentType = None
        self.ContentLength = None
        self.Content = None
    
    def Validate(self):
        #Request line
        if not isinstance(self.Method, Method):
            return False

        if not isinstance(self.FinalDestinationExtension, str):
            return False
        
        if self.FinalDestinationDomain != None:
            if not isinstance(self.FinalDestinationDomain, str):
                return False
        
        if not isinstance(self.Version, str):
            return False
        
        #Vias
        for via in self.Via:
            if not via.Validate():
                return False
        
        #From
        if not self.From.Validate():
            return False

        if not self.To.Validate():
            return False
        
        #Contact
        if not self.Contact.Validate():
            return False
        
        return True

    def Assemble(self):
        packet = ""

        #Request line
        requestLine = self.Method.value + " sip:" + self.FinalDestinationExtension
        if self.FinalDestinationDomain != None:
            requestLine += "@" + self.FinalDestinationDomain
        requestLine += " " + self.Version + "/r/n"
        packet += requestLine

        #Via headers
        for via in self.Via:
           packet += via.Assemble() + "\r\n"
        
        #From header
        packet += self.From.Assemble()

        #To header
        packet += self.To.Assemble()

        #Contact header
        packet += self.Contact.Assemble()
        
        #Call id header
        packet += "Call-ID: " + self.CallId + "\r\n"
        #Cseq header
        packet += "CSeq: " + str(self.SequenceNumber) + " " + self.Method.value + "\r\n"

        #Content length header
        packet += "Content-Length: " + str(self.ContentLength) + "\r\n"
        #Max forewards header
        packet += "Max-Forwards: " + str(self.MaxForwards) + "\r\n"
        #Content type header
        packet += "Content-Type: " + self.ContentType.value + "\r\n"

        #User agent header
        if self.UserAgent != None:
            packet += "User-Agent: " + self.UserAgent + "\r\n"
        
        packet += "\r\n"

        return packet

    def Disassemble(self, packet):
        pass
        #Not implemented yet