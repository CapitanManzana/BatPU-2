from assembler import assemble
from schematic import make_schematic

def main():
    program = 'clearRegister'
    
    as_filename = f'programs/{program}.as'
    mc_filename = f'programs/{program}.mc'
    schem_filename = f'{program}program.schem'
    schem_path = f'C:/Users/manza/curseforge/minecraft/Instances/Computacion/config/axiom/blueprints/Schematics Code/'

    assemble(as_filename, mc_filename)
    make_schematic(mc_filename, schem_filename,schem_path)

if __name__ == '__main__':
    main()