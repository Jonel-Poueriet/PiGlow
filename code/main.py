import tkinter as tk
from PIL import ImageGrab
import time

#updated virtual led color
def update_color(color):
    canvas.delete("all")
    canvas.create_oval(50, 50, 250, 250, fill=color, outline=color)

#turns rgb color format (x, y, z) -> hex color equivalent
def rgb_to_hex(rgb):
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

#set up led window
root = tk.Tk()
root.title("Virtual RGB LED")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

#runs until virtual led window is closed
while True:
    #Grab current screen
    screen = ImageGrab.grab()

    #file = "4quart.png"
    #screen = Image.open(file)

    width, height = screen.size
    #print("width and height are ",width, height)

    #crops image into 4 quarters, ultimately this zoning should be relative to number of rgb strips program is using

    #top left
    #zone_color_top_left = screen.crop((0, 0, width/2, height/2)).getcolors(maxcolors=1000000)
    #average_color_tl = max(zone_color_top_left, key=lambda x: x[0])[1]
    #colorhex_tl = rgb_to_hex(average_color_tl)

    #top right
    #zone_color_top_right = screen.crop(((width/2), 0, width, height/2)).getcolors(maxcolors=1000000)
    #average_color_tr = max(zone_color_top_right, key=lambda x: x[0])[1]
    #colorhex_tr = rgb_to_hex(average_color_tr)

    #bottom left
    #zone_color_bottom_left = screen.crop((0, (height/2), width/2, height)).getcolors(maxcolors=1000000)
    #average_color_bl = max(zone_color_bottom_left, key=lambda x: x[0])[1]
    #colorhex_bl = rgb_to_hex(average_color_bl)

    #bottom right
    #zone_color_bottom_right = screen.crop(((width/2), (height/2), width, height)).getcolors(maxcolors=1000000)
    #average_color_br = max(zone_color_bottom_right, key=lambda x: x[0])[1]
    #colorhex_br = rgb_to_hex(average_color_br)
    #print("average color is ",average_color_br)
    
    screencolors = screen.getcolors(maxcolors=1000000)
    average_color_total = max(screencolors, key=lambda x: x[0])[1]
    colorhex = rgb_to_hex(average_color_total)
    #print("hex color is ",colorhex)

    update_color(colorhex)
    root.update()
    #root.after()  # Wait for .5 second
    time.sleep(1)