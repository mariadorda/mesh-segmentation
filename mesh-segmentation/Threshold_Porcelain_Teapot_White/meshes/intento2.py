import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import igl as igl
from sklearn.cluster import spectral_clustering

# Leer la malla
sv, sf = igl.read_triangle_mesh("C:\\Users\\maria\\Downloads\\mesh-segmentation\\Threshold_Porcelain_Teapot_White\\meshes\\model.obj")
A = igl.adjacency_matrix(sf)
labels = spectral_clustering(A)

# Calcular los clusters de las caras
face_clusters = np.zeros(len(sf), dtype=int)
for i, face in enumerate(sf):
    vertex_labels = labels[face]
    unique_labels, counts = np.unique(vertex_labels, return_counts=True)
    most_common_label = unique_labels[np.argmax(counts)]
    face_clusters[i] = most_common_label

# Crear la colección de polígonos tridimensionales
polygons = Poly3DCollection([sv[face] for face in sf], alpha=1.0, linewidths=0.5)

# Obtener el mapa de colores
cmap = plt.cm.viridis
norm = plt.Normalize(vmin=np.min(face_clusters), vmax=np.max(face_clusters))
mapper = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
face_colors = mapper.to_rgba(face_clusters)

# Configurar el color de cada polígono según el cluster
polygons.set_facecolor(face_colors)

# Configurar el gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Agregar la colección de polígonos al gráfico
ax.add_collection3d(polygons)

# Configurar los límites del gráfico
ax.set_xlim(np.min(sv[:, 0]), np.max(sv[:, 0]))
ax.set_ylim(np.min(sv[:, 1]), np.max(sv[:, 1]))
ax.set_zlim(np.min(sv[:, 2]), np.max(sv[:, 2]))

# Mostrar el gráfico
plt.show()