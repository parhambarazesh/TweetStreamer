# TweetStreamer

This webapp streams tweets in real-time using TweeterAPI, Filtered Stream endpoint based on a keyword.
You will need to setup a developer account in Twitter website (https://developer.twitter.com/en) and create an app.
The credentials are used to connect to the APIs. This app uses BREAER_TOKEN which needs to be fed into the tweet_streamer.py as an env variable (or other ways).

How to run:

1. set a mongodb server up and running
2. run data_producer/data_receiver.py
3. run data_consumer/web_socket.py
4. open localhost:3000 in the browser
