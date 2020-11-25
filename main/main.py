from unsplash_search import UnsplashSearch
from unsplash.api import Api
from unsplash.auth import Auth
import urllib.request
import subprocess


client_id = "fc1c5ae4391097118e468b5ad1149fad31026b70811e3898e5bf63080dee6f3a"
client_secret = "342eb1f4ec97e4e1b552e9462764d9df51120fee0353a6a9ab5b7c27778a6f8f"
redirect_uri = ""
code = ""
base_dir = "/home/lucasclusman/Images/wallpapers"

auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)

image = api.photo.random(query='sunset wallpaper desktop')
link = api.photo.download(image[0].id)
file = "{0}/{1}.jpg".format(base_dir, image[0].id)

urllib.request.urlretrieve(link['url'], file)
subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', "file://{}".format(file)])

