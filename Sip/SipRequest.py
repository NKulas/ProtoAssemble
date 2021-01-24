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
        self.Allow = []
        self.Subject = None
        self.Expires = None

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

        #Call id
        if not isinstance(self.CallId, str):
            return False
        
        #Sequence
        if not isinstance(self.SequenceNumber, int):
            return False
        
        #Max forwards
        if not isinstance(self.MaxForwards, int):
            return False

        if not (self.MaxForwards >= 0 and self.MaxForwards <= 255):
            return False
        
        #User agent
        if self.UserAgent != None:
            if not isinstance(self.UserAgent, str):
                return False
        
        #Allow
        if len(self.Allow) > 0:
            for method in self.Allow:
                if not isinstance(method, Method):
                    return False
        
        #Subject
        if self.Subject != None:
            if not isinstance(self.Subject, str):
                return False
        
        #Expires
        if self.Expires != None:
            if not isinstance(self.Expires, int):
                return False
            
            if not (self.Expires >= 0 and self.Expires <= (pow(2, 32)-1)):
                return False
        
        #Content
        if (self.Content != None):
            if self.ContentLength != len(self.Content):
                return False
        else:
            if self.ContentLength != 0:
                return False

        return True

    def Assemble(self):
        pdu = ""

        #Request line
        requestLine = self.Method.value + " sip:" + self.FinalDestinationExtension
        if self.FinalDestinationDomain != None:
            requestLine += "@" + self.FinalDestinationDomain
        requestLine += " " + self.Version + "\r\n"
        pdu += requestLine

        #Via headers
        for via in self.Via:
           pdu += via.Assemble()
        
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

        #Max forwards header
        pdu += "Max-Forwards: " + str(self.MaxForwards) + "\r\n"

        #User agent header
        if self.UserAgent != None:
            pdu += "User-Agent: " + self.UserAgent + "\r\n"

        #Allow header
        if len(self.Allow) > 0:
            allow = "Allow: "
            first = True

            for method in self.Allow:
                if first:
                    first = False
                else:
                    allow += ", "
                allow += method.value
            pdu += allow + "\r\n"
        
        #Subject header
        if self.Subject != None:
            pdu += "Subject: " + self.Subject + "\r\n"

        #Expires header
        if self.Expires != None:
            pdu += "Expires: " + str(self.Expires) + "\r\n"

        #Content length header
        pdu += "Content-Length: " + str(self.ContentLength) + "\r\n"
        
        #Content type header
        pdu += "Content-Type: " + self.ContentType.value + "\r\n"
        
        pdu += "\r\n"
        
        if self.Content != None:
            pdu += self.Content

        return pdu

    def Disassemble(self, pdu):
        head, body = pdu.split("\r\n\r\n")
        self.Content = body

        requestLine = True
        for header in head.split("\r\n"):
            if requestLine:
                self.Method, uri, self.Version = header.split(" ")
                uri = uri.strip("sip:")

                if "@" in uri:
                    self.FinalDestinationExtension, self.FinalDestinationDomain = uri.split("@")
                else:
                    self.FinalDestinationExtension = uri
                
                requestLine = False
            else:
                key, value = header.split(":", 1)
                key = str.strip(key)
                value = str.strip(value)
                #Implementation not completed