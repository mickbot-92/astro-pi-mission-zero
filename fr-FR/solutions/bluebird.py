from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
w = (255, 255, 255) # blanc
x = (0, 0, 0) # noir
g = (0,255,0) # vert
s = (180,180,180) # argenté
r = (255,0,0) # rouge
c = (66, 220, 240) # cyan
o = (180,100,0) # orange
b = (0, 0,255) # bleu

picture = [
    c, c, c, c, c, c, c, c,
    c, c, b, b, b, c, c, c,
    c, b, b, x, b, b, c, c,
    c, b, b, b, b, o, o, c,
    c, b, b, b, b, b, c, c,
    b, b, b, b, b, c, c, c,
    b, b, b, b, b, c, c, c,
    b, b, b, b, b, c, c, c
    ]
    
sense.set_pixels(picture)
