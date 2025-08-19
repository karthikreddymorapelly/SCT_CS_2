from PIL import Image

# Open the encrypted image
img = Image.open("encrypted.png")
pixels = img.load()

# Simple key (same as used in encryption)
key = 50

# Decrypt each pixel
for x in range(img.width):
    for y in range(img.height):
        r, g, b = pixels[x, y]
        pixels[x, y] = (r ^ key, g ^ key, b ^ key)  # XOR reverse

# Save decrypted image
img.save("decrypted.png")
print("Decryption complete. Saved as decrypted.png")
