

import pygame as pg
from matrix_functions import *

class Object3D:
    def __init__(self,render):
        self.color = pg.Color(255,0,0)
        self.render = render
        self.vertexes = np.array([(0,0,0,1),(0,1,0,1),(1,1,0,1),(1,0,0,1),
                                  (0,0,1,1),(0,1,1,1),(1,1,1,1),(1,0,1,1)])
        self.faces = np.array([
            (0,1,2,3),(4,5,6,7),(0,4,5,1),(2,3,7,6),(1,2,6,5),(0,3,7,4)
        ])

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        vertexes = self.vertexes @ self.render.camera.camera_matrix()
        vertexes = vertexes @ self.render.projection.projection_matrix
        vertexes /= vertexes[:,-1].reshape(-1,1)
        vertexes[(vertexes > 2) | (vertexes < -2)] = 0
        vertexes = vertexes @ self.render.projection.to_screen_matrix
        vertexes = vertexes[:,:2]

        for face in self.faces:
            polygon = vertexes[face]
            if not np.any((polygon == self.render.H_WIDTH) | (polygon == self.render.H_HEIGHT)):
                pg.draw.polygon(self.render.screen, self.color, polygon)

    def translate(self,pos):
        self.vertexes = self.vertexes @ translate(pos)
    def scale(self,scale_to):
        self.vertexes = self.vertexes @ scale(scale_to)
    def rotate(self,typ,angle):
        if typ.lower == "x":
            self.vertexes = self.vertexes @ rotate_x(angle)
        if typ.lower == "y":
            self.vertexes = self.vertexes @ rotate_y(angle)
        if typ.lower == "z":
            self.vertexes = self.vertexes @ rotate_z(angle)