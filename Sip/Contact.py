class Contact():
    def __init__(self):
        self.DisplayName = None
        self.Extension = None
        self.Domain = None

        #TODO Figure out what these are for
        #Only used in register and 300 replies
        self.Q = None
        self.Expires = None
    
    def Validate(self):
        if self.DisplayName != None:
            if not isinstance(self.DisplayName, str):
                return False
        
        if not isinstance(self.Extension, str):
            return False
        
        if self.Domain != None:
            if not isinstance(self.Domain, str):
                return False
        
        #Q and Expires
    
    def Assemble(self):
        '''if not self.Validate():
            return None'''

        contact = "Contact: "

        if self.DisplayName != None:
            contact += "\"" + self.DisplayName + "\" "
        
        contact += "<sip:" + self.Extension

        if self.Domain != None:
            contact += "@" + self.Domain
        
        contact += ">\r\n"
        #TODO include Q and Expires

        return contact