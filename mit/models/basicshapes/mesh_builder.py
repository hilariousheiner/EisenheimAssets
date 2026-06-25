# A python utility class for creating pythonSCAD polyhedra.
# License: MIT
# Copyright (c) 2026 Heiner Schmidt

from pythonscad import *

def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])
    
def mul(v, s):
    return (v[0] * s, v[1] * s, v[2] * s)

class MeshBuilder: 
    def __init__(self):
        self.vertices = []; 
        self.triangles = [];
        self.groups = [];
        self.midoints = {};
        
    def add_group(self, group=None):
        if group is None: 
            group = []
        
        index = len(self.groups)
        self.groups.append(group)
        return index
        
    def add_vertex(self, v):
        index = len(self.vertices)
        self.vertices.append(v)
        return index
      
    def add_triangle(self, a, b, c):
        self.triangles.extend([a,b,c])
      
    def fan_triangulate(self, groupID, apex, reverse=False):
       group = self.groups[groupID]
       
       for i in range(len(group)):
            p0 = group[i]
            p1 = group[(i + 1) % len(group)]

            if reverse:
                self.add_triangle(apex, p1, p0)
            else:
                self.add_triangle(apex, p0, p1)
    
    def get_polyhedron(self):
        faces = []

        for i in range(0, len(self.triangles), 3):
            faces.append([
                self.triangles[i],
                self.triangles[i + 1],
                self.triangles[i + 2]
            ])

        return polyhedron(points=self.vertices, faces=faces)