
import bpy

# Define los parámetros que deseas pasar al operador
params = {
    'action': 'assignMaterials',
    'k': 3,         # Cantidad de clusters
    'delta': 0.03,  # delta: cerca de 0 da más relevancia a distancias angulares, cerca de 1 a distancias geodésicas
    'eta': 0.15,    # eta: cerca de 0 da más importancia a los ángulos cóncavos, cerca de 1 trata igual a ángulos cóncavos y convexos
    'ev_method': 'sparse',  # Cómo calcula autovalores
    'kmeans_init': 'liu_zhang'  # Cómo elige centros de k-means
}

# Llama al operador con los parámetros definidos
bpy.ops.mesh.mesh_segmentation(**params)


# Define la ruta donde se guardará la imagen
ruta_imagen = "C:\\Users\\maria\\Downloads\\mesh-segmentation\\imagen.png"

# Configura la resolución de la imagen
bpy.context.scene.render.resolution_x = 1920  # Ancho de la imagen
bpy.context.scene.render.resolution_y = 1080  # Alto de la imagen

# Renderiza la imagen
bpy.ops.render.render(write_still=True)

# Guarda la imagen en la ubicación especificada
bpy.data.images['Render Result'].save_render(ruta_imagen)
