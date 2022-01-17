import os
import time
from pynput import keyboard as k
from vlc import MediaPlayer as mp
from argparse import ArgumentParser as ap

player = mp()
left = "a"
right = "s"
c = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
bookmark = []
o = ""
is_playing = False
music = ""
path = ""

def p(any):
    global o 
    o += str(any) + "\n"
    c()
    print(o)

def play(music: str):
    global player
    player = mp(music)
    player.play()
        
def click(key):
    global bookmark
    try:
        if key.char in [left, right]:
            bookmark.append(player.get_time())
    except AttributeError:
        pass

def release(key):
    global is_playing
    if key == k.Key.space and is_playing == False:
            p("Starting Music")
            is_playing = True
            play(music)

if __name__ == '__main__':
    try:
        parser = ap(description="a helpful tool for making bookmarks for osu!")
        parser.add_argument("music", metavar="music", type=str, help="the music to play")
        parser.add_argument("--left", "-l", type=str, metavar="key", default="a", help="left key (default: a)")
        parser.add_argument("--right", "-r", type=str, default="s", metavar="key", help="right key (default: s)")
        
        args = parser.parse_args()
        left = args.left
        right = args.right
        music = args.music
        
        print("Click Space to start the song!")
        with k.Listener(on_press=click, on_release=release) as listener:
            listener.join() 
        
        while True:
            time.sleep(1)      
    except KeyboardInterrupt:
        p("Result: " + (",".join(str(e) for e in bookmark)))
        