import sys

import pygame as pg


NAME_TO_RGBA = pg.color.THECOLORS
RGBA_TO_NAME = {}
for name, rgb in NAME_TO_RGBA.items():
    if rgb in RGBA_TO_NAME:
        RGBA_TO_NAME[rgb].append(name)
    else:
        RGBA_TO_NAME[rgb] = [name]
        

class ColorPicker(object):
    def __init__(self):
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 60
        self.screen = pg.display.set_mode((768, 576))
        pg.display.set_caption("Color Picker")
        
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            elif event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.quit()               
    
    def update(self, dt):
        pass
        
    def draw(self):
        self.screen.fill(pg.Color("black"))

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()
            
    def quit(self):
        self.done = True
        
        
if __name__ == "__main__":
    pg.init()
    app = ColorPicker()
    app.run()
    pg.quit()
    sys.exit()