"""
Suggest by year

2.0:
Try setting range of movie years (get rid of before/after, make range of years)
Order movies from newest to oldest
Display year of release next to name
"""

from ParseMovie import movie_profile


def recom_year():

    year_from = int(input("From what year?"))
    year_to = int(input("To what year?"))

    i = 0
    suggest2 = []
    while i < len(movie_profile):
        if int(movie_profile[i][2]) >= year_from:
            if int(movie_profile[i][2]) <= year_to:
                suggest2.append(movie_profile[i][1])
            else:
                pass
        i += 1
    import numpy as np
    suggest = np.unique(suggest2)

    return suggest

    # if before_after == 'before':
    #     if int(movie_profile[i][2]) <= release_year: #int() bc element is string
    #         suggest.append(movie_profile[i][1])
    # elif before_after == 'after':
    #     if int(movie_profile[i][2]) >= release_year:
    #         suggest.append(movie_profile[i][1])
    # i += 1
