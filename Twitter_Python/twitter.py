import tweepy

consumer_key = 'acisTloOHSws1UA289etVw'
consumer_secret = 'b9eVS9CeFxIFx3jIwKkeeQPfsO3hlrAdWNOfIItQEgU'
access_token = '2308079432-cDmExMexRNNwAEvIUdrtKQFXgfIA1vQPeM4mLRC'
access_token_secret = 'eUFjHJf3Wbqzo6NKxJRHE0HapuzNBzLynA8nOTOPygqis'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search,q="melero90",count=100,result_type="photo",include_entities=True).items():
    #print tweet.text
    if 'media' in tweet.entities:
        for image in  tweet.entities['media']:
            #print image['media_url']
		L.append(image['media_url'])


