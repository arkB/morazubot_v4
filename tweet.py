import config
from transformers import T5Tokenizer, AutoModelForCausalLM
import twitter

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
  ACCESS_TOKEN_KEY = config.ACCESS_TOKEN_KEY
  ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET
  CONSUMER_KEY = config.CONSUMER_KEY
  CONSUMER_SECRET = config.CONSUMER_SECRET
  oauth = twitter.OAuth(ACCESS_TOKEN_KEY,
                        ACCESS_TOKEN_SECRET,
                        CONSUMER_KEY,
                        CONSUMER_SECRET)
  tweet = twitter.Twitter(auth=oauth)
  tweet_text = decoded[0][3:]

  # Tweet
  if len(tweet_text) < 140:
      tweet.statuses.update(status=tweet_text)
  else:
      tweet.statuses.update(status=tweet_text[:138]+"字数")
