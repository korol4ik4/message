from message import Message

class MoreArguments:
    def __init__(self,*args, **kwargs):
        vars = Message(**kwargs)
        self.name = vars.name
        self.wеight = vars.wеight
        self.color = vars.color
        self.size = vars.size
        self.price = vars.price

    def print_v(self):
        for k,v in self.__dict__.items():
            print(f"{k} = {v}")

ma = MoreArguments(name="John", wеight=250, color="white",size="small")
ma.print_v()

