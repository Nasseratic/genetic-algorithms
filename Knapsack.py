import knapsack_genetic_algorithm as GA

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


# ---------------------- get cases from the file  ---------------

file = open("input.txt", "r") 
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
# ------------------------------------------------------------------


# ------------- main ----------------

for  i , case in enumerate(casses):
    selectedChromosome = GA.select_chromosome(case['size'] , case['items'])
    result = GA.chromosome_to_items(case['items'] , selectedChromosome)
    print('case %s :' % i)    
    print('Total benefit %s'% (GA.get_total_benefit(result)))
    for item in result:
        print( item.weight , item.benefit )
    print('\n')