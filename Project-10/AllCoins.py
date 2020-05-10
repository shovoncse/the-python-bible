from random import choice
# Abstruct Class (Template for all this type class)
class Coin:
    def __init__(self, rare = False, clean = True, heads = True, **data):

        for key,val in data.items():
            setattr(self,key,val)
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads
    
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        
        if self.is_clean:
            self.color = self.clean_color
        else:
            self.value = self.rusty_color

    def flip(self):
        self.heads = choice([True, False])

    def __del__(self):
        print("Coin Spent!")


# Inheritence
# A class that inherite the features from abstruct class
class Pound(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thikness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)

a = Pound()


print(a.mass)