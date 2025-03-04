import os

from PIL import Image, ImageOps

path = r"C:\Users\arthu\source\repos\Honor In (after 8 12 2023)\textures"
os.chdir(path)

print("Current working directory:", os.getcwd())  # Verify the change


# Load the original 512x512 images
cat = Image.open("input.jpg")
logo = Image.open("logo.jpg")

gyro = Image.open("gyro.png")
gyro.thumbnail((512, 512))
gyro = gyro.convert("RGB")
gyro = ImageOps.invert(gyro)

#beacon = Image.open("beaconNight.jpg")
beacon = Image.open("beacon.jpg")
beacon.thumbnail((512, 512))

gun = Image.open("gun2.jpg")
gun.thumbnail((512, 512))

sword = Image.open("sword.jpg")
sword.thumbnail((512, 512))


reload = Image.open("reload.jpg")
reload.thumbnail((512, 512))

bigBen = Image.open("bigBen.jpg")
bigBen.thumbnail((512, 512))


# Create a new blank 5120x5120 image
new_img = Image.new("RGB", (5120, 5120))

# Tile the image 10x10 times
for i in range(10):
    for j in range(10):
        if i == 0 and j == 0:
            new_img.paste(logo, (i * 512, j * 512))
        elif i == 1 and j == 0:
            new_img.paste(gyro, (i * 512, j * 512))
        elif i == 2 and j == 0:
            new_img.paste(beacon, (i * 512, j * 512))
        elif i == 3 and j == 0:
            new_img.paste(gun, (i * 512, j * 512))
        elif i == 4 and j == 0:
            new_img.paste(sword, (i * 512, j * 512))
        elif i == 5 and j == 0:
            new_img.paste(reload, (i * 512, j * 512))
        elif i == 6 and j == 0:
            new_img.paste(bigBen, (i * 512, j * 512))
        else:
            new_img.paste(cat, (i * 512, j * 512))

# Save the output
new_img.save("texture.jpg")

new_img.show()