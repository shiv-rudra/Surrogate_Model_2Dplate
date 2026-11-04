import gmsh
import skfem
def make_plate_mesh(W, H, r, h, e, path,show=False):
    gmsh.initialize()
    gmsh.model.add("plate")
    plate = gmsh.model.occ.addRectangle(0,0,0,W,H)
    hole = gmsh.model.occ.addDisk(W/2,H/2+e,0,r,r)
    gmsh.model.occ.cut([(2, plate)], [(2, hole)])
    gmsh.model.occ.synchronize()
    gmsh.option.setNumber("Mesh.MeshSizeMax", h)
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.setOrder(2)
    gmsh.write(path)
    if show: 
        gmsh.fltk.run()
    gmsh.finalize()

if __name__ == "__main__":
    path1 = "data/plate_10.msh"
    path2 = "data/plate_5.msh"
    path3 = "data/plate_2_5.msh"

    make_plate_mesh(200,100,10,10,0,path1,True)
    make_plate_mesh(200,100,10,5,0,path2)
    make_plate_mesh(200,100,10,2.5,0,path3)
    
    m1 = skfem.Mesh.load(path1)
    m2 = skfem.Mesh.load(path2)
    m3 = skfem.Mesh.load(path3)
    
    print(m1)
    print(m2)
    print(m3)