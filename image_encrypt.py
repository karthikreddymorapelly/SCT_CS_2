from PIL import Image

# Open and convert image to RGB
img = Image.open("image.png").convert("RGB")
pixels = img.load()

width, height = img.size

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]   # now it will work
        # simple encryption (example: invert colors)
        pixels[x, y] = (255-r, 255-g, 255-b)

# Save encrypted image
img.save("encrypted.png")
print("Encryption complete. Saved as encrypted.png")

