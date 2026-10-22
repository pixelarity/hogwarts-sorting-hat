def check_gryffindor_eligibility(bravery, loyalty, ambition):
    """
    Given three integer scores (0-10) for bravery, loyalty and ambition,
    decide whether a student is Gryffindor material.

    Rules:
    - Every score must be between 0 and 10 (inclusive). If any score is
      out of that range, return "Invalid score".
    - The student qualifies if bravery is at least 7, AND at least one
      of loyalty or ambition is at least 5.
    - If they qualify, return "Gryffindor material!".
    - If they do not qualify, return "Not Gryffindor material.".
    """
    if (bravery < 0 or bravery > 10) or (loyalty < 0 or loyalty > 10) or (ambition < 0 or ambition > 10):
        return "Invalid score"
    elif (bravery >= 7) and ((loyalty >= 5) or (ambition >= 5)):
        return "Gryffindor material"
    else:
        return "Not Gryffindor material"
    # TODO: Write your if / elif / else logic here.
    # This time you will need to combine comparison operators
    # (>, <, ==, >=, <=) with and / or.
    pass
