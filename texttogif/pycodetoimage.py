import time, math
import text_to_image
import texttoimage
from PIL import Image
frames = []
A, B = 0, 0
#encoded_image_path = text_to_image.encode("Hello World!", "image.png")
open('text.txt', 'w').close()
file = open("text.txt", "a")
#file.write("\x1b[2J")
time = 628
while time > 1:
    z = [0] * 1760
    b = [' '] * 1760
    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 22 > y and y > 0 and x > 0 and 80 > x and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]


    #file.write('\x1b[H')
    for k in range(1761):
        file.write((b[k] if k % 80 else '\n'))
        A += 0.00004
        B += 0.00002
    #encoded_image_path = text_to_image.encode_file("text.txt", "frame.png")
    image = texttoimage.textfile_to_image('text.txt')
    #image.show()
    image.save('texttogif/frame.png')
    #new_frame = Image.open(i)
    frames.append(image)

    open('text.txt', 'w').close()
    file = open("text.txt", "a")
    time= time -1
frames[1].save('texttogif/png_to_gif.gif', format='GIF',
                               append_images=frames[1:],
                               save_all=True,
                               duration=100, loop=0)
