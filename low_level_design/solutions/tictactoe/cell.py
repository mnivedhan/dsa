from low_level_design.solutions.tictactoe.symbol import Symbol

class Cell:
    def __init__(self):
        self.symbol = Symbol.EMPTY
    
    def get_symbol(self):
        return self.symbol
    
    def set_symbol(self, symbol: Symbol):
        self.symbol = symbol