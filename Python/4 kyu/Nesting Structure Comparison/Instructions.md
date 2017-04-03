# 4 kyu

Complete the method (or function in Python) to return true when its argument is an array that has the same nesting structure as the first array.

For example:

    # should return True
    same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
    same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

    # should return False 
    same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
    same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

    # should return True
    same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

    # should return False
    same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

For your convenience, there is already a function 'isArray(o)' declared in the JS version that returns true if its argument is an array, false otherwise.
