#Color Picker Challenge

As well as being able to use RGB or RGBA values for colors, Pygame has a dict, color.THECOLORS,
 that maps color-name strings to RGBA values. These names can be passed to pygame.Color() instead of RGB/A values, for example, `pygame.Color("antiquewhite")`. This
 challenge focuses on creating a color-picker tool that allows you to click on a color and see the color's name/s. This challenge is meant to be appropriate for pygamers of all skill levels
 - if you've found the previous challenges too difficult, this is a good chance to snag yourself some sweet flair.
 
###How It Works

The provided code is a minimal pygame app skeleton that handles creating and exiting a pygame window. There are also two dicts provided: NAME_TO_RGBA maps color-name keys to RGBA
 values and RGBA_TO_NAME maps RGBA keys to lists of color-names (some colors have multiple names, "red" and "red1", for example). As always, feel free to ignore the provided code and
 use your own implementation.

###Controls

*ESC* Exit 
 
#Challenge
Display each color in RGB_TO_NAME to the screen. Clicking on a color should display that color's RGBA value and each of its names.

Friendly reminder: Surface.get_at returns a pygame.Color instance, not an RGBA tuple. You can use `tuple(color_instance)` to get an RGBA tuple.


###Achievements

#####Deft Palette
Add the ability to add and remove colors from a palette and save the palette as an image. You may also want to create a text file to accompany the palette image.

#####It Takes All Sorts
Sort the colors displayed to the screen. [Good article about color sorting with python examples](http://www.alanzucconi.com/2015/09/30/colour-sorting/)

Good luck, have fun and feel free to ask for help if you need it.