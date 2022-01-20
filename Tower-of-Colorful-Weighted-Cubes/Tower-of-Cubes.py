


from typing_extensions import Self


class Cube:
    def __init__(self, W , front, back , left , right , top , bottom) -> None:
        self.W = W
        self.sides = { 0: front , 1: back , 2: left , 3: right , 4: top , 5: bottom }
    
    def getOppositeSide(self, side):
        """find the color of the opposite side of the cube
            sides position as { 0: front , 1: back , 2: left , 3: right , 4: top , 5: bottom }
        Args:
            side (int): given side of the cube
        
        Returns:
            int : color of the opposite side
        """
        return self.sides[(side+1) if (side%2==0) else side - 1]
        