using BioSequences, FASTX, GenomicAnnotations, BioAlignments
rc(s) = reverse_complement(s)

s = dna"GACAGGTTTCCCGACTGGA"
rc(s)


sg = readgbk("seqs/try2/mCherry_SG_reverse_translated.gbk")[1]
tw = readgbk("seqs/try2/mCherry_Twist_RevTrans.gb")[1]

