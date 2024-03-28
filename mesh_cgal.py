import CGALPY_epec

#from CGAL.CGAL_Mesh_Segmentation import sdf_values, segmentation_via_sdf_values


# Ruta al archivo de la malla
mesh_file = "model.obj"

# Cargar la malla tridimensional
mesh = CGALPY_epec.Mesh_3()
mesh.load(mesh_file)

# Acceder a los vértices y caras de la malla
vertices = mesh.vertices
faces = mesh.faces

#labels = segmentation_via_sdf_values(mesh)