

class Room:
    
    #! magic method | dunder init | constructor
    def __init__(self, size, name,type):
        self.size = size
        self.name = name
        self.type = type
        self.objects = []
        
    def __repr__(self) -> str:
        return f"{self.name} | {self.type}"
    
    def info(self) -> None:
        """
        This function is going to print out all of the attributes of the class
        """
        print(f"name: {self.name}")
        print(f"size: {self.size}")
        print(f"type: {self.type}")
        
    
    def add_to_room(self, object):
        self.objects.append(object)
        print(f"object {object.name} added")
        return self
    
    def add_many_to_room(self, list_of_items):
        for item in list_of_items:
            self.objects.append(item)
        return self