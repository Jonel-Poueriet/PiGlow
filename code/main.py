from PIL import ImageGrab
from PIL import Image

#Grab current screen
#screen = ImageGrab.grab()
file = "4quart.png"
screen = Image.open(file)

width, height = screen.size
print("width and height are ",width, height)

#crops image into 4 quarters, ultimately this zoning should be relative to number of rgb strips program is using

#top left
zone_color_top_left = screen.crop((0, 0, width/2, height/2)).getcolors(maxcolors=1000000)

#top right
zone_color_top_right = screen.crop(((width/2), 0, width, height/2)).getcolors(maxcolors=1000000)

#bottom left
zone_color_bottom_left = screen.crop((0, (height/2), width/2, height)).getcolors(maxcolors=1000000)

#bottom right
zone_color_bottom_right = screen.crop(((width/2), (height/2), width, height)).getcolors(maxcolors=1000000)

average_color_tl = max(zone_color_top_left, key=lambda x: x[0])[1]
print("average color is ", average_color_tl)

average_color_tr = max(zone_color_top_right, key=lambda x: x[0])[1]
print("average color is ", average_color_tr)

average_color_bl = max(zone_color_bottom_left, key=lambda x: x[0])[1]
print("average color is ", average_color_bl)

average_color_br = max(zone_color_bottom_right, key=lambda x: x[0])[1]
print("average color is ", average_color_br)

Image.new("RGB", (width, height), average_color_tl).show()
Image.new("RGB", (width, height), average_color_tr).show()
Image.new("RGB", (width, height), average_color_bl).show()
Image.new("RGB", (width, height), average_color_br).show()