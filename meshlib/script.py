from meshlib import mrmeshpy as mm
from meshlib import mrmeshnumpy as mn
import numpy as np
import meshlib
 
# load mesh
mesh = mm.loadMesh("model.obj")
# extract numpy arrays
verts = mn.getNumpyVerts(mesh)
faces = mn.getNumpyFaces(mesh.topology)
 
print(dir(mrmeshpy))