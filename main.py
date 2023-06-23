from cube import *
from camera import *
from projection import *

import pygame as pg


class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH,self.HEIGHT = 1600,800
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH//2,self.HEIGHT//2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()
        self.smallfont = pg.font.SysFont('Corbel',35)

        self.text = self.smallfont.render('+' , True , pg.Color(255,255,255))


    def create_objects(self):
        self.camera = Camera(self,[0.5,1,-4])
        self.projection = Projection(self)
        self.objects = [

        ]


        #self.object.translate([0,0,0])
        #self.object.scale(0.5)

    def draw(self):
        self.screen.fill(pg.Color('#121212'))
        for rb in self.objects:
            rb.draw()
        self.screen.blit(self.text , (self.WIDTH/2,self.HEIGHT/2))

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == "__main__":
    app = SoftwareRender()
    app.run()
