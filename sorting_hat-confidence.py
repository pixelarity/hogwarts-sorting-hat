def determine_house_by_confidence(confidence):
    """
    Given a single integer confidence score (0-10), return the name of
    the Hogwarts house it maps onto.

    Rules:
    - confidence 8, 9 or 10   -> "Gryffindor"
    - confidence 6 or 7       -> "Ravenclaw"
    - confidence 4 or 5       -> "Hufflepuff"
    - confidence 0, 1, 2 or 3 -> "Slytherin"
    - Anything outside 0-10   -> "Invalid score"
    """
    if confidence == 10:
        return "Gryffindor"
    elif confidence == 9:
        return "Gryffindor"
    elif confidence == 8:
        return "Gryffindor"
    elif confidence == 7:
        return "Ravenclaw"
    elif confidence == 6:
        return "Ravenclaw"
    elif confidence == 5:
        return "Hufflepuff"
    elif confidence == 4:
        return "Hufflepuff"
    elif confidence == 3:
        return "Slytherin"
    elif confidence == 2:
        return "Slytherin"
    elif confidence == 1:
        return "Slytherin"
    elif confidence == 0:
        return "Slytherin"
    else:
        return "Invalid score"
    # TODO: Write your if / elif / else logic here.
    # Use comparison operators (>, <, ==, >=, <=) only.
    # You should not need and / or for this challenge.
    pass
    # Remember to return values/variables rather than printing them
