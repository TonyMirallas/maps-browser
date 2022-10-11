from multiprocessing.connection import wait
import webbrowser
import time
import sys

pages_list = ["https://www.twitch.tv/veranodelos90", "https://twitter.com/home", "https://web.whatsapp.com/", "https://www.youtube.com/", "https://www.youtube.com/watch?v=jRFRq1EEID0&list=PLuKau6Oi1dkQ0vtOPEVzDR-gZrE8_bY6r&index=41&t=261s&ab_channel=SkyGuitar"]

pages_list = {
    'twitter': 'https://twitter.com/home',
    'youtube': 'https://www.youtube.com/',
    'guitar': 'https://www.youtube.com/watch?v=jRFRq1EEID0&list=PLuKau6Oi1dkQ0vtOPEVzDR-gZrE8_bY6r&index=41&t=261s&ab_channel=SkyGuitar',
    'whatsapp': 'https://web.whatsapp.com/',
    'verano90': 'https://www.twitch.tv/veranodelos90',
}

open = []

args_list = sys.argv[1:]

if 'twitch' in args_list:
    open.append(pages_list["twitter"])
    open.append(pages_list["whatsapp"])
    open.append(pages_list["verano90"])

elif 'guitar' in args_list:
    open.append(pages_list["guitar"])
    open.append(pages_list["whatsapp"])
    open.append(pages_list["verano90"])
    
webbrowser.open(open[0])
webbrowser.open_new(open[1])
time.sleep(3)
webbrowser.open_new_tab(open[2])