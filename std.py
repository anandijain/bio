from num2words import num2words
from Bio.Seq import Seq
from Bio import SeqIO

G_PER_MOL_BP = 650
AVO = 6.022e23

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

def ng_to_n(ng, bps):
    return ng_to_mol(ng, bps) * AVO 

def psci(x):
    return f"{x:.3e}"

def rc(x):
    if type(x) == str:
        return str(Seq(x).reverse_complement())
    elif type(x) == Seq:
        return x.reverse_complement()
    else:
        raise ValueError("rc() only accepts str or Seq")

# def numname(x):
    # return num2words(x)

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
    # lets say we start with 1ng
    # ul = ng / (ng/uL)
    5 / conc_puc19 # 0.05 uL
    # so we need to dilute the concentrated extracted puc19 plasmid to be able to pipette it
    # for pcr 

    # c1*v1 = c2*v2
    # so if we add like 1 uL of the concentrated puc19 to 99uL water we get ~1ng/uL (tho will check on nanodrop)
    puc_ng_for_hifi=pmol_to_ng(.05,2800)
    vector_insert_ratio = 2
    puc_ng_for_hifi*vector_insert_ratio
    # 1ng -> 500ng

    sg = SeqIO.read("seqs/try2/mCherry_SG_reverse_translated.gbk", "genbank")
    tw = SeqIO.read("seqs/try2/mCherry_Twist_RevTrans.gb", "genbank")
