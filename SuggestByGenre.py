"""
Suggest movie by genre

QUESTION: make each of these new 'function' file into functions to call when I create the ultimate UI script?

2.0:
Order movies under each genre by highest to lowest rating

"""


from ParseMovie import movie_profile

def recom_genre():

    suggest1 = []
    genre = []
    nofgenre = input("How many genres?")

    for i in range(nofgenre):
        genre.append(input('What genre do you want to see?'))
    # genre = ['Horror', 'Action']

    i = 0
    while i < len(movie_profile):
        clean = movie_profile[i][3]
        for j in range(len(clean)):
            for k in range(len(genre)):
                if clean[j] == genre[k]:
                    suggest1.append(movie_profile[i][1])
                k += 1
        i += 1

    import numpy as np
    suggest = np.unique(suggest1) #this accidentally made my results super aesthetic

    return suggest
