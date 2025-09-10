
G_PER_MOL_BP = 650

def bps_to_mw(bps):
    """assumes ~50% GC content"""
    return bps * G_PER_MOL_BP # [g/mol]

def ng_to_mol(ngs, bps):
    mw = bps_to_mw(bps)
    return (ngs * 1e-9) / mw # [mol]

def mol_to_ng(mols, bps):
    mw = bps_to_mw(bps)
    return (mols * mw) * 1e9 # [ng]

def ng_to_pmol(ng, bps):
    return ng_to_mol(ng, bps) * 1e12

def pmol_to_ng(pmol, bps):
    # pmol * (g/mol) * (1e-12 mol/pmol) * (1e9 ng/g) = pmol * MW * 1e-3
    return pmol * bps_to_mw(bps) * 1e-3


if __name__ == "__main__":
    # for hifi, we want .03-.2 pmol of the fragments and a ratio of (vector:insert) 1:2
    # we pick .1pmol of vector and .2pmol of insert 
    len_puc19 = 2800 # aprox bps
    ng_puc19 = pmol_to_ng(0.1, len_puc19) # 182 ng 

    # in the past i have gotten ~ 75uL of 100ng/uL concentration plasmid (pGLO) from miniprep
    # we extrapolate to assume same yield for puc19
    conc_puc19 = 100 # ng/uL
    vol_puc19 = ng_puc19 / conc_puc19 # uL

    # the above is wrong becasue we need to linearize first and PCR will make it different concentration 
    # for Q5 neb recommends 1pg-10ng of template
    # lets say we start with 5ng
    # ul = ng / (ng/uL)
    5 / conc_puc19 # 0.05 uL
    # so we need to dilute the concentrated extracted puc19 plasmid to be able to pipette it
    # for pcr 

    # c1*v1 = c2*v2
    