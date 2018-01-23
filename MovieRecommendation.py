"""
Final interface
"""
from ParseMovie import movie_id, name, year, genre_2, movie_profile
from ParseRatings import allratings

from SuggestByGenre import recom_genre
from SuggestByYear import recom_year


zipfinal = zip(movie_id, name, year, genre_2, allratings)
answer = list(zipfinal)

genrelist = recom_genre()
yearlist = recom_year()

# print yearlist
print genrelist

# display movie per line
# display year, rating, all info
