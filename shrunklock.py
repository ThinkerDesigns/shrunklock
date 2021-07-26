#import os
import requests
#import json
#import sys
#import re
#import platform
#from argparse import ArgumentParser, PARSER
val = input("Enter the user for which you would like to search: ")
print ("Searching, this may take a while\n")
#def search():
#    file = open("resource/site.json",)
#    siteData = json.load(file)

#    for i in siteData["facebook"]:
#        print(i)
#    file.close()
#search()
def search():
    sitesOneDir = ["about.me", 
                   "independent.academia.edu", 
                   "ask.fm", 
                   "avizo.cz", 
                   "blip.fm", 
                   "bandcamp.com", 
                   #"bazar.cz", 
                   "behance.net", 
                   "bitbucket.org", 
                   "bodyspace.bodybuilding.com", 
                   "buymeacoff.ee", 
                   "buzzfeed.com", 
                   "career.habr.com", 
                   "profil.chatujme.cz", 
                   "codepen.io", 
                   "coroflot.com", 
                   "countable.us", 
                   "dev.to", 
                   "dailymotion.com", 
                   "designspiration.net", 
                   "disqus.com", 
                   "dribbble.com", 
                   "ello.co", 
                   "f3.cool", 
                   "facebook.com", 
                   "facenama.com", 
                   "my.flightradar24.com", 
                   "giphy.com", 
                   "github.com", 
                   "gitlab.com", 
                   "gitee.com", 
                   "goodreads.com", 
                   "en.gravatar.com", 
                   "gumroad.com", 
                   "hackaday.io", 
                   "hackerone.com", 
                   "hackerrank.com", 
                   "icq.im", 
                   "imgup.cz", 
                   "issuu.com", 
                   "kaggle.com", 
                   "keybase.io", 
                   "kik.me", 
                   "leetcode.com", 
                   "letterboxd.com", 
                   "mixcloud.com", 
                   "myspace.com", 
                   "blog.naver.com", 
                   "notabug.org", 
                   "ok.ru", 
                   "psnprofiles.com", 
                   "patreon.com", 
                   "pinterest.com", 
                   "polarsteps.com", 
                   "promodj.com", 
                   "quizlet.com", 
                   "reverbnation.com", 
                   "sbazar.cz", 
                   "scribd.com", 
                   "slideshare.net",
                   "smule.com", 
                   "soundcloud.com", 
                   "t.me", 
                   "tellonym.me", 
                   "trello.com", 
                   "twitch.tv", 
                   "vk.com", 
                   "vsco.co", 
                   "venmo.com", 
                   "vero.co", 
                   "vimeo.com", 
                   "weheartit.com", 
                   "younow.com", 
                   "authorstream.com"
                  ]
    for i in sitesOneDir:
        req = requests.get("//" + i + "/" + val)
        print((i + "/" + val), req.status_code)
search()
#print("Ignore that, nothing to worry about")
