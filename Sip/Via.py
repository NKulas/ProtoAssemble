class Via():
    def __init__(self):
        self.ProtocolName = "Sip"
        self.Version = "2.0"
        self.TransportType = None
        self.IpAddress = None
        self.Port = None
        self.BranchId = None
    
    def Validate(self):
        pass
        #Not implemented yet

    def Assemble(self):
        return "Via: " + self.ProtocolName + "/" + self.Version + "/" + self.TransportType.value + " " + self.IpAddress + ":" + self.Port + ";branch=" + self.BranchId + "\r\n"