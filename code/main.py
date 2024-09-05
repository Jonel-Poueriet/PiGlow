import tkinter as tk
from PIL import ImageGrab
import time

#updated virtual led color
def update_color(color):
    #reformat virtual led window with new color
    canvas.delete("all")
    canvas.create_oval(50, 50, 250, 250, fill=color, outline=color)

#turns rgb color format (x, y, z) -> hex color equivalent
def rgb_to_hex(rgb):
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

#makes the change between colors more gradual by switching to color between old and new color
#intermediate color depends on range, closer to 0 means closer match to old color, closer to 1 means closer match to new color
#returns a rgb triple
def gradual_color_change(curr_color, target_color, range):
    return (
        int(curr_color[0] + (target_color[0] - curr_color[0]) * range),
        int(curr_color[1] + (target_color[1] - curr_color[1]) * range),
        int(curr_color[2] + (target_color[2] - curr_color[2]) * range)
    )

#set up led window
root = tk.Tk()
root.title("Virtual RGB LED")
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

#initialize current startup color to black, this variable keeps track of old color to help fade to new color
current_color = (0, 0, 0)

#determines how "balanced" the fade from colors is, between 0-1, closer to 0 means fade color is closer to current color, closer to 1 means fade color is closer to new color
#.5 means the leds will fade with a color between old and new
transition_speed = .5

#runs until virtual led window is closed
while True:
    #Grab current screen
    screen = ImageGrab.grab()
    
    #file = "4quart.png"
    #screen = Image.open(file)

    #get screen size for screen partitions if applicable
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
    
    #grab colors from current screen
    screencolors = screen.getcolors(maxcolors=1000000)
    
    #find average color to update
    average_color_total = max(screencolors, key=lambda x: x[0])[1]
    
    #get intermediate between current color and new color for smooth transition
    mid_color = gradual_color_change(current_color, average_color_total, transition_speed)
    current_color = average_color_total
    
    #convert led color to hex in order to update
    colorhex = rgb_to_hex(mid_color)
    #print("hex color is ",colorhex)

    #update color
    update_color(colorhex)
    root.update()
    #root.after()  # Wait for .5 second
    #time.sleep(1)