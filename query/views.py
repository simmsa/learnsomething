import random

import gdata.youtube
import gdata.youtube.service

from django.shortcuts import render_to_response

def home(request):
    name = "Andrew"
    return render_to_response('index.html')

def find_video_id(entry):
    start = entry.find("=")
    end = entry.find("&", start + 1)
    return entry[start + 1: end]

def ReturnEntryDetails(entry):
    return find_video_id(entry.media.player.url)

def PrintVideoFeed(feed):
    array = []
    for entry in feed.entry:
        array.append(ReturnEntryDetails(entry))
    number = random.randint(0, 4)
    return array[number]

def SearchAndPrint(search_terms):
    yt_service = gdata.youtube.service.YouTubeService()
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.vq = search_terms
    query.orderby = "relevance"
    query.racy = "include"
    query.max_results = 5
    feed = yt_service.YouTubeQuery(query)
    return PrintVideoFeed(feed)

def completion_word(query):
    words = ["tutorial", "training", "tips"]
    return query + " " + words[random.randint(0, len(words) - 1)]

def learn(request):
    query = request.GET['q']
    video_id = SearchAndPrint(completion_word(query))
    return render_to_response("learn.html", {'query': query, 'video_id': video_id})