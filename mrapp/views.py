from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
import django.contrib.auth.decorators
from django.contrib.auth import login, authenticate, logout
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from imdb import IMDb


# Create your views here.

def land(request):
    return render(request, 'land.html')


def call(request):
    return render(request, 'call.html')


def home(request):
    return render(request, 'home.html')


def action(request):
    return render(request, 'category/action.html')


def comedy(request):
    return render(request, 'category/comedy.html')


def horror(request):
    return render(request, 'category/horror.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.last_name = last_name

        myuser.save()
        return redirect('home')

    else:
        return HttpResponse('404 - NOT FOUND')


def signin(request):
    if request.method == 'POST':
        loguser = request.POST['loguser']
        logpass = request.POST['logpass']

        myuser = authenticate(username=loguser, password=logpass)

        if myuser is not None:
            login(request, myuser)
            return redirect('call')
        else:
            return redirect('home')


ia = IMDb()


@django.contrib.auth.decorators.login_required
def recommend_movies(request):
    df = pd.read_csv("IMDb_All_Genres_etf_clean1.csv", encoding='latin-1')
    features = ['Director', 'Actors', 'main_genre', 'side_genre']
    for f in features:
        df[f] = df[f].fillna('')
    df['Genre'] = df['main_genre'] + ', ' + df['side_genre']
    df['Combined'] = df['Director'] + ', ' + df['Actors'] + ', ' + df['Genre']

    data = df.groupby(['Genre']).agg({'Combined': list, 'Movie_Title': list, }).apply(list).reset_index()
    titles = data["Movie_Title"].tolist()

    te = TransactionEncoder()
    te_ary = te.fit(titles).transform(titles)
    df_end = pd.DataFrame(te_ary, columns=te.columns_)

    apriori_frequent_itemsets = apriori(df_end, min_support=0.001, max_len=2, use_colnames=True)

    rules = association_rules(apriori_frequent_itemsets, metric="lift", min_threshold=0.01)

    input_movie = request.POST.get('movie_name')
    if input_movie:
        print('You searched for:', input_movie)
        recommended_movies = rules[rules["antecedents"].apply(lambda x: input_movie in str(x))].sort_values(
            ascending=False, by='lift')

        recommended_movies = recommended_movies.groupby(['antecedents', 'consequents'])[['lift']].max().sort_values(
            ascending=False, by='lift')

        movie_titles = recommended_movies.index.get_level_values(1).tolist()

        movie_titles_clean = []
        movie_posters = []
        for mt in movie_titles:
            if len(movie_titles_clean) == 18:
                break
            title = str(mt)
            title = title.replace("frozenset({'", "")
            title = title.replace("'})", "")
            movie_titles_clean.append(title)

            search_results = ia.search_movie(title)
            if search_results:
                movie = search_results[0]
                ia.update(movie)
                poster_url = movie.get('full-size cover url')
                movie_posters.append(poster_url)
            else:
                movie_posters.append(None)

        search_results = ia.search_movie(input_movie)
        if search_results:
            input_movie_obj = search_results[0]
            ia.update(input_movie_obj)
            input_movie_poster = input_movie_obj.get('full-size cover url')
        else:
            input_movie_poster = None


        if movie_titles_clean:
            return render(request, 'call.html',
                      {'movies': zip(movie_titles_clean[:18], movie_posters[:18]), 'input_movie': input_movie,'input_movie_poster': input_movie_poster,'has_recommendations':True})
        else:
            return render(request, 'call.html', {'movies': [], 'input_movie': input_movie, 'input_movie_poster': input_movie_poster, 'error_msg': 'No recommendations found.'})

@django.contrib.auth.decorators.login_required
def logoutuser(request):
    logout(request)
    return redirect('home')

