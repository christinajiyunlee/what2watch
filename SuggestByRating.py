"""
Suggest movies in order of highest ratings
"""

from ParseRatings import movie_ratings, allratings
from ParseMovie import movie_profile

suggest = []

#input range of ratings you want movies to be in
stars_l = 4 #intput("at least how many stars do you want your movie to have?")
stars_u = 5 #input("at most how many stars do you want your movie to have?")

allratings = movie_ratings

#build suggest array if movie meets rating criteria
for i in range(len(movie_profile)):
    if allratings >= stars_l and allratings <= stars_u:
        suggest.append(movie_profile[1])
