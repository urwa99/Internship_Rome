import numpy as np
import healpy as hp
import pysm3
import pysm3.units as u


def gen_sims(nsims: int) -> np.ndarray:
    
    """
    Generates simulated CMB maps using PySM3.
    
    Parameters:
        nsims (int): number of simulations to generate.

    Returns:
        cmb_map (np.ndarray): simulated cmb maps.
    """
    nside = 128
     
    
    npix=hp.nside2npix(nside)
    freqs = np.array([28.4,  44.1,  70.4,  100.0,  143.0,  217.0,  353.0])
    n_freqs=len(freqs)
    cmb_map=np.zeros((nsims, n_freqs, npix), dtype=float)
    
    for i in range(nsims):
        
        #Dictionary containing the configuration of the
        #components of the sky model
        
        sky_config = {
            "c1":{
                "class":"CMBLensed",
                "cmb_spectra" : "pysm_2/camb_lenspotentialCls.dat",
                "cmb_seed" : i,
                "apply_delens": False,
                "delensing_ells": "pysm_2/delens_ells.txt"
            }
        
            
        }
        for nf, freq in enumerate(freqs):
            
            # Initialize the PySM sky
            sky = pysm3.Sky(nside=nside, component_config=sky_config)
            # Convert emissions to uK_CMB
            conversion = u.K_RJ.to(u.K_CMB, equivalencies=u.cmb_equivalencies(freq * u.GHz))

            cmb_map[i,nf,:]=sky.get_emission(freq * u.GHz)[0] * conversion
            
    return(cmb_map)