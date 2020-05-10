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

# coin1 = Pound()
# coin1.color
# coin1.color = "Greenish"