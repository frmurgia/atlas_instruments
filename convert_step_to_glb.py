"""Convert STEP file to GLB (glTF binary) for web use - optimized for smaller size."""
import cadquery as cq
import json
import struct
import numpy as np

# Load the STEP file
result = cq.importers.importStep("/home/user/atlas_instruments/3dmodel/top+bottom v0.1.stp")

# Tessellate with higher tolerance for fewer polygons
vertices = []
indices = []

offset = 0
for shape in result.solids().vals():
    tess = shape.tessellate(1.0)  # higher tolerance = fewer polys
    verts = tess[0]
    faces = tess[1]

    for v in verts:
        vertices.extend([v.x, v.y, v.z])

    for f in faces:
        indices.extend([f[0] + offset, f[1] + offset, f[2] + offset])

    offset += len(verts)

# Compute proper normals
vert_array = np.array(vertices).reshape(-1, 3)
idx_array = np.array(indices).reshape(-1, 3)
norm_array = np.zeros_like(vert_array)

for tri in idx_array:
    v0, v1, v2 = vert_array[tri[0]], vert_array[tri[1]], vert_array[tri[2]]
    edge1 = v1 - v0
    edge2 = v2 - v0
    n = np.cross(edge1, edge2)
    length = np.linalg.norm(n)
    if length > 0:
        n = n / length
    norm_array[tri[0]] += n
    norm_array[tri[1]] += n
    norm_array[tri[2]] += n

lengths = np.linalg.norm(norm_array, axis=1, keepdims=True)
lengths[lengths == 0] = 1
norm_array = norm_array / lengths

# Center and normalize
center = (vert_array.max(axis=0) + vert_array.min(axis=0)) / 2
vert_array -= center
max_extent = (vert_array.max(axis=0) - vert_array.min(axis=0)).max()
scale_factor = 2.0 / max_extent
vert_array *= scale_factor

print(f"Vertices: {len(vert_array)}, Triangles: {len(idx_array)}")
print(f"Bounds: {vert_array.min(axis=0)} to {vert_array.max(axis=0)}")

# Build GLB
vert_bytes = vert_array.astype(np.float32).tobytes()
norm_bytes = norm_array.astype(np.float32).tobytes()
idx_bytes = idx_array.astype(np.uint32).flatten().tobytes()

def pad4(b):
    r = len(b) % 4
    if r != 0:
        b += b'\x00' * (4 - r)
    return b

buffer_data = pad4(vert_bytes) + pad4(norm_bytes) + pad4(idx_bytes)

vert_min = vert_array.min(axis=0).tolist()
vert_max = vert_array.max(axis=0).tolist()

gltf = {
    "asset": {"version": "2.0", "generator": "cadquery-to-glb"},
    "scene": 0,
    "scenes": [{"nodes": [0]}],
    "nodes": [{"mesh": 0}],
    "meshes": [{
        "primitives": [{
            "attributes": {"POSITION": 0, "NORMAL": 1},
            "indices": 2,
            "material": 0
        }]
    }],
    "materials": [{
        "pbrMetallicRoughness": {
            "baseColorFactor": [0.12, 0.12, 0.12, 1.0],
            "metallicFactor": 0.4,
            "roughnessFactor": 0.6
        },
        "name": "DeviceMaterial"
    }],
    "accessors": [
        {"bufferView": 0, "componentType": 5126, "count": len(vert_array), "type": "VEC3", "min": vert_min, "max": vert_max},
        {"bufferView": 1, "componentType": 5126, "count": len(norm_array), "type": "VEC3"},
        {"bufferView": 2, "componentType": 5125, "count": len(idx_array.flatten()), "type": "SCALAR"}
    ],
    "bufferViews": [
        {"buffer": 0, "byteOffset": 0, "byteLength": len(vert_bytes), "target": 34962},
        {"buffer": 0, "byteOffset": len(pad4(vert_bytes)), "byteLength": len(norm_bytes), "target": 34962},
        {"buffer": 0, "byteOffset": len(pad4(vert_bytes)) + len(pad4(norm_bytes)), "byteLength": len(idx_bytes), "target": 34963}
    ],
    "buffers": [{"byteLength": len(buffer_data)}]
}

json_str = json.dumps(gltf, separators=(',', ':'))
while len(json_str) % 4 != 0:
    json_str += ' '
json_bytes = json_str.encode('utf-8')

glb_length = 12 + 8 + len(json_bytes) + 8 + len(buffer_data)
output_path = "/home/user/atlas_instruments/vue-app/public/tenlooper.glb"

with open(output_path, 'wb') as f:
    f.write(struct.pack('<I', 0x46546C67))
    f.write(struct.pack('<I', 2))
    f.write(struct.pack('<I', glb_length))
    f.write(struct.pack('<I', len(json_bytes)))
    f.write(struct.pack('<I', 0x4E4F534A))
    f.write(json_bytes)
    f.write(struct.pack('<I', len(buffer_data)))
    f.write(struct.pack('<I', 0x004E4942))
    f.write(buffer_data)

print(f"GLB written to {output_path}")
print(f"GLB size: {glb_length / 1024:.1f} KB")
