# author=rhnvrm<hello@rohanverma.net>

from __future__ import absolute_import, print_function

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import key
global api


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        # this line parses the json data into a python dictionary
        d = json.loads(data)

        # uncomment this to explore the dictionary
        print(d, '\n')

        # uncomment this to just see the text of the tweet, simlarly you
        # can see the other fields of the dict
        print('test: ' + d["text"] + '\n')
        parsing = d['text'].split(' ')
        # uncomment to to tweet from your twitter bot
        # although before tweeting you might want to implement
        # command parsing and your logic
        if d['user']['screen_name'] == 'Hai3leyyy':
            api.update_status(
                status='@' + d['user']['screen_name'] +
                " Hey Sweetie, I'm typing this on April 1st of 2018, but even if that was months ago, I still love you"
            )
        elif d['user']['screen_name'] == 'lanceanjuna':
            api.update_status(
                status='@' + d['user']['screen_name'] +
                " I'm sorry, I never meant for any of this to happen")
        elif parsing[0] == 'Status:':
            parsing.pop(0)
            parsing.pop(parsing.index('#TannersBot'))
            tweet = ''
            for i in parsing:
                tweet += i + " "
            api.update_status(tweet)
        else:
            api.update_status(
                '@' + d['user']['screen_name'] +
                " BotSays: I have no idea, what the fuck you are talking about"
            )

        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    nolonger = StdOutListener()
    auth = OAuthHandler(key.consumer_key, key.consumer_secret)
    auth.set_access_token(key.access_token, key.access_token_secret)
    api = tweepy.API(auth)
    stream = Stream(auth, nolonger)
    # change filters to listen to various types of tweets
    # eg try 'coldplay', '@rhnvrm', '#ACMSNU' etc
    stream.filter(track=['#TannersBot'])