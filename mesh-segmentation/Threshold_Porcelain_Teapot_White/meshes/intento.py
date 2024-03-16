import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
import numpy as np
from sklearn.cluster import spectral_clustering
import igl as igl

# Cargar la malla
sv, sf = igl.read_triangle_mesh("C:\\Users\\maria\\Downloads\\mesh-segmentation\\Threshold_Porcelain_Teapot_White\\meshes\\model.obj")

# Calcular la matriz de adyacencia y realizar el clustering
A = igl.adjacency_matrix(sf)
labels = spectral_clustering(A)

# Obtener un mapa de colores personalizado basado en el número de clusters
cmap = ListedColormap(plt.cm.tab10(np.linspace(0, 1, len(np.unique(labels)))))

# Crear la figura
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar cada triángulo de la malla con su respectivo color de cluster
for i in range(len(sf)):
    triangle = [sv[sf[i][0]][:2], sv[sf[i][1]][:2], sv[sf[i][2]][:2]]  # Tomar solo las dos primeras columnas (x, y)
    tri = plt.Polygon(triangle, closed=True, facecolor=cmap(labels[i]))
    ax.add_collection3d(tri)

# Ajustar el rango de ejes para que la malla sea completamente visible
ax.auto_scale_xyz(sv[:,0], sv[:,1], sv[:,2])

# Añadir etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Mesh Segmentation')

# Mostrar el gráfico
plt.show()