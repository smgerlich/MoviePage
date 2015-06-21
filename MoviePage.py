#!/usr/bin/env python

import media
from apiclient.discovery import build

# Must insert API Key here
api_key = ''
playlist_id = 'PLvxSBboz1_2vgYIxJzQMYs1cHPpQwvkBc'


def get_videos_from_playlist(api_key, playlist_id):
    """takes an api_key and youtube playlist id and returns a
    videolist object from the youtube python API"""

    # instantiate the api
    service = build('youtube', 'v3', developerKey=api_key)

    # get all item IDs from playlist
    playlist = service.playlistItems().list(part='snippet',
                                            playlistId=playlist_id,
                                            maxResults=50).execute()

    # we need the IDs in a csv string
    video_id_list = ''
    for item in playlist['items']:
        video_id_list += item['snippet']['resourceId']['videoId']+','
    video_id_list = video_id_list.rstrip(', ')

    # get the videolist object containing all the
    # videos in the playlist
    video_data = (service.videos()
                  .list(part="id, snippet, contentDetails, player",
                        id=video_id_list).execute())
    return video_data


def make_movies(videos):
    """takes a youtube videolist object and returns
    a list of Media objects"""
    movie_list = []
    for video in videos['items']:
        movie = media.Movie(video)
        movie_list.append(movie)
    return movie_list

movies_list = make_movies(get_videos_from_playlist(api_key, playlist_id))


# ready the HTML for each image/title card and each detail
# pane to be inserted into main.html.
paper_tabs = ''
movie_details = open('elements/welcome.html').read()

for movie in movies_list:
    paper_tabs += movie.cardHTML
    movie_details += movie.paneHTML

print open('main.html').read().format(paper_tabs=paper_tabs,
                                      movie_details=movie_details)
