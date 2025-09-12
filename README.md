# bio stuff

the plan (try 2):

## plasmid linearization and preparation
1) liquid culture of ecoli expressing puc19 
2) miniprep to purify the puc19
3) quantify concentration on nanodrop
4) dilute some for PCR, maybe store the rest in TE stock in -20
5) PCR 
6) run some of the pcr product on an agarose gel and expect a ~2kbp band
  - if no band, need to start over, maybe adjust pcr program or the primers
7) DpnI digestion to remove plasmid dna 
8) monarch pcr cleanup kit 
9) optionally rerun the cleaned product on another gel. 
  - again expect the ~2kbp 
10) quantify concentration of amplified linear fragments on nanodrop
11) use concentration as a seed for planning the assembly volumes  

## fragment preparation 


todo:
- understand the overlapped primers designed in snapgene 
- finish writing up the whole protocol in typstx
- order the polymerase, loading dye?, gene fragment, 

done:
- walk thru arrow chasing of overhanging pcr 
- finish designing the insert (promoter, operator, terminator) overhangs (insert: `seqs/ptac_mcherry_overhangs.dna`)

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




## primers and overhangs
lets say we have the following setup for letter strings A,B,G,X 

we have a plasmid and we are looking at a junction (where * represents rc):

5' A  |  B 3' ... X (wraps around to A) 
3' A*| B* 5' ... X* 

and we want to linearize it and then insert the letter sequence G into the 5->3 upper strand 

i believe my inverse primers should be A* and B so that my linear strands Lins become 

5' B X A 3'
3' B* X* A* 5' 

which i believe is the same as 

5' A* X* B* 3'
3' A   X   B   5' 

then my gene Ge should have 

5' A G B 3'
3' A* G* B* 5' 

right as the A and the B* in the Ge should get chewed back by exonuclease
and the A* and B in the Lins gets chewed back so that the exposed A in Lins binds with the exposed A* in Ge, and same for the exposed B in Ge and the exposed B* in Lin 