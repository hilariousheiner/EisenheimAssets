# star.py
# License: MIT
# Copyright (c) 2026 Heiner Schmidt

from pythonscad import *
from mesh_builder import MeshBuilder

meshBuilder = MeshBuilder()

r = 1.0
h = 0.5

A = meshBuilder.add_vertex([0.0, 0.0, r])
B = meshBuilder.add_vertex([r, 0.0, 0.0])
C = meshBuilder.add_vertex([0.0, 0.0, -r])
D = meshBuilder.add_vertex([-r, 0.0, 0.0])

AB = meshBuilder.add_midpoint(A, B)
BC = meshBuilder.add_midpoint(B, C)
CD = meshBuilder.add_midpoint(C, D)
DA = meshBuilder.add_midpoint(D, A)

meshBuilder.scale_group([AB, BC, CD, DA], 0.6)

apexTop = meshBuilder.add_vertex([0.0, h / 2.0, 0.0])
apexBottom = meshBuilder.add_vertex([0.0, -h / 2.0, 0.0])

border = meshBuilder.add_group([A, AB, B, BC, C, CD, D, DA])

meshBuilder.fan_triangulate(border, apexTop)
#meshBuilder.fan_triangulate(border, apexBottom, True)

mesh = meshBuilder.get_polyhedron()
mesh.show()