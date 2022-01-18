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
exit_key = "m"
running = True
tickd = 1
offset = 0

def get_tick():
    return (round(player.get_time() / tickd) * tickd) + offset

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
            bookmark.append(int(get_tick()))
    except AttributeError:
        pass

def release(key):
    global is_playing, running
    if key == k.Key.space and is_playing == False:
            p("Starting Music")
            is_playing = True
            play(music)
    try:
        if key.char == exit_key:
            return False
    except AttributeError:
        pass

if __name__ == '__main__':
    try:
        parser = ap(prog="barnacle" ,description="a helpful tool for making bookmarks for osu!")
        parser.add_argument("music", metavar="music", type=str, help="the music to play")
        parser.add_argument("--left", "-l", type=str, metavar="key", default="a", help="left key (default: a)")
        parser.add_argument("--right", "-r", type=str, default="s", metavar="key", help="right key (default: s)")
        parser.add_argument("--exit", "-e", type=str, default="m", metavar="key", help="exit key (default: m)")
        parser.add_argument("--sync", "-s", type=int, default=1, metavar="bpm", help="the bpm of the song (default: 1, if value is less than 1, it sets bpm to 1)")
        parser.add_argument("--offset", "-o", type=int, default=0, metavar="ms", help="the offset of every tick")
        parser.add_argument("--snap", "-sd", type=int, default=1, metavar="snap", help="the snap")
        
        args = parser.parse_args()
        left = args.left
        right = args.right
        music = args.music
        exit_key = args.exit
        bpm = args.sync if args.sync > 0 else 1
        tickd = round(60000/bpm)/args.snap
        offset = args.offset
        
        print("Click Space to start the song!")
        with k.Listener(on_press=click, on_release=release) as listener:
            listener.join()
        
        raise KeyboardInterrupt
             
    except KeyboardInterrupt:
        p("Bookmarks: " + (",".join(str(e) for e in bookmark)))
        
