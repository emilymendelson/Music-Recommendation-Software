"""The statistics module imports the recommendations module and includes statistical functions.
These functions calculate and print out the average rating of each music genre and the most popular music genre"""

import recommendations

"""The calculate_average function accepts a genre and a dictionary of subscriber ratings as its parameters.
It prints the average rating for each genre."""


def calculate_average(genre, subscriber_ratings):
    if genre in recommendations.music_genres:
        num_genre = 0
        genre_total = 0
        genre_average = 0
        for i in subscriber_ratings:
            if genre in subscriber_ratings[i]:
                num_genre = num_genre + 1
                genre_total = genre_total + subscriber_ratings[i][genre]
            # genre_average is calculated by dividing the genre_total by the number of times the genre has been rated.
                genre_average = genre_total / num_genre
        if len(genre) < 4:
            print(genre + "				" + str(round(genre_average, 1)))
        if 4 <= len(genre) < 8:
            print(genre + "			" + str(round(genre_average, 1)))
        if 8 <= len(genre) < 10:
            print(genre + "		" + str(round(genre_average, 1)))
        if len(genre) >= 10:
            print(genre + "	" + str(round(genre_average, 1)))
    else:
        print("This genre is not in the music genre list.")


""""The average_ratings function accepts a dictionary of subscriber ratings as its parameter. 
It calls the calculate_average function which prints out the average rating for each genre of music. The average
rating for each genre is printed out in an easy-to-read table."""


def average_ratings(subscriber_ratings):
    print("GENRE		AVERAGE RATING")
    for i in recommendations.music_genres:
        genre = i
        # The calculate average function is called.
        calculate_average(genre, subscriber_ratings)


"""The most_popular function accepts a dictionary of subscriber ratings as its parameter and prints out the genre of 
music that is most popular based on the highest total rating from all subscribers."""


def most_popular(subscriber_ratings):
    total_ratings = {}
    for genre in recommendations.music_genres:
        genre_total = 0
        for i in subscriber_ratings:
            if genre in subscriber_ratings[i]:
                genre_total = genre_total + subscriber_ratings[i][genre]
        total_ratings[genre] = genre_total  # genre and genre_total are added to total_ratings dictionary.
        popular_genre = max(total_ratings, key=lambda k: total_ratings[k])
    return (popular_genre)
