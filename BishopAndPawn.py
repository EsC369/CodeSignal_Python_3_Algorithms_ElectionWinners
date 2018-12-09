"""
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement.
"""

def bishopAndPawn(bishop, pawn):
    list1 = list(bishop)
    list2 = list(pawn)
    list1[0] = ord(list1[0].lower())-96
    list2[0] = ord(list2[0].lower())-96
    list1 = [int(x) for x in list1]
    list2 = [int(x) for x in list2]
    if abs(list2[1] - list1[1]) == abs(list2[0] - list1[0]):
        return True
    else:
        return False
