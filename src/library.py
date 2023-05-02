import matplotlib.pyplot as plt
import numpy as np

def buat_garis(Gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb):
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    dy = y2 - y1
    dx = x2 - x1
    if dy <= dx:
        my = dy / dx
        for j in range(x1, x2):
            i = int(my * (j - x1) + y1)
            x = j
            y = i
            # if y % 50:
            print('x, y = ', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)
            x = i
            y = j
            # if x % 50:
            print('x, y = ', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    return Gambar

def buat_titik(canvas, color, r, x, y):
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if ((i - x) ** 2 + (j - y) ** 2) <= (r ** 2):
                canvas[j, i] = color 
    return canvas

# def garis(Gambar, y1, x1, y2, x2, pr, pg, lr, lg):
#     #The user informs the coordinates of the two points for the line.
#     row, col = int(500), int(500)
#     # y1,x1 = 50,50
#     # y2,x2 = 50,450

#     # y1,x1  = 50,50
#     # y2,x2 = 450,70

#     # y1,x1  = 50,50
#     # y2,x2 = 450,50

#     # memnentukan warna
#     point_color=[180, 136 ,17]
#     line_color=[220, 220, 220]

#     dy = y2 - y1
#     dx = x2 - x1

#     # Membuat garis horizontal
#     if abs(dx) > abs(dy):
#         my = dy/dx
#         for x in range(x1, x2+1):
#             y = round(my*(x-x1)+y1)
#             Gambar[y,x,:] = point_color
#     # Membuat garis vertikal
#     else:
#         mx = dx/dy
#         for y in range(y1, y2+1):
#             x = round(mx*(y-y1)+x1)
#             Gambar[y,x,:] = point_color


def vertikal(Gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb):
    hasil = buat_garis(Gambar, y1, x1, y2, x2, hd, hw, pr, pg, pb, lr, lg, lb)

    plt.figure()
    plt.imshow(hasil)
    plt.show()
    
def titik(canvas, color, r, x, y):
    hasil = buat_titik(canvas, color, r, x, y)
    
    plt.figure()
    plt.imshow(hasil)
    plt.show()
    