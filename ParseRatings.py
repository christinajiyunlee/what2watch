"""
Parse ratings.dat file

- calculate average of all movies

commented out user_id and timestamp bc it's not used yet, for efficiency
"""

from ParseMovie import movie_profile, movie_id


file = open('ratings.dat')

ratings = []
rating = []
movie_id2 = []
#user_id = []
#timestamp = []
j = 0

#Split at every '::'
for line in file:
    ratings.append(line.split('::'))
    # j += 1
    # if j > 1000:
    #     break #for speed's sake, made it only run first 1000 lines

#Separating each dataset into different arrays
for i in ratings:
#    user_id.append(int(i[0]))
#    timestamp.append(i[3])
    movie_id2.append(int(i[1]))
    rating.append(int(i[2]))


# #Array of all desired movie characteristics: movie_id and ratings
zipratings = zip(movie_id2, rating)
movie_ratings = list(zipratings)

#Assign ratings to each movie
allratings = [None] * 3952 #more movie ids than movies due to duplicates?
for j in range(len(movie_ratings)):
    if allratings[(movie_ratings[j][0])-1] == None:
        allratings[(movie_ratings[j][0])-1] = [movie_ratings[j][1]]
    else:
        allratings[(movie_ratings[j][0])-1].append(movie_ratings[j][1])

# find average of ratings (as decimals as necessary) for all movies


for k in range(len(movie_id)):
    summed = 0.0
    if allratings[k] == None:
        pass
    else:
        for p in range(len(allratings[k])):
            summed += allratings[k][p]
    if p == 0:
        pass
    else:
        avgrating = summed/p
    allratings[k] = avgrating #length: 3952
    allratings = allratings[0:len(movie_id)]


def main():
    pass

if __name__ == "__main__":
    print (allratings)

"""
Appendix

#Removing /n at the end of timestamps
for j in range(len(timestamp)):
    char = timestamp[j]
    timestamp[j] = int(char[0:len(char)-1])/60
    #represents time of rating in min passed since Jan 1, 12am, 1970
    #if statements or loops to assign dates to each rating
"""
