import media
import fresh_tomatoes
import urllib.request
import json

auth='ad7c97ac9bcb03c023df835b77650a9e'
url='https://api.themoviedb.org/3/movie/'
imgBasePath='https://image.tmdb.org/t/p/w500'
trailerBasePath='http://youtube.com/watch?v='
movies=[]

'''
Movies to be added:
1. Princess Mononoke
2. Howl's Moving Castle
3. Spirited Away
4. The Secret Life of Walter Mitty
5. The Perks of Being a Wallflower
6. Pride and Prejudice
'''

for mId in ['128', '4935', '129', '161', '207703', '284054', '116745', '84892', '11820']:
    #IDs extracted from movie urls from https://www.themoviedb.org/
    response=urllib.request.urlopen(url+mId+'?api_key='+auth+'&append_to_response=videos').read()
    json_obj=str(response, 'utf-8')
    data=json.loads(json_obj)
    movies.append(media.Movie(data['title'], data['overview'], imgBasePath+data['poster_path'],
                              trailerBasePath+data['videos']['results'][0]['key']))

fresh_tomatoes.open_movies_page(movies)

