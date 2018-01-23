"""
Python project version 1.0

Giving movie recommendations to users using various criteria
Parse movie.dat file
"""

#For each movie, determine its ratings as an average mean value of all ratings it's gotten from different users
#Calculate movie time by taking time stamp and converting it into minutes

#Create movie profile
#   create one giant list of all movies, describing each movie with the following characterstics:
#       - genre
#       - rating
#       - year of movie

file = open('movies.dat')

#separating movie ID number, movie title and genre
movies = []
genre_1 = []
genre_2 = []
rating1 = []

for line in file:
    movies += [line.split('::')]
    movie_id = [i[0] for i in movies]
    name_year = [i[1] for i in movies]
    genre_1 = [i[2] for i in movies]
    for k in range(len(genre_1)):
        char = genre_1[k]
        genre_1[k] = char[0:len(char)-1]

#creating an array of arrays (genres), for each movie
j = 0
while j < len(movies):
    genre_2.append(genre_1[j].split('|'))
    j += 1

#separating movie name from years
name = []
year = []
for index in range(len(name_year)):
    temp = name_year[index]
    name.append(temp[0:len(temp)-6-1])
    year.append(temp[len(temp)-5:len(temp)-1])

#giant array version of original movies.dat
zipmovies = zip(movie_id, name, year, genre_2)
movie_profile = list(zipmovies)

def main():
    pass

if __name__ == "__main__":
    print year


"""Appendix

#placing name and year into separate arrays
name = []
year = []

for i in range(len(name_year)):
    name = [i[0] for i in name_year]
    year = [i[1] for i in name_year]
    #getting rid of that outer bracket left on the year
    year = [i[:-1] for i in year]

"""
