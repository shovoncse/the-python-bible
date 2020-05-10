from random import choice
# Abstruct Class (Template for all this type class)
class Coin:
    def __init__(self, rare= False, clean = True):
        self.is_rare = rare
        self.is_clean = clean
    
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        
        if self.is_clean:
            self.color = self.clean_color
        else:
            self.value = self.rusty_color
        
    def __del__(self):
        print("Coin Spent!")




# A class that inherite the features from abstruct class
class Pound:

    def __init__(self,rare=False):
        self.value = 1.00
        self.color = "Golden"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True
        
        self.rare = rare
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
    
    def rust(self):
        self.color = "Greenish"
    
    def clean(self):
        self.color = "Gold"

    def flip(self):
        self.heads = choice([True, False])

    def __del__(self):
        print("Coin Spent")

# coin1 = Pound()
# coin1.color
# coin1.color = "Greenish"
a = Pound()
a.flip()
print(a.heads)
# destructed
del a
# not found
print(a.heads)
