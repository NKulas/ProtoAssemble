from enum import Enum

class Method(Enum):
    Register = "REGISTER"
    Invite = "INVITE"
    Ack = "ACK"
    Bye = "BYE"
    Cancel = "CANCEL"
    Update = "UPDATE"
    Refer = "REFER"
    Prack = "PRACK"
    Subscribe ="SUBSCRIBE"
    Notify = "NOTIFY"
    Publish = "PUBLISH"
    Message = "MESSAGE"
    Info = "INFO"
    Options = "OPTIONS"

class ContentType(Enum):
    ApplicationSdp = "application/sdp"

class TransportType(Enum):
    Tcp = "TCP"
    Udp = "UDP"