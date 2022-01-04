#cred.py, python script with my client ID and my client secret
import cred
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

client_credential_manager = SpotifyClientCredentials(client_id= cred.client_ID, client_secret= cred.client_SECRET)
sp = spotipy.Spotify(client_credentials_manager= client_credential_manager)

#Function that returns every track from each album from a specific artist
def artist_tracks(artist):
    tracks = []

    for artist in artist:
        #Get artist id
        artist_uri = sp.search(artist)['tracks']['items'][0]['artists'][0]['uri']

        album_checker = []
        n = 0

        while len(sp.artist_albums(artist_uri, album_type= 'album', limit= 50, offset= n)['items']) > 0:
            #With this variable, on each loop the list of albums dictionaries will be saved each time
            dict_list = sp.artist_albums(artist_uri, album_type= 'album', limit= 50, offset= n)['items']

            for i, album in enumerate(dict_list):

                check_this_album = [j['name'] for j in dict_list[i]['artists']]
                check_this_album.append(dict_list[i]['name'])
                check_this_album.append(dict_list[i]['release_date'])

                if check_this_album not in album_checker:
                    album_checker.append(check_this_album)
                    #Everything to track
                    tracks.extend([[artist, album['name'], album['uri'], song['name'], 
                    album['release_date']]+ list(sp.audio_features(song['uri'])[0].values())
                    for song in sp.album_tracks(album['uri'])['items']])
            n += 50
    return tracks


def df_track(tracklist):

    df = pd.DataFrame(tracklist, columns= ['artist',
    'album_name',
    'album_uri',
    'track',
    'release_date'] + list(sp.audio_features('6rqhFgbbKwnb9MLmUQDhG6')[0].keys()))
    df.rename(columns= {'uri':'song_uri'}, inplace= True)
    df.drop_duplicates(subset= ['artist', 'track', 'release_date'], inplace= True)

    return df
