# Name: Emily Mendelson (20071835)
# Date: August 4, 2020
# CISC 121 Assignment 3


"""The recommendations module creates a randomized dictionary of subscribers and music ratings. It recommends
a music genre for a user, calculates how similar two users are, and matches users based on similarity."""


from random import *
from math import *


# initialize subscribers list and music_genre list
subscribers = [
			'Justin Trudeau',
			'Bob Jones',
			'Sam Frizzel',
			'Captain Nemo',
			'Joe Jameson',
			'Paul Casindes',
			'Justin Bieber',
			'Natlie Portman',
			'Bugs Bunny',
			'Peter Rabbit',
			'Mickey Mouse',
			'Martin Melchor',
			'Nada Neel',
			'Kristin Karlin',
			'Edmond Earls',
			'Fredrick Foxwell',
			'Thomas Twitty',
			'Julieann Jenning',
			'Anton Autin',
			'Alix Ashmore',
			'Tiffany Turgeon',
			'Noella Nash',
			'Esther Edgerton',
			'Sanda Sewart',
			'Fannie Ferrera',
			'Bernardine Block',
			'Roger Rudd',
			'Yang Wu',
			'Raisa Rohr',
			'Cirocco Jones',
			'Mickie Milling',
			'Ronald McDonald',
			'Tim Horton',
			'Colonel Sanders',
			'Joel Jerry',
			'Leanora Lion',
			'Oscar Oliverio',
			'Jernau Fortier'
		]
		
music_genres = [
			'Jazz',
			'Country',
			'Rap',
			'Blues',
			'Reggae',
			'Soul',
			'EDM',
			'Hip Hop',
			'World',
			'Rock',
			'Funk',
			'Dance',
			'Pop',
			'Metal',
			'Easy Listening',
			'Hits',
			'Opera',
			'Classical',
			]

			
# create nested dictionary
subscriber_ratings = {}
num_genres = len(music_genres)
for p in subscribers:
	subscriber_ratings[p] = {}
	num_ratings = randint(num_genres/3,num_genres*2/3)
	chosen_genres = sample(music_genres,num_ratings)
	for f in chosen_genres:
		subscriber_ratings[p][f] = randint(1,10)


"""The genre_similarity function accepts a dictionary of subscriber ratings and two subscriber names as its parameters. 
The function will return the similarity value for the two subscribers inputted. Similarity is calculated using
fuzzy set theory."""


def genre_similarity(subscriber_ratings, sub1, sub2):
	sub1_sum = 0
	sub2_sum = 0
	intersection_sum = 0
	if sub1 and sub2 in subscriber_ratings:
		for i in music_genres:	 # For each genre in the music_genres list.
			if i in subscriber_ratings[sub1]:	 # If the ith genre is in sub1's dictionary.
				# Add the rating for that genre in sub1's dictionary to sub1_sum.
				sub1_sum = sub1_sum + subscriber_ratings[sub1][i]
			if i in subscriber_ratings[sub2]:
				# Add the rating for that genre in sub2's dictionary to sub2_sum.
				sub2_sum = sub2_sum + subscriber_ratings[sub2][i]
			if i in subscriber_ratings[sub1] and i in subscriber_ratings[sub2]:
				# If ith genre is in sub1 and sub2's dictionaries, add the min of the two ratings to the intersection_sum.
				intersection_sum = intersection_sum + min(subscriber_ratings[sub1][i], subscriber_ratings[sub2][i])

		intersection_sub1 = intersection_sum/sub1_sum
		intersection_sub2 = intersection_sum / sub2_sum

		similarity = min(intersection_sub1, intersection_sub2)

		return similarity
	else:
		similarity = "One or both of these subscribers do not exist."
		return similarity


"""The match_subscribers function accepts a dictionary of subscriber ratings and a subscriber name, custName, 
as its parameters. The function will return the name of the subscriber that is most similar to custName.
To do this it uses the genre_similarity function, and looks for the subscriber with the highest similarity."""


def match_subscribers(subscriber_ratings, custName):
	similarity_ratings = {}
	sub1 = custName
	if sub1 in subscriber_ratings:	 # Check if custName is in subscriber_ratings dictionary.
		for i in subscriber_ratings:
			if sub1 != i:
				sub2 = i
				# Use genre_similarity to create dictionary of similarity ratings.
				similarity_ratings[i] = genre_similarity(subscriber_ratings, sub1, sub2)
				# Choose the max value in the similarity_ratings dictionary to find most similar subscriber.
				similarity_sub = max(similarity_ratings.values())
		for name in similarity_ratings:
			if sub1 != name:
				if similarity_sub != 0:	 # If there is a subscriber with a similarity score that is not zero.
					if similarity_sub == similarity_ratings[name]:
						return name # Return the name of the subscriber with the highest similarity score.
				else:	 # If there is not a subscriber with a similarity score that is not zero.
					no_subs = "No similar subscribers"
					return no_subs
	else:
		not_in_list = "This subscriber does not exist in the dictionary."
		return not_in_list


"""The recommend_genre function will accept a dictionary of subscriber ratings and the name of a subscriber as its 
parameters. The function will return a recommended music genre for the given subscriber."""


def recommend_genre(subscriber_ratings, custName):
	# The match_subscribers function is called to find the most similar subscriber to custName.
	similar_sub = match_subscribers(subscriber_ratings, custName)
	unique_genres = {}
	if match_subscribers(subscriber_ratings, custName) == "No similar subscribers":
		return "No genre could be recommended"
	if match_subscribers(subscriber_ratings, custName) == "This subscriber does not exist in the dictionary.":
		return "This subscriber does not exist in the dictionary."
	else:	 # If a customer name is returned by match_subscribers function.
		for genre in music_genres:
			# If genre is not in custName dictionary, but is in the dictionary of the most similar subscriber.
			if genre not in subscriber_ratings[custName] and genre in subscriber_ratings[similar_sub]:
				# Add the genre and the rating to the unique_genres dictionary.
				unique_genres[genre] = subscriber_ratings[similar_sub].get(genre)
		if unique_genres == {}:
			return("No recommendation could be made because the most similar subscriber listens to the same genres.")
		else:
			# Recommend the genre with the highest rating from unique_genres dictionary.
			recommended_genre = max(unique_genres.values())
			for genre in unique_genres:
				if recommended_genre == unique_genres[genre]:
					return genre
