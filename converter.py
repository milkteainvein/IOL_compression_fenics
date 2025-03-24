import gmsh
import meshio
import vedo

def gmsh_converter(path_name, output_file):
  gmsh.initialize()
  gmsh.open(path_name)

  gmsh.model.mesh.generate(3)

  gmsh.write(output_file)
  gmsh.finalize()

def refine_mesh(mesh_file, output_file, refinement_steps=0):
  gmsh.initialize()
  
  # open the mesh file
  gmsh.open(mesh_file)

  # refine the mesh
  for step in range(refinement_steps):
    gmsh.model.mesh.refine()
  
  gmsh.write(output_file)
  gmsh.finalize()

def optimize_mesh(input_file, output_file):
  # initialize
  gmsh.initialize()
  gmsh.open(input_file)

  # Apply mesh optimization
  gmsh.option.setNumber("Mesh.Optimize", 1)
  gmsh.option.setNumber("Mesh.OptimizeNetgen", 1)  # Better smoothing
  gmsh.model.mesh.optimize("Netgen")  # Runs Netgen's optimization

  # Save the optimized mesh
  gmsh.write(output_file)
  gmsh.finalize()

def show_msh_file(msh_file):
    # Read the .msh file
    mesh = meshio.read(msh_file)

    # Extract points and tetrahedral cells
    points = mesh.points
    cells = mesh.cells_dict.get("tetra", None) 

    # Check if there are tetrahedral elements
    if cells is None or cells.size == 0:
        print("No tetrahedral elements found!")
        return

    # Create a Vedo mesh
    vmesh = vedo.Mesh([points, cells])

    # Show the mesh
    vedo.show(vmesh, axes=True, viewup="z", title="Gmsh Mesh Visualization")


def inspect_file(output_file):
  # Load the .msh file
  mesh = meshio.read(output_file)

  # Print available cell types
  print("Available cell types:", mesh.cells_dict.keys())

  # Print number of elements per type
  for cell_type, elements in mesh.cells_dict.items():
      print(f"{cell_type}: {len(elements)} elements")



def main():
  path_name = "object_files/IOL.STEP"
  mesh_file = "model.msh"
  refinement_steps = 4

  gmsh_converter(path_name, mesh_file)
  optimize_mesh(mesh_file, mesh_file)
  refine_mesh(mesh_file, mesh_file, refinement_steps)
  show_msh_file(mesh_file)
  # inspect_file(output_file)

if __name__ == "__main__":
   main()





