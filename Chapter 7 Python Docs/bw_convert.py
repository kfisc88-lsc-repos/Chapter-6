def blackAndWhite(image):
    """Converts an image to black and white"""
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if(average < 128):
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)