import smooth_fitting_genetic as GA

casses = []
class Point:
    def __init__( self , x  , y ):
        self.x = x
        self.y = y

"""
EX for the data :
casses =
[ 
    {
     'degree'  : 4,
     'points' : [ { x : 5 , y : 4 } , { x : 2 , y : 3 } ] 
    },
    {
     'degree'  : 10,
     'points' : [ { x : 14 , y : 7 } , { x : 4 , y : 6 } , { x : 5 , y : 2 } , { x : 2.1 , y : 3.1 }]
    }

]
"""


# ---------------------- get cases from the file  ---------------

file = open("input.txt", "r") 
numOfCases = int ( file.readline() )

for iCases in range(0 , numOfCases):
    numOfPoints = int ( file.readline() )
    degree = int( file.readline() )
    points = []
    for iPoint in range(0 , numOfPoints):
        p = file.readline()
        points.append( Point( int(p[0]) , int(p[1]) ))

    casses.append( { 'degree' : degree , 'points' : points })

# ------------------------------------------------------------------


# ------------- main ----------------

for  i , case in enumerate(casses):
    selectedChromosome = GA.select_chromosome(case['degree'] , case['points'])
    print('case %s :' % i)    
    for point in selectedChromosome:
        print( point.x , point.y )
    print('\n')