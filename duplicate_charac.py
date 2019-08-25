
def duplication ( string ):
    match = string[0]
    index = 1

    for letter in string:
        potential_duplicate = string[index]
        if match == potential_duplicate:
            print (potential_duplicate)
            return
        else:
            match = potential_duplicate
            index += 1



duplication( "abcdefghhijkkloooop" )
