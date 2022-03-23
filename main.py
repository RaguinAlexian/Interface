from tkinter import *
from tkinter import ttk

def both():
    tir()
    deplaceDisque()
    start_anim()

def tir():
    global xo, yo, t, dt, r, vox, voy, g, dessin, oval, jeu, anim
    t += dt/1000  # Conversion en s
    x, y = xo+vox*t, yo+voy*t+1/2*g*t**2
    if 0 < x < xmax and 0 < y < ymax:
        dessin.coords(oval, x, y, x+d, y+d)
    if anim:
        jeu.after(6,tir)

def deplaceDisque():
   global x, y, dx, dy, anim
   x, y = x+dx, y+dy
   if x > L-d-m: # Tourner d’1/4 de tour = descendre => dx = 0 et dy > 0
      x, dx, dy = L-d-m, 0, pas
   if y > L-d-m: # Tourner d’1/4 de tour = reculer horizontalement => dx < 0 et dy = 0
      y, dx, dy = L-d-m, -pas, 0
   if x < m: # Tourner d’1/4 de tour = monter => dx = 0 et dy < 0
      x, dx, dy = m, 0, -pas
   if y < m: # Tourner d’1/4 de tour = avancer horizontalement => dx > 0 et dy = 0
      y, dx, dy = m, pas, 0
   dessin.coords(Joueur,x,y,x+d,y+d)
   if anim:
      jeu.after(50,deplaceDisque)

def stop_anim(): # Stopper l’animation (bouton « Arrêter »)
   global anim
   anim = False

def start_anim(): # Lancer/relancer l’animation (bouton « Démarrer »)
   global anim
   if not anim: # Pour éviter que le bouton ne puisse lancer plusieurs boucles
      anim =True
      tir()
      deplaceDisque()

# Paramétrage
H, L = 300, 300  # Taille canevas
m = 10 # Marge entre le disque et le bord du canvas
d = 10  # Diamètre du projectile
xo, yo = 10, 280  # Position initiale (1 px = 1 m)
t, dt = 0, 10  # Temps et pas temporel en ms
xmax, ymax = L-d, H-d  # Valeur max des coordonnées
vox, voy = 15, -70  # Coordonnées vitesse initiale
g = 10  # Accélération pesanteur
x, y = m, m # Position initiale du disque
pas = 15 # Pas du déplacement
dx, dy = pas, 0 # Déplacement initial horizontal (dy=0) de gauche à droite (dx>0)
xf, yf = 210, 210       # coordonnées finales du disque
anim = False # Variable booléenne

jeu = Tk()

dessin = Canvas(jeu,bg='dark grey',height=H, width=L)
dessin.pack(side=LEFT, padx =5, pady =5)

Joueur = dessin.create_oval(x, y, x+d, y+d, width=2, fill='green')
oval = dessin.create_oval(xo, yo, xo+d, yo+d, width=2, fill='red')

boutQ = Button(jeu, text='Quitter', width=8, command=jeu.destroy)
boutQ.pack(side=BOTTOM, padx=5, pady=5)
boutD = Button(jeu, text='Démarrer', width=8, command=both)
boutD.pack(padx=5, pady=5)
boutA = Button(jeu, text='Arrêter', width =8, command=stop_anim)
boutA.pack(padx =5, pady =5)




jeu.mainloop()
