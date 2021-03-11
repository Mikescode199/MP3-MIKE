import tkinter as tk
from tkinter import PhotoImage
from Mp3 import def_mike

class Mp3(tk.Frame):
    def __init__(self, __padre__, *pargs):
        super(Mp3,self).__init__(__padre__, *pargs)

    def __main__(self):
        label = tk.Label(self, text="Music With Mike")
        label.pack()
        label.config(font=("Times New Roman", 20))

        boton_musica = tk.Button(self, text="Play", command=def_mike.play_Music)
        boton_musica.pack(side='left')
        boton_musica.config(font=("Times New Roman", 20))

        boton_pause = tk.Button(self, text="Pause", command=def_mike.pause_Music)
        boton_pause.pack(side='left')
        boton_pause.config(font=("Times New Roman", 20))

        boton_unpause = tk.Button(self, text="Unpause", command=def_mike.unpause_Music)
        boton_unpause.pack(side='left')
        boton_unpause.config(font=("Times New Roman", 20))

        boton_stop = tk.Button(self, text="Stop", command=def_mike.stop_Music)
        boton_stop.pack(side='left')
        boton_stop.config(font=("Times New Roman", 20))

        boton_playagain = tk.Button(self, text="Play again", command=def_mike.play_again_music)
        boton_playagain.pack(side='left')
        boton_playagain.config(font=("Times New Roman", 20))


        # def play_Music(self):
        #     pg.mixer.init()
        #     pg.mixer.music.load(musica)
        #     pg.mixer.music.play(0)
        #

if __name__ == "__main__":
    screen = tk.Tk()
    screen.geometry("500x500")
    screen.title("Mp3 Mike")
    imagen = PhotoImage(file="musica/fondo.png")
    #screen.resizable(0, 0)
    background = tk.Label(image=imagen, text="Imagen S.O de fondo")
    background.place(x=0, y=0, relwidth=1, relheight=1)

    #Aqui comienza nuestro objeto
    nuevo_mp3 = Mp3(screen)
    nuevo_mp3.pack()
    nuevo_mp3.__main__()
    screen.mainloop()

