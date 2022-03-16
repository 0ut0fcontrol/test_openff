# %%
# Load a molecule into the OpenFF Molecule object
from openff.toolkit.topology import Molecule
molecule = Molecule.from_file('example.mol.ob.sdf')

# Create an OpenFF Topology object from the molecule
from openff.toolkit.topology import Topology
topology = Topology.from_molecules(molecule)

# Load the latest OpenFF force field release: version 2.0.0, codename "Sage"
from openff.toolkit.typing.engines.smirnoff import ForceField
forcefield = ForceField('openff-2.0.0.offxml')

# Create an OpenMM system representing the molecule with SMIRNOFF-applied parameters
openmm_system = forcefield.create_openmm_system(topology)

# %%
import parmed

# Convert OpenMM System to a ParmEd structure.
parmed_structure = parmed.openmm.load_topology(
    topology.to_openmm(), openmm_system, molecule.conformers[0]
)

# %%
# Export GROMACS files.
parmed_structure.save("system.top", overwrite=True)
parmed_structure.save("system.pdb", overwrite=True)


