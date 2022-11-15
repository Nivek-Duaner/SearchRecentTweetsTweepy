import tweepy

bearer_token = input("Insert Bearer Token here : ")
# You have to register at : https://developer.twitter.com/en

request = tweepy.Client(bearer_token)

try:
  # Twitter API Query Builder : https://developer.twitter.com/apitools/query?query=
  response = request.search_recent_tweets('"replit" -is:retweet -is:reply', 
                                          tweet_fields=["created_at", "lang"], 
                                          expansions=["author_id"], 
                                          user_fields=["created_at"], 
                                          max_results=10)
except:
  print("Bearer Token is probably not correct...")

else:
  tweets = response.data
  includes = response.includes
  users = includes["users"]
  
  users = {user["id"]: user for user in users}
  
  for tweet in tweets:
  
    print(f"Username : @{users[tweet.author_id].username} / Name : {users[tweet.author_id].name} / Created at : {users[tweet.author_id].created_at}")
    print(f"Tweet (id = {tweet.id}): \n{tweet.text}")
    print(f"Date and hour : {tweet.created_at}")
    print(f"Lang : {tweet.lang}")
    print("")