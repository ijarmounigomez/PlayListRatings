PlayListRatings = [10,9,8.5,9.2,7,4,5,6]
i = 0 
rating = PlayListRatings [0]

while (i < len(PlayListRatings) and rating >= 6):
    rating = PlayListRatings [i]
    print (rating)
    i = i + 1
