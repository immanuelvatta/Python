

class Screen:
    def __init__(self, size, type):
        self.size = size
        self.is_on = False
        self.type = type

    def toggle_state(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True
        return self
    
class TV(Screen):
    
    def __init__(self, name, watt, size, type="LCD"):
        self.name = name
        self.watt = watt
        super().__init__(size, type)


class Monitor(Screen):
    
    def __init__(self, size, type, name):
        self.name = name
        super().__init__(size, type)
        
class Ultra_wide_monitor(Monitor):
    def __init__(self, size, type, name):
        super().__init__(size,type,name)
            