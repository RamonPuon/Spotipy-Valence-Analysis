# Spotipy-Valence-Analysis

## Radiohead Analysis

Music is everywhere, it is part of our daily lives, and streaming services like spotify have made it easy for everyone to access all kinds of music. At any time you can listen to a large part of the catalog of multiple artists. All this amount of content generates a wide range of data about our favorite songs, which can give us interesing insights about them. 

This is my first attempt to analyze the Radiohead discography, using the Python library [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) for handling the Spotify Web API. All this idea was inspired by [this blog](https://www.rcharlie.com/blog/fitter-happier/) posted in Thompson Analytics, where an analysis of Radiohead albums is carried out using R.

This is still a work in progress, so far I have analyzed the audio features of the songs from each album. Starting with the variable Valence, which according to Spotify's documentation it can be defined as: 
> A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).

Meaning I was able to verify that A Moon Shaped Pool is, musically, the saddest Radiohead Album. All the details of this analysis and its visualization can be seen at the Jupyter Notebook on this repository.

![You can see the Valence in the album cover](https://m.media-amazon.com/images/I/815bmGN5LML._AC_SX466_.jpg)
