import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.twitch.tv/coreano')
except urllib.error.URLerror:
    print('Não consegui acessar o site.')
else:
    print('Consegui ter acesso ao site.')