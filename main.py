# ---------------------------
# Configuration des API de Twitter et Mastodon
# ---------------------------
config = {
    "mastodon_token" : "",
    "mastodon_url" : "",
    "twitter_key" : "",
    "twitter_key_secret" : "",
    "twitter_token" : "",
    "twitter_token_secret" : "",
}

# ---------------------------
# Contenu du message
# ---------------------------

texte = "Un peu de texte"
images = ["/chemin/vers/mon_image.jpg"]

# ---------------------------
# Publication du message sur Twitter et Mastodon
# ---------------------------

from pyTweetodon import pyTweetodon
pyTweetodon(config, texte, images)
