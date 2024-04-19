from django.shortcuts import get_object_or_404, render
from core.models import * 


# Create your views here.
def home(request):
    movie = Movie.objects.all()  

    imgPaths = [movie.imgPath for movie in movie]

    context = {
        "movie": movie, "imgPaths": imgPaths
    }

    return render(request, "home.html", context) 


def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    poster_path = movie.imgPath = movie.imgPath
    mpaa_rating = MPAARating.objects.filter(pk=movie.mpaaRating_id).first()
    genre_movie = (movie.genre1, movie.genre2)

    context={
        "movie": movie, "mpaa_rating": mpaa_rating, 'Genre': genre_movie, "image":poster_path
    }

    print(poster_path)
    return render(request, 'detail_movie.html', context)