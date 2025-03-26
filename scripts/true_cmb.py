import numpy as np

def true_cmb() -> np.ndarray:
    """
    Generates the true CMB power spectrum using PySM3.
    
    Returns:
        cl_cmb (np.ndarray): true CMB power spectrum.
    """
    
    cl_th = np.loadtxt("https://portal.nersc.gov/project/cmb/pysm-data/pysm_2/camb_lenspotentialCls.dat",skiprows=0, max_rows=382 ,usecols=(1))

    return cl_th