# Name: Emily Mendelson (20071835)
# Date: August 4, 2020
# CISC 121 Assignment 3

# This module runs the unit testing for the program.

import recommendations
import statistics

if __name__ =='__main__':
    # Create test_dictionary for unit testing.
    test_dictionary = {'Emily': {'Pop': 10, 'Rap': 5, 'Jazz': 2},
                       'Alec': {'Pop': 10, 'Rap': 5, 'Jazz': 2},
                       'Molly': {'Country': 8, 'Pop': 5, 'World': 3},
                       'Bob': {'EDM': 1, 'Opera': 4, 'Classical': 9}}

    print("UNIT TESTING")
    print("This is the start of the unit testing code.")
    print("")

    # Unit testing for genre_similarity function.
    print("Testing genre_similarity function")
    print(recommendations.genre_similarity(test_dictionary, 'Emily', 'Emily'), "Should return 1.0")
    print(recommendations.genre_similarity(test_dictionary, 'Emily', 'Alec'), "Should return 1.0")
    print(recommendations.genre_similarity(test_dictionary, 'Emily', 'Molly'), "Should return 0.29411764705882354")
    print(recommendations.genre_similarity(test_dictionary, 'Emily', 'Bob'), "Should return 0.0")
    print(recommendations.genre_similarity(test_dictionary, 'Emily', 'Joe'), "Should return One or both of these subscribers "
                                                                       "do not exist")
    print(recommendations.genre_similarity(test_dictionary, 'Emily', ''), "Should return One or both of these subscribers "
                                                                    "do not exist")
    print(recommendations.genre_similarity(test_dictionary, '', 'Emily'), "Should return One or both of these subscribers "
                                                                    "do not exist")
    print(recommendations.genre_similarity(test_dictionary, '', ''), "Should return One or both of these subscribers "
                                                               "do not exist")
    print(recommendations.genre_similarity(test_dictionary, 'emily', 'emily'), "Should return One or both of these "
                                                                         "subscribers do not exist")
    print(recommendations.genre_similarity(test_dictionary, 'emily', 'alec'), "Should return One or both of these "
                                                                        "subscribers do not exist")
    print(recommendations.genre_similarity(test_dictionary, 'emily', ''), "Should return One or both of these subscribers "
                                                                    "do not exist")
    print("")

    # Unit testing for match_subscribers function.
    print("Testing match_subscribers function")
    print(recommendations.match_subscribers(test_dictionary, 'Emily'), "Should return Alec.")
    print(recommendations.match_subscribers(test_dictionary, 'Molly'), "Should return Emily.")
    print(recommendations.match_subscribers(test_dictionary, 'Bob'), "Should return no similar subscribers.")
    print(recommendations.match_subscribers(test_dictionary, 'Joe'), "Should return This subscriber does not exist in "
                                                               "the dictionary.")
    print(recommendations.match_subscribers(test_dictionary, '3#$'), "Should return This subscriber does not exist in "
                                                               "the dictionary.")
    print(recommendations.match_subscribers(test_dictionary, 'emily'), "Should return This subscriber does not exist in "
                                                                 "the dictionary.")
    print(recommendations.match_subscribers(test_dictionary, 'Jazz'), "Should return This subscriber does not exist in "
                                                                "the dictionary.")
    print(recommendations.match_subscribers(test_dictionary, ''), "Should return This subscriber does not exist in "
                                                            "the dictionary.")
    print("")

    # Unit testing for most_popular function.
    print("Testing most_popular function")
    print(statistics.most_popular(test_dictionary), "Should return Pop")
    print("")

    # Unit testing for calculate_average function.
    print("Testing calculate_average function")
    statistics.calculate_average("Pop", test_dictionary), print("Should return Pop   8.3.")
    statistics.calculate_average("Funk", test_dictionary), print("Should return Funk     0.")
    statistics.calculate_average("pop", test_dictionary), print("Should return This genre is not in the music genre "
                                                               "list.")
    statistics.calculate_average("", test_dictionary), print("Should return This genre is not in the music genre "
                                                            "list.")
    statistics.calculate_average("123", test_dictionary), print("Should return This genre is not in the music genre "
                                                               "list.")
    statistics.calculate_average("123$%*", test_dictionary), print("Should return This genre is not in the music genre "
                                                                  "list.")
    statistics.calculate_average("Emily", test_dictionary), print("Should return This genre is not in the music genre "
                                                                 "list.")
    print("")

    # Unit testing for average_ratings function.
    print("Testing average_ratings function")
    print(statistics.average_ratings(test_dictionary), "Should return Pop: 8.3, Rap: 5.0, Jazz: 2.0, Country: 8.0, "
                                                      "World: 3.0, EDM: 1.0, Opera: 4.0, Classical: 9.0, and 0.0 for"
                                                      " all other genres in an easy-to-read table.")
    print("")

    # Unit testing for recommend_genre function.
    print("Testing recommend_genre function")
    print(recommendations.recommend_genre(test_dictionary, 'Emily'), "Should return no recommendation.")
    print(recommendations.recommend_genre(test_dictionary, 'Molly'), "Should return Rap.")
    print(recommendations.recommend_genre(test_dictionary, 'Bob'), "Should return no genre could be recommended.")
    print(recommendations.recommend_genre(test_dictionary, 'Joe'), "Should return This subscriber does not exist in "
                                                             "the dictionary.")
    print(recommendations.recommend_genre(test_dictionary, '3$*'), "Should return This subscriber does not exist in "
                                                             "the dictionary.")
    print(recommendations.recommend_genre(test_dictionary, 'emily'), "Should return This subscriber does not exist in "
                                                               "the dictionary.")
    print(recommendations.recommend_genre(test_dictionary, 'Jazz'), "Should return This subscriber does not exist in "
                                                              "the dictionary.")
    print(recommendations.recommend_genre(test_dictionary, ''), "Should return This subscriber does not exist in "
                                                          "the dictionary.")