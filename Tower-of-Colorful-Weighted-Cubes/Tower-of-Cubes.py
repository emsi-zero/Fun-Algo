



class Cube:
    def __init__(self, W , front, back , left , right , top , bottom) -> None:
        """initiates a Cube object with given parameters   

        Args:
            W ([int]): wight of the cube
            front ([int]): color of front side
            back ([int]): color of back side
            left ([int]): color of left side
            right ([int]): color of right side
            top ([int]): color of top side
            bottom ([int]): color of bottom side
        """
        self.W = W
        self.sides = { 0: front , 1: back , 2: left , 3: right , 4: top , 5: bottom }
    
    
    def getSideColor(self , side):
        """get the color of the given side

        Args:
            side (int): index of the given side
            
        Returns:
            int : color of the given side
        """
        return self.sides[side]
    
    def getOppositeSide(self, side):
        """find the color of the opposite side of the cube
            sides position as { 0: front , 1: back , 2: left , 3: right , 4: top , 5: bottom }
        Args:
            side (int): given side of the cube
        
        Returns:
            int : color of the opposite side
        """
        return self.sides[(side+1) if (side%2==0) else side - 1] 
    
    def getWeight(self):
        """get weight of the cube

        Returns:
            int: weight of the cube
        """
        return self.W
    
    
    def __str__(self) -> str:
        return str(self.W)    


def sortBlocksbyWeight(blocks):
    return sorted(blocks , key=lambda b: b.getWeight())



cubes = []

numberOfBlocks = (int)(input())

for i in range(0,numberOfBlocks):
    inputStr = list(map(int , input().split()))
    cubes.append(Cube(inputStr[0], inputStr[1] ,inputStr[2] ,inputStr[3] ,inputStr[4] ,inputStr[5], inputStr[6]))
    
cubes = sortBlocksbyWeight(cubes)

#A dynamic programming table to record the highest possible tower with n blocks and space for recording the optimal choice for each step
T = [[[0]*3]*6]*numberOfBlocks
for i in range(0,numberOfBlocks):
    for j in range(0,6):
        T[i][j][0] = 1  

print(T)
#Maximum tower: max height, best starting block, best starting side
hmax = [0]*3


#fill the table for blocks and sides from the bottom block to the top for a tower of height i.
# And recording the Optimal step(top block) for each pair of blocks.

# check from cube 2 to n. 
# cube 1 is the lightest so the best possible solution is already 1.
for i in range(1,numberOfBlocks):
    # topside of cube i
    for ai in range(0,6):
        # check for cube above
        for j in reversed(range(i-1, 0)):
            # top side of cube j
            for aj in range(0,6):
                pass