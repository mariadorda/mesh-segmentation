import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
import numpy as np
from sklearn.cluster import spectral_clustering
import igl as igl

# Cargar la malla
sv, sf = igl.read_triangle_mesh("C:\\Users\\maria\\Downloads\\mesh-segmentation\\Threshold_Porcelain_Teapot_White\\meshes\\model.obj")



def adjacency_matrix_faces(sf):
    num_faces = len(sf)
    num_vertices = np.max(sf) + 1
    adjacency = np.zeros((num_faces, num_faces), dtype=int)

    # Para cada cara, encontramos las caras adyacentes
    for i in range(num_faces):
        for j in range(num_faces):
            # Si comparten dos vértices, son caras adyacentes
            if i != j:
                common_vertices = np.intersect1d(sf[i], sf[j])
                if len(common_vertices) == 2:
                    adjacency[i, j] = 1
                    adjacency[j, i] = 1

    return adjacency

# Calcular la matriz de adyacencia y realizar el clustering
A = adjacency_matrix_faces(sf)
labels = spectral_clustering(A)

'''
X = sv[:,0]
Y = sv[:,1]
Z = sv[:,2]
triang = sf  

# Obtener el mapa de colores
cmap = plt.cm.viridis

# Mapear los labels a colores
norm = plt.Normalize(vmin=np.min(labels), vmax=np.max(labels))
colors = cmap(norm(labels))

# Crear la figura
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar la malla con colores
ax.plot_trisurf(X, Y, Z, triangles=triang, cmap=cmap, shade=True, facecolors=colors)
#ax.plot_trisurf(X, Y, Z, triangles=triang, cmap=cmap)

# Añadir etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Mesh Segmentation')

# Mostrar el gráfico
plt.show()
'''