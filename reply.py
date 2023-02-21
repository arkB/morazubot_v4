# -*- coding:utf-8 -*-
import config
from transformers import T5Tokenizer, AutoModelForCausalLM
import twitter

if __name__ == '__main__':
  # set tokenizer and model
  tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-small")
  model = AutoModelForCausalLM.from_pretrained("output/")

  # set Twitter OAuth
  BOT_SCREEN_NAME = config.BOT_SCREEN_NAME
  ACCESS_TOKEN_KEY = config.ACCESS_TOKEN_KEY
  ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET
  CONSUMER_KEY = config.CONSUMER_KEY
  CONSUMER_SECRET = config.CONSUMER_SECRET
  oauth = twitter.OAuth(ACCESS_TOKEN_KEY,
                        ACCESS_TOKEN_SECRET,
                        CONSUMER_KEY,
                        CONSUMER_SECRET)

  # set Twitter API
  twitter_api = twitter.Twitter(auth=oauth)
  friends = twitter_api.friends.ids(screen_name=BOT_SCREEN_NAME, count=5000)
  friends_ids = ','.join(map(str, friends['ids']))
  stream = twitter.TwitterStream(auth=oauth, secure=True)

  # reply
  for tweet in stream.statuses.filter(follow=friends_ids):
    if 'user' in tweet and tweet['user']['id'] in friends['ids']:
      if '@'+BOT_SCREEN_NAME in tweet['text']:
        status_id = str(tweet["id"])
        prompt = tweet['text'].replace('@'+BOT_SCREEN_NAME+' ','')
        input = tokenizer.encode(prompt, return_tensors="pt")
        output = model.generate(input, do_sample=True, max_length=137, num_return_sequences=1)
        decoded = tokenizer.batch_decode(output, skip_special_tokens=True)
        tweet_text = decoded[0][len(prompt)+1:]
        if len(tweet_text) < 140:
          twitter_api.statuses.update(status='@'+tweet['user']['screen_name']+' '+tweet_text, in_reply_to_status_id=status_id)
        else:
          twitter_api.statuses.update(status='@'+tweet['user']['screen_name']+' '+tweet_text[:130]+"字数", in_reply_to_status_id=status_id)
