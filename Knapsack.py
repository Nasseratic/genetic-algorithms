file = open("input.txt", "r") 

casses = []
class Individul:
    'Individul object'
    def __init__( self , weight  , benefit ):
        self.weight = weight
        self.benefit = benefit

"""
EX for the data :
casses =
[ 
    {
     'size'  : 10,
     'items' : [ { weight : 5 , benefit : 4 } , { weight : 2 , benefit : 3 } ] 
    },
    {
     'size'  : 20,
     'items' : [ { weight : 5 , benefit : 4 } , { weight : 5 , benefit : 10 } , { weight : 8 , benefit : 20 } ]
    }

]
"""



numOfCases = int ( file.readline() )
for iCases in range(0 , numOfCases):

    numOfItems = int ( file.readline() )
    size = int( file.readline() )
    items =[]

    for iItem in range(0 , numOfItems):
        p = file.readline()
        p = p.split(' ')
        items.append( Individul( int(p[0]) , int(p[1]) ))

    casses.append( { 'size' : size , 'items' : items })

    # to ignore extra end lines
    file.readline()
    file.readline()
