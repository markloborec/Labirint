import pygame.font

LEVEL_MAP = [
'                            ',
'                            ',
'                            ',
'       XXXX           XX    ',
'   P           O            ',
'XXXXX         XX         XX ',
' XXXX       XX              ',
' XX    X  XXXX    XX  XX   ',
'       X  XXXX    XX  XXX   ',
'O   XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

LEVEL_2 = [
'  XXXXO        OXXXX        ',
'      X       XXXX       XX ',
'                            ',
'       XXXX           XX    ',
'   P           O            ',
'XXXXXX        XX         XX ',
' XXXX       XX    O         ',
' XX    X  XXXX    XX  XX    ',
'       X  XX          XXX   ',
'    XXXX  XXXOXX      XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']


LEVEL_3 = [
'  XXXXO        OXXXX        ',
'      X       XXXX       XX ',
'         P          O       ',
'       XXXX         XXX     ',
'     O        O            X',
'XXXXXX        XX         XX ',
' XXXX  O    XX    XXXX      ',
' XX    X  XXXX    XX  XX    ',
'      O    X          XXX   ',
'    XXXX  XXXOXX  O    XXX  ',
'XXXXXXXX  XXXXX  XX  XXXX  ']

LEVEL_4 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "  P  X  X               O    XX",
"X  X  X  X  XXXX  X  X  X  XXXX",
"X  X        XO    X  X  X  X  X",
"XXXXXXX  XXXXXXXXXX  X  X  X  X",
"X  O     X  X  X  O  X  X     X",
"XXXXXXXX X  X  XXXXXXXXXXXXX  X",
"X  O                       X  X",
"XXXXXXXXXX  XXXXXXX  XXXX  X  X",
"X           X           X  XO X",
"X  XXXX  XXXXXXXXXXXXX  X  XXXX",
"X   O X  X O            X  O  X",
"X XXXXX  XXXX  X  X  X  XXXX  X",
"X     X OX     X  X  X    OXXXX",
"XXXX  XXXXXXX  XXXX  XXXXXXX  X",
"X     X  X     O  X     X     X",
"X  X  X  X  X  X  X  XXXXXXX  X",
"X  X     X  X  X  X  X     X  X",
"X XXXXX  X  XXXXXXX  XXXX  X  X",
"X OX    OX    OXO    X ",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXX", ]


TILE_SIZE = 20
width = 1500
height = 768

LEVELS = [LEVEL_4]
CURENT_LEVEL = 0
BG_COLOR = "#060C17"
PLAYER_COLOR = "#C4F7FF"
TILE_COLOR = "#94D7F2"
COIN_COLOR = "#ebe134"
FONT = pygame.font.SysFont("Times New Roman",50)
TEXT_COLOR = "#ffffff"


CAMERA_BORDERS = {
    "left" : 600,
    "right" : 500,
    "top" : 700,
    "botom" : 850,
}