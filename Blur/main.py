from PIL import Image, ImageColor


def GetHSVfromRGB(R, G, B):
    r = R / 255
    g = G / 255
    b = B / 255

    cMax = max(r, g, b)
    cMin = min(r, g, b)
    delta = cMax - cMin

    H = 0
    if delta == 0:
        H = 0
    elif cMax == r:
        H = 60 * (((g - b) / delta) % 6)
    elif cMax == g:
        H = 60 * ((b - r) / delta + 2)
    elif cMax == b:
        H = 60 * ((r - g) / delta + 4)

    S = 0
    if cMax == 0:
        S = 0
    else:
        S = delta / cMax

    V = cMax

    return H, S, V


def GetRGBfromHSV(H, S, V):
    C = V * S
    X = C * (1 - abs(H / 60 % 2 - 1))
    m = V - C

    r = 0
    g = 0
    b = 0

    if 0 <= H < 60:
        r = C
        g = X
        b = 0
    elif 60 <= H < 120:
        r = X
        g = C
        b = 0
    elif 120 <= H < 180:
        r = 0
        g = C
        b = X
    elif 180 <= H < 240:
        r = 0
        g = X
        b = C
    elif 240 <= H < 300:
        r = X
        g = 0
        b = C
    elif 300 <= H < 360:
        r = C
        g = 0
        b = X

    R = (r + m) * 255
    G = (g + m) * 255
    B = (b + m) * 255

    return int(R), int(G), int(B)



image = Image.open("try4.jpg")
pixels = image.load()
width, height = image.size

kernel = [[1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]]


img = Image.new(mode="RGBA", size=(width, height))
newPixels = img.load()

for i in range(2, width - 2):
    for j in range(2, height - 2):
        H = 0
        newS = 0
        V = 0

        x = 0
        y = 0
        for ii in range(i - 2, i + 3):
            for jj in range(j - 2, j + 3):
                rgb = pixels[ii, jj]
                R = rgb[0]
                G = rgb[1]
                B = rgb[2]

                H, S, V = GetHSVfromRGB(R, G, B)
                newS += S * kernel[y][x]
                x += 1
            y += 1
            x = 0

        newS /= 25
        R, G, B = GetRGBfromHSV(H, newS, V)
        newPixels[i, j] = (R, G, B)




img.show()

