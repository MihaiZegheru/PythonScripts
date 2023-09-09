from PIL import Image, ImageDraw
from math import floor

# Input file path
INPUT_FILE = "image.jpg"

# Output file path
OUTPUT_FILE = "output.png"

# Color Picking Type
BLUR_COLOR_SELECTION = True

# Background Color
BG_COLOR = "black"

# Space between the painted dots (in pixels)
SPACE_BETWEEN_DOTS = 30
# Border size (in pixels)
BORDER_SIZE = 100
# Input image grid cell surface to dot ratio
PIXEL_DOT_RATIO = 17
# Output image rescale (keep int)
IMAGE_SIZE_MODIFIER = 4


def ComputeElipseCoords(i, j, offsetX, offsetY):
    startX = (offsetX + i * PIXEL_DOT_RATIO * IMAGE_SIZE_MODIFIER)
    startY = (offsetY + j * PIXEL_DOT_RATIO * IMAGE_SIZE_MODIFIER)
    endX = (startX + PIXEL_DOT_RATIO * IMAGE_SIZE_MODIFIER)
    endY = (startY + PIXEL_DOT_RATIO * IMAGE_SIZE_MODIFIER)
    elipseCoords = (startX, startY, endX, endY)

    return elipseCoords


def GetBlurColor(i, j):
    global initialImage
    originalImageStartX = i * PIXEL_DOT_RATIO
    originalImageStartY = j * PIXEL_DOT_RATIO
    originalImageEndX = (i + 1) * PIXEL_DOT_RATIO
    originalImageEndY = (j + 1) * PIXEL_DOT_RATIO

    cellColorR = 0
    cellColorG = 0
    cellColorB = 0
    for ii in range(originalImageStartX, originalImageEndX):
        for jj in range(originalImageStartY, originalImageEndY):
            cellColor = initialImage.getpixel((ii, jj))
            cellColorR += cellColor[0]
            cellColorG += cellColor[1]
            cellColorB += cellColor[2]

    numberOfPixelsPerCell = PIXEL_DOT_RATIO * PIXEL_DOT_RATIO
    cellColorR /= numberOfPixelsPerCell
    cellColorG /= numberOfPixelsPerCell
    cellColorB /= numberOfPixelsPerCell
    color = (int(cellColorR), int(cellColorG), int(cellColorB))

    return color


def GetRawMiddleColor(i, j):
    colorCoords = i * PIXEL_DOT_RATIO + PIXEL_DOT_RATIO / 2, j * PIXEL_DOT_RATIO + PIXEL_DOT_RATIO / 2
    return initialImage.getpixel(colorCoords)


def DrawImage(numberDotsX, numberDotsY, brush):
    offsetX = BORDER_SIZE
    for i in range(0, numberDotsX):
        offsetY = BORDER_SIZE

        for j in range(0, numberDotsY):
            elipseCoords = ComputeElipseCoords(i, j, offsetX, offsetY)

            if BLUR_COLOR_SELECTION:
                color = GetBlurColor(i, j)
            else:
                color = GetRawMiddleColor(i, j)

            brush.ellipse(elipseCoords, color)
            offsetY += SPACE_BETWEEN_DOTS

        offsetX += SPACE_BETWEEN_DOTS


initialImage = Image.open(INPUT_FILE)
initialSizeX, initialSizeY = initialImage.size

numberDotsX = floor(initialSizeX / PIXEL_DOT_RATIO)
numberDotsY = floor(initialSizeY / PIXEL_DOT_RATIO)
newSizeX = 2 * BORDER_SIZE + IMAGE_SIZE_MODIFIER * numberDotsX * PIXEL_DOT_RATIO + (numberDotsX - 1) * SPACE_BETWEEN_DOTS
newSizeY = 2 * BORDER_SIZE + IMAGE_SIZE_MODIFIER * numberDotsY * PIXEL_DOT_RATIO + (numberDotsY - 1) * SPACE_BETWEEN_DOTS
newSize = newSizeX, newSizeY

newImage = Image.new("RGB", newSize, BG_COLOR)
brush = ImageDraw.Draw(newImage)
DrawImage(numberDotsX, numberDotsY, brush)
newImage.save(OUTPUT_FILE)