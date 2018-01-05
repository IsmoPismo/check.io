def safe_pawns(pawns):
    
    pawn_index = list()
    counter=0
    
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawn_index.append((row,col))

    for r in pawn_index:
        is_safe = ((r[0]-1, r[1]-1) in pawn_index) or ((r[0]-1, r[1]+1) in pawn_index)
        if is_safe:
            counter+=1
    
    return counter
        
if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1