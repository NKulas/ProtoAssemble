class From():
    def __init__(self):
        self.DisplayName = None
        self.Extension = None
        self.Domain = None
        self.Tag = None
    
    def Validate(self):
        if self.DisplayName != None:
            if not isinstance(self.DisplayName, str):
                return False
        
        if not isinstance(self.Extension, str):
            return False
        
        if self.Domain != None:
            if not isinstance(self.Domain, str):
                return False
        
        if self.Tag != None:
            if not isinstance(self.Tag, str):
                return False
        
        return True
    
    def Assemble(self):
        '''if not self.Validate():
            return None'''
        
        frm = "From: "

        if self.DisplayName != None:
            frm += "\"" + self.DisplayName + "\" "
        
        frm += "<sip:" + self.Extension

        if self.Domain != None:
            frm += "@" + self.Domain
        
        frm += ">"

        if self.Tag != None:
            frm += ";tag=" + self.Tag
        
        frm += "\r\n"

        return frm