from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Title: {self.title} Movie Id:({self.id})"


# newly_created_movie = Movie.objects.create(title="The Princess Bride",description="the best movie ever",release_date="1987-09-25",duration=98)
# print(newly_created_movie.id)

# # another way to add a row to our database

# # newly_created_movie = Movie(title="The Princess Bride",description="the best movie ever",release_date="1987-09-25",duration=98)
# # newly_created_movie.save()

# # get all movies
# all_movies = Movie.objects.all()


# # filter (WHERE)
# some_movies = Movie.objects.filter(release_date='2018-11-16')

# #exclude (WHERE NOT)
# other_movies = Movie.objects.exclude(release_date='2018-11-16')

# # when we have a list of instances
# for m in all_movies:    # m represents each movie instance as we iterate through the list
#     print(m.title)	# that means m has all the properties of the Movie class, including title, release_date, etc.


# # single records

# one_movie = Movie.objects.get(id=7)

# # to get the first row from the table:
# first_movie = Movie.objects.first()

# # to get the last row from the table:
# last_movie = Movie.objects.last()

# print("Movie 7", one_movie.title)
# print("First movie", first_movie.release_date)
# print("Last movie", last_movie.description)

# # UPDATING

# movie_to_update = Movie.objects.get(id=42)	# let's retrieve a single movie,
# movie_to_update.description = "the answer to the universe"	# update one/some of its field values
# movie_to_update.title = "The Hitchhiker's Guide to the Galaxy"
# movie_to_update.save()  # then make sure all changes to the existing record get saved to the database


# # DELETING 
# movie_to_delete = Movie.objects.get(id=2)	# let's retrieve a single movie,
# movie_to_delete.delete()	# and then delete it
