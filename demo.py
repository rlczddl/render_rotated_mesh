import sys
import os
import numpy as np
from tqdm import tqdm
from vedo import *

def render(mesh_file, output_path):
    os.makedirs(output_path, exist_ok=True)

    vp = Plotter(axes=0, size=(800, 800), interactive=0, offscreen=0)
    mesh = load(mesh_file)
    mesh.computeNormals()
    mesh.phong()
    mesh.lighting("glossy")
    vp += mesh
    
    step = 3
    for i in tqdm(range(int(360 / step)), ncols = 100):
        vp.show(zoom = 1.0, bg = "white", interactive = 0)
        vp.camera.Azimuth(step)
        screenshot(os.path.join(output_path, str(10000+(i+0)*step).zfill(5) + ".png"))
    vp.show(zoom = 1.0, bg = "white", interactive = 1)
    vp.close()

def render_with_texture(mesh_file, texture_file, output_path):
    os.makedirs(output_path, exist_ok=True)

    vp = Plotter(axes=0, size=(800, 800), interactive=0, offscreen=0)
    mesh = load(mesh_file).texture(texture_file)
    mesh.computeNormals()
    mesh.phong()
    mesh.lighting("glossy")
    vp += mesh
    
    step = 3
    for i in tqdm(range(int(360 / step)), ncols = 100):
        vp.show(zoom = 1.0, bg = "white", interactive = 0)
        vp.camera.Azimuth(step)
        screenshot(os.path.join(output_path, str(10000+(i+0)*step).zfill(5) + ".png"))
    vp.show(zoom = 1.0, bg = "white", interactive = 1)
    vp.close()

if __name__ == "__main__":
    render("./Armadillo.ply", "./output")
    #render_with_texture("./str_model.obj", "texture.jpg", "./output")

