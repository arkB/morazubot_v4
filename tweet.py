from transformers import T5Tokenizer, AutoModelForCausalLM
import tweepy
import configparser

def auth_api_v2(envName):
    config = configparser.ConfigParser(interpolation=None)
    config.read('morazu2_bot.ini')
    consumer_key = config.get(envName, 'consumer_key')
    consumer_secret = config.get(envName, 'consumer_secret')
    access_key = config.get(envName, 'access_key')
    access_secret = config.get(envName, 'access_secret')
    bearer_token = config.get(envName, 'bearer_token')
    client = tweepy.Client(bearer_token=bearer_token,
                           consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           access_token=access_key,
                           access_token_secret=access_secret)
    return client

if __name__ == '__main__':
  # Preparation of tokenizers and model
  tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-small")
  model = AutoModelForCausalLM.from_pretrained("output/")

  # Run inference
  prompt = "福岡"
  input = tokenizer.encode(prompt, return_tensors="pt")
  output = model.generate(input, do_sample=True, max_length=137, num_return_sequences=1)
  decoded = tokenizer.batch_decode(output, skip_special_tokens=True)

  # Twitter OAuth
  client = auth_api_v2('morazu2_bot')
  tweet_text = decoded[0][3:].replace("!", "！").replace("?", "？").replace("(","（").replace(")", "）")

  # Tweet
  if len(tweet_text) < 140:
      client.create_tweet(text=tweet_text)
  else:
      client.create_tweet(text=tweet_text[:138]+"字数")
