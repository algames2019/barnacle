# Barnacle

A helpful tool for making bookmarks for osu!.

## Usage

~~~ text
usage: barnacle [OPTIONS] music
~~~

## Arguments

### Positional Arguments

~~~ text
music - the music to play
~~~

### Optional Arguments

~~~ text
-h, --help            show this help message and exit
  --left key, -l key    left key (default: a)
  --right key, -r key   right key (default: s)
  --exit key, -e key    exit key (default: m)
  --sync bpm, -s bpm    the bpm of the song (default: 1, if value is less than 1, it sets bpm to 1)
  --offset ms, -o ms    the offset of every tick
  --snap snap, -sd snap the snap
~~~

## Installation

~~~ bash
git clone https://github.com/algames2019/barnacle.git
cd barnacle
~~~

### Bash

Do not use with `su` or `sudo`! It can cause many problems.

~~~ bash
./install.sh
~~~
