# bio stuff

random notes:
* [neb stable](https://www.neb.com/en-us/products/c3040-neb-stable-competent-e-coli-high-efficiency)
    - neb stable genotype  F' proA+B+ lacIq ∆(lacZ)M15 zzf::Tn10 (TetR)/∆(ara-leu) 7697 araD139 fhuA ∆lacX74 galK16 galE15 e14-  Φ80dlacZ∆M15 recA1 relA1 endA1 nupG rpsL (StrR) rph spoT1 ∆(mrr-hsdRMS-mcrBC) 
    - note the lacIq means that it overexpresses lacI so we dont need to include it in the pUC19 

hifi assembly plan:

we start with ecoli expressing puc19 in glycerol stock and we order the gene fragment of mcherry from twist without adapters but with the promoter (plac), operator, RBS, and the overhangs all apart of the fragment

we then order two sets of primers, the inverse primers used to amplify and linearize the puc19 (but with the primers designed to excise the lacza)
the other set of primers will be designed to amplify the gene fragment, as we will set aside some of the DNA so that if the first attempt doesnt work we can always amplify it



primers planning to use to excise the Lacza and insert the mCherry:
these primers need to be RC'd to be inverse primers 
```
Pair 0:
  Forward (LEFT) window 450..504
    seq : GACAGGTTTCCCGACTGGA
    pos : 460 len: 19
    Tm  : 62.03301112748716
    GC% : 57.89473684210526
  Reverse (RIGHT) window 939..1178
    seq : GGTGATGACGGTGAAAACCTC
    pos : 1071 len: 21
    Tm  : 62.00623169136122
    GC% : 52.38095238095238
  Predicted product size: 612
```


cassette design:

why are these totally different 
[ptac from snapgene](https://www.snapgene.com/plasmids/basic_cloning_vectors/tac_promoter)
[ptac from igem](https://registry.igem.org/parts/bba-k5515009)


