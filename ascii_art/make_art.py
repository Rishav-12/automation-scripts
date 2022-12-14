import PIL.Image
import sys

path = sys.argv[1]
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image, new_width = 30):
  width, height = image.size
  new_height = new_width * height // width
  return image.resize((new_width, new_height))

def to_greyscale(image):
  return image.convert("L")

def pixel_to_ascii(image):
  pixels = image.getdata()
  ascii_str = ""
  for pixel in pixels:
    ascii_str += ASCII_CHARS[pixel // 25]
  return ascii_str

image = PIL.Image.open(path)
image = resize(image)
greyscale_image = to_greyscale(image)
ascii_str = pixel_to_ascii(greyscale_image)

img_width = greyscale_image.width
ascii_str_len = len(ascii_str)
ascii_img = ""

for i in range(0, ascii_str_len, img_width):
  ascii_img += ascii_str[i:i+img_width] + "\n"

with open("ascii_img.txt", "w") as ascii_drawing:
  ascii_drawing.write(ascii_img)
