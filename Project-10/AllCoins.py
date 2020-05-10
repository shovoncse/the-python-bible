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

    def rust(self):
        self.color = self.rusty_color
    
    def clean(self):
        self.color = self.clean_color

    def flip(self):
        self.heads = choice([True, False])

    def __str__(self):
        if self.original_value >= 1:
            return f"{int(self.original_value)} TK Coin"
        else:
            return f"{int(self.original_value*100)} Poisa Coin"

    def __del__(self):
        print("Coin Spent!")


# Inheritence
# A class that inherite the features from abstruct class
class OnePoisa(Coin):
    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_color": "silver",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thikness": 3.15,
            "mass": 0.05
        }
        super().__init__(**data)

class FivePoisa(Coin):
    def __init__(self):
        data = {
            "original_value": 0.05,
            "clean_color": "silver",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thikness": 3.15,
            "mass": 0.15
        }
        super().__init__(**data)

class TenPoisa(Coin):
    def __init__(self):
        data = {
            "original_value": 0.10,
            "clean_color": "silver",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thikness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)

class TwentyFivePoisa(Coin):
    def __init__(self):
        data = {
            "original_value": 0.25,
            "clean_color": "silver",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thikness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)


class FiftyPoisa(Coin):
    def __init__(self):
        data = {
            "original_value": 0.50,
            "clean_color": "silver",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thikness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)

# Polymorphism

class OneTaka(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
    self.color = self.clean

    self.color = self.clean

    self.color = self.clean
            "thikness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color
    
    def clean(self):
        self.color = self.clean_color

class TwoTaka(Coin):
    def __init__(self):
        data = {
            "original_value": 2.00,
            "clean_color": "silver",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thikness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color
    
    def clean(self):
        self.color = self.clean_color

class FiveTaka(Coin):
    def __init__(self):
        data = {
            "original_value": 5.00,
            "clean_color": "silver",
            "rusty_color": "greenish",
            "num_edges": 7,
            "diameter": 22.5,
            "thikness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color
    
    def clean(self):
        self.color = self.clean_color

coins = [OnePoisa(),FiftyPoisa(),FivePoisa(),TwentyFivePoisa(),OneTaka(),TwoTaka(),FiveTaka()]

for coin in coins:
    arguments = [coin, coin.value, coin.num_edges]
    print('{} - Value:{}, Edges:{}'.format(*arguments))