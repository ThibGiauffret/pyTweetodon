
import requests
from pathlib import Path
from tweepy import Client, API,OAuthHandler

def pyTweetodon(config, text, images) :
    media_ids = []
    for file in images:
        data = {
            'description': 'Image file ' + file
        }
        file_path = Path(file)
        files = {
            'file': (file, file_path.open('rb'), 'application/octet-stream')
        }
        url = config["mastodon_url"]+"/api/v1/media"
        r = requests.post(url, 
            files=files, 
            headers={'Authorization': 'Bearer '+config["mastodon_token"]})
        json_data = r.json()

        media_id = json_data['id']
        media_ids.append(media_id)

    data = { 
        "status": text, 
        "media_ids[]": media_ids
    }

    url = config["mastodon_url"]+"/api/v1/statuses"
    r = requests.post(url, 
            data=data, 
            headers={'Authorization': 'Bearer '+config["mastodon_token"]})
    json_data = r.json()
    print("Publication sur Mastodon terminée.")

    auth=OAuthHandler(config["twitter_key"],config["twitter_key_secret"])
    auth.set_access_token(config["twitter_token"],config["twitter_token_secret"])
    twitter=API(auth)


    twit_media_ids = []
    for i in images:
        response = twitter.media_upload(i)
        twit_media_ids.append(response.media_id)

    twitter.update_status(status=text, media_ids=twit_media_ids)
    print ("Publication sur Twitter terminée.")
