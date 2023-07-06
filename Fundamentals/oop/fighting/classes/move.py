class Move:
    
    def __init__(self, name, damage_modifier):
        self.name = name
        self.damage_modifier = damage_modifier

    def __repr__(self) -> str:
        return self.name