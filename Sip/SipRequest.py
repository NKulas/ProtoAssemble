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
        pdu = ""

        #Request line
        requestLine = self.Method.value + " sip:" + self.FinalDestinationExtension
        if self.FinalDestinationDomain != None:
            requestLine += "@" + self.FinalDestinationDomain
        requestLine += " " + self.Version + "/r/n"
        pdu += requestLine

        #Via headers
        for via in self.Via:
           pdu += via.Assemble() + "\r\n"
        
        #From header
        pdu += self.From.Assemble()

        #To header
        pdu += self.To.Assemble()

        #Contact header
        pdu += self.Contact.Assemble()
        
        #Call id header
        pdu += "Call-ID: " + self.CallId + "\r\n"
        #Cseq header
        pdu += "CSeq: " + str(self.SequenceNumber) + " " + self.Method.value + "\r\n"

        #Content length header
        pdu += "Content-Length: " + str(self.ContentLength) + "\r\n"
        #Max forewards header
        pdu += "Max-Forwards: " + str(self.MaxForwards) + "\r\n"
        #Content type header
        pdu += "Content-Type: " + self.ContentType.value + "\r\n"

        #User agent header
        if self.UserAgent != None:
            pdu += "User-Agent: " + self.UserAgent + "\r\n"
        
        pdu += "\r\n"

        return pdu

    def Disassemble(self, pdu):
        pass
        #Not implemented yet