'''
this is an example reading the puc19 genbank file and finding a primer pair 
in the region between the end of LacZa and the start of the AmpR promoter


'''

from Bio import SeqIO
import primer3

# safe-harbor window from your pUC19 paste:
SAFE_HARBOR_START = 939
SAFE_HARBOR_END   = 1178

# 1) read the plasmid
rec = SeqIO.read("seqs/puc19.gb", "genbank")
seq = str(rec.seq).upper()

# 2) constrain Primer3 to search only within the safe-harbor window
start = SAFE_HARBOR_START
length = SAFE_HARBOR_END - SAFE_HARBOR_START + 1

res = primer3.bindings.design_primers(
    {
        "SEQUENCE_ID": "pUC19",
        "SEQUENCE_TEMPLATE": seq,
        "SEQUENCE_INCLUDED_REGION": (start, length),
    },
    {
        # minimal, sane defaults
        "PRIMER_MIN_SIZE": 18,
        "PRIMER_OPT_SIZE": 21,
        "PRIMER_MAX_SIZE": 27,
        "PRIMER_MIN_TM": 58.0,
        "PRIMER_OPT_TM": 62.0,
        "PRIMER_MAX_TM": 66.0,
    }
)

# 3) print whatever it found
print("PAIRS RETURNED:", res["PRIMER_PAIR_NUM_RETURNED"])
if res["PRIMER_PAIR_NUM_RETURNED"] > 0:
    F_seq = res["PRIMER_LEFT_0_SEQUENCE"]
    R_seq = res["PRIMER_RIGHT_0_SEQUENCE"]

    # positions are 0-based start and length
    F_pos, F_len = res["PRIMER_LEFT_0"]
    R_pos, R_len = res["PRIMER_RIGHT_0"]

    print("\nForward primer:")
    print("  seq :", F_seq)
    print("  pos :", F_pos, "len:", F_len, "Tm", res["PRIMER_LEFT_0_TM"], "GC%", res["PRIMER_LEFT_0_GC_PERCENT"])

    print("\nReverse primer:")
    print("  seq :", R_seq)
    print("  pos :", R_pos, "len:", R_len, "Tm", res["PRIMER_RIGHT_0_TM"], "GC%", res["PRIMER_RIGHT_0_GC_PERCENT"])

    # optional: report product size Primer3 predicts
    print("\nPredicted product size:", res["PRIMER_PAIR_0_PRODUCT_SIZE"])
else:
    print(res.get("PRIMER_ERROR", "No primers found. Try widening the window or relaxing Tm/size."))
