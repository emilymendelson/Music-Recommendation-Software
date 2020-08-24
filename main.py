# Name: Emily Mendelson (20071835)
# Date: August 4, 2020
# CISC 121 Assignment 3

import recommendations
import statistics


# The main() function starts program execution.
def main():
    print("MAIN MENU")
    custName = input("Please enter the name of the subscriber to see their genre recommendations: ")
    subscriber_ratings = recommendations.subscriber_ratings

    # Call recommend_genre function.
    if custName in subscriber_ratings:   # Check that inputted custName is in subscriber_ratings
        print("The recommended genre for " + custName + " is: ")
        print(recommendations.recommend_genre(subscriber_ratings, custName)) # Print output from recommend_genre function
    else:
        print("This user does not exist. Please try again.")
        main()

    # Call average_ratings function.
    print("")
    print("The Average Ratings of Each Genre")
    statistics.average_ratings(subscriber_ratings)

    # Call most_popular function.
    print("")
    print("The most popular genre is: ")
    print(statistics.most_popular(subscriber_ratings))

    # Call most_similar function.
    print("")
    print("The most similar subscriber is: " + recommendations.match_subscribers(subscriber_ratings, custName))
    print("")

    main()

if __name__ =='__main__':
    # Run main() function.
    main()