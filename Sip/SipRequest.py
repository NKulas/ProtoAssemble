from SipEnums import Method, ContentType, TransportType
from Via import Via

class SipRequest():
    def __init__(self):
        self.Method = None
        self.Version = "SIP/2.0"

        self.ToAddress = None
        self.ToName = None
        self.ToTag = None

        self.FromAddress = None
        self.FromName = None
        self.FromTag = None

        self.Via = []

        self.CallId = None
        self.SequenceNumber = None
        self.MaxForwards = None
        self.UserAgent = None

        self.ContentType = None
        self.ContentLength = None
        self.Content = None
    
    def Validate(self):
        pass
        #Not implemented yet

    def Assemble(self):
        packet = self.Method.value + " sip:" + self.ToAddress + " " + self.Version + "\r\n"

        #can't use from as the variable name because it is reserved
        frm = "From: "
        if self.FromName != None:
            frm += "\"" + self.FromName + "\" "
        frm += "<sip:" + self.FromAddress + ">"
        if self.FromTag != None:
            frm += ";tag=" + self.FromTag
        packet += frm + "\r\n"
        
        to = "To: "
        if self.ToName != None:
            to += "\"" + self.ToName + "\" "
        to += "<sip:" + self.ToAddress + ">"
        if self.ToTag != None:
            to += ";tag=" + self.ToTag
        packet += to + "\r\n"

        packet += "Call-ID: " + self.CallId + "\r\n"
        packet += "CSeq: " + str(self.SequenceNumber) + " " + self.Method.value + "\r\n"

        for via in self.Via:
           packet += via.Assemble() + "\r\n"

        packet += "Content-Length: " + str(self.ContentLength) + "\r\n"
        packet += "Max-Forwards: " + str(self.MaxForwards) + "\r\n"
        packet += "Content-Type: " + self.ContentType.value + "\r\n"

        if self.UserAgent != None:
            packet += "User-Agent: " + self.UserAgent + "\r\n"
        
        packet += "\r\n"

        return packet

    def Disassemble(self, packet):
        pass
        #Not implemented yet