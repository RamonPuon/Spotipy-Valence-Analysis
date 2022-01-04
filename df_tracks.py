import pandas as pd
import spotipy
import get_tracks

sp = spotipy.Spotify(client_credentials_manager= get_tracks.client_credential_manager)

def df_track(tracklist):

    df = pd.DataFrame(tracklist, columns= ['artist',
    'album_name',
    'album_uri',
    'track',
    'release_date'] + list(sp.audio_features('7tr2za8SQg2CI8EDgrdtN1')[0].keys()))
    df.rename(columns= {'uri':'song_uri'}, inplace= True)
    df.drop_duplicates(subset= ['artist', 'track', 'release_date'], inplace= True)

    return df

