class Square:
    
    def __init__(self,length):
        self.side_length = length
        
    @staticmethod
    def square_area(length):
        return length*length
    
    @classmethod
    def square_from_area(cls,area):
        return cls(area ** 0.5)
        
    def print(self):
        print("Side length = ", self.side_length)
        print("Area of the square = ", Square.square_area(self.side_length))
        
        
        
sq = Square.square_from_area(25)

sq.print()