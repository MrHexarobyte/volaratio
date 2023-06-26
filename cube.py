import pygame as pg
from matrix_functions import *

# The Cube3D class creates a 3D cube object with specified color, position, and size for rendering.
class Cube3D:
    def __init__(self,render,color,pos=[0,0,0],sz=1):
        """
        This function initializes a 3D object with a specified color, rendering method, position, and size.
        
        * #### render
          Application parameter. Renderer() class required.
        * #### color
         The color of the object being rendered
        * #### pos
         The position of the object in 3D space, represented as a list or tuple of three values
        ``(x, y, z)``
        * #### sz
         sz stands for size and it determines the size of the object being created. It is used to
        scale the vertexes of the object, defaults to 1 (optional)
        """
        
        self.color = color
        self.render = render
        s = 1
        self.vertexes = np.array([(0,0,0,s),(0,s,0,s),(s,s,0,s),(s,0,0,s),
                                  (0,0,s,s),(0,s,s,s),(s,s,s,s),(s,0,s,s)])
        self.faces = np.array([
            (0,1,2,3),(4,5,6,7),(0,4,5,1),(2,3,7,6),(1,2,6,5),(0,3,7,4)
        ])
        self.vertexes = self.vertexes @ translate(pos)
        self.vertexes = self.vertexes @ scale(sz)

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
        """
        This function rotates a set of vertexes based on the specified axis and angle.
        
        :param type: a string indicating the axis of rotation ("x", "y", or "z")
        :param angle: The angle (in degrees) by which the object needs to be rotated
        """
        if typ.lower == "x":
            self.vertexes = self.vertexes @ rotate_x(angle)
        if typ.lower == "y":
            self.vertexes = self.vertexes @ rotate_y(angle)
        if typ.lower == "z":
            self.vertexes = self.vertexes @ rotate_z(angle)
