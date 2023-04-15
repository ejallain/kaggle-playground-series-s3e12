# simple utility functions specific for Jupyter notebooks

def proj_path_setup():
    '''
    appends the src directory to path to allow for module use
    also returns the project directory path
    '''
    from pyprojroot import here
    import os
    import sys

    proj_dir = here()
    src_dir = os.path.join(proj_dir, 'src')
    sys.path.append(src_dir)
    return(proj_dir)