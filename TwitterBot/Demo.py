# importing the module 
import tweepy 
   
access_token = "3411995465-o82AMN7CnaKqpg4vV3OankKKcOyswpSP47rLG0I"
access_token_secret = "XRXtmob3zeRmumcgSwuPl30wyr7G2a0PNANLZWK9v2Ntl"
consumer_key = "OdUX2xAE7BxwRBSPkl5jDJkiB"
consumer_secret = "Hb294VT37O1SpqtEmj6SB8vX9yIwbFfMNfncIF0ulvoYNsx7Lr"
   
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
tweet ="Testailua" # toDo 
image_path ="Projects/Twitter/Images/testia.jpg" # toDo 
  
# to attach the media file 
status = api.update_with_media(image_path, tweet)  
#api.update_status(status = tweet)  
  
# update the status 
#api.update_status(status ="Asd !") 