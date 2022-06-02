def get_pairs(cast_and_crew):
    '''
    Returns a list of all the pairs individuals who have worked together

    Parameters
    ----------
    cast_and_crew : list
        a list of all the cast and crew members of all the shows on netflix

    Returns
    -------
    cast_and_crew_pairs : list
        a list of all the pairs of cast and crew members who have worked together

    '''
    cast_and_crew_pairs = []
    for i in range(len(cast_and_crew)):
        for j in range(len(cast_and_crew[i])):
            for k in range(len(cast_and_crew[i])):
                individual_1 = cast_and_crew[i][j]
                individual_2 = cast_and_crew[i][k]
                if individual_1 > individual_2:
                    cast_and_crew_pairs.append((individual_1, individual_2))
    return cast_and_crew_pairs       


def count_for_each_pair(cast_and_crew):
    '''
    Counts the total number of times each pair of individuals have worked together  

    Parameters
    ----------
    cast_and_crew : list
        a list of all the cast and crew members of all the shows on netflix

    Returns
    -------
    num_shows_for_cast_and_crew_pairs : dict
        keys are the pairs of cast and crew members, values are the number of times they have worked together  

    '''
    cast_and_crew_pairs = get_pairs(cast_and_crew)
    num_shows_for_cast_and_crew_pairs = {}
    for cast_or_crew in cast_and_crew_pairs:
        if cast_or_crew in num_shows_for_cast_and_crew_pairs:
            num_shows_for_cast_and_crew_pairs[cast_or_crew] += 1
        else:
            num_shows_for_cast_and_crew_pairs[cast_or_crew] = 1
    return num_shows_for_cast_and_crew_pairs

          
def x_or_more_given_df(cast_and_crew, x = 10):
    '''
    Prints the pairs of cast and crew members who have worked together on x or more shows and the corresponding number of shows they have worked together on 

    Parameters
    ----------
    cast_and_crew : list
        a list of all the cast and crew members of all the shows on netflix
    x : int, optional
        the number of times the pairs of cast and crew members of worked together. The default is 10.

    Prints
    -------
    str,
        {pair of cast and crew members}: {number of shows they have worked together on}

    '''
    if not isinstance(x, int):
        raise TypeError(f"x to be an integer, but {type(x)} is given.")
    if x < 0:
        raise ValueError(f"x has to be a non-negative integer, but {x} is given.")        

    num_shows_for_cast_and_crew_pairs = count_for_each_pair(cast_and_crew)
    for cast_or_crew in num_shows_for_cast_and_crew_pairs:
        if num_shows_for_cast_and_crew_pairs[cast_or_crew] > x:
            print(f"{cast_or_crew}: {num_shows_for_cast_and_crew_pairs[cast_or_crew]}")
 
            
def x_or_more_given_dict(cast_and_crew_counts, x = 10):
    '''
    Prints the pairs of cast and crew members who have worked together on x or more shows and the corresponding number of shows they have worked together on 

    Parameters
    ----------
    cast_and_crew_counts : dict
        a dictionary of all the pairs of cast and crew members and the number of shows they have worked together on
    x : int, optional
        the number of times the pairs of cast and crew members of worked together. The default is 10.

    Prints
    -------
    str,
        {pair of cast and crew members}: {number of shows they have worked together on}

    '''
    if not isinstance(x, int):
        raise TypeError(f"x to be an integer, but {type(x)} is given.")
    if x < 0:
        raise ValueError(f"x has to be a non-negative integer, but {x} is given.")        

    for key in cast_and_crew_counts.keys():
        if cast_and_crew_counts[key] > x:
            print(f"{key}: {cast_and_crew_counts[key]}")


