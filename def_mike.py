import pygame as pg
import os
import random

all_music = 'musica'

musica = os.listdir(all_music)

musica_rep = []

def cancion_actual():
    for cancion in musica:
        if os.path.isfile(os.path.join(all_music, cancion)) and cancion.endswith('.mp3'):
            musica_rep.append(cancion)

def play_Music():
    cancion_actual()
    pg.mixer.init()
    cancion_rep = random.choice(musica_rep)
    pg.mixer.music.load("musica/" + cancion_rep)
    pg.mixer.music.play(0)


def pause_Music():
    pg.mixer.init()
    pg.mixer.music.pause()


def unpause_Music():
    pg.mixer.init()
    pg.mixer.music.unpause()

def stop_Music():
    pg.mixer.init()
    pg.mixer.music.stop()

def play_again_music():
    pg.mixer.init()
    pg.mixer.music.rewind()