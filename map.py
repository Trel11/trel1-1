from settings import *

text_map = [
    'WWWWWWWWWWWW',
    'W..........W',
    'W..WWWW....W',
    'W.......W..W',
    'W.......W..W',
    'WWW...WWW..W',
    'W......W...W',
    'WWWWWWWWWWWW'
]
w_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            w_map.add((i * TITLE, j * TITLE))
