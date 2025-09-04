# pick_forward_left_region_and_right_safeharbor.py
# pip install primer3-py biopython

from Bio import SeqIO
import primer3

# Windows (0-based, inclusive endpoints from your map)
FWD_START, FWD_END = 450, 504          # forward primer window (before CAP)
RIGHT_START, RIGHT_END = 939, 1178     # reverse primer window (safe harbor)

# Convert to (start, length)
fwd_start = FWD_START
fwd_len   = FWD_END - FWD_START + 1
rev_start = RIGHT_START
rev_len   = RIGHT_END - RIGHT_START + 1

rec = SeqIO.read("seqs/puc19.gb", "genbank")
seq = str(rec.seq).upper()

res = primer3.bindings.design_primers(
    # --- SEQUENCE args ---
    {
        "SEQUENCE_ID": "pUC19",
        "SEQUENCE_TEMPLATE": seq,
        # Constrain LEFT (forward) to 450..504 and RIGHT (reverse) to 939..1178
        # NOTE: list of lists, each item = [left_start, left_len, right_start, right_len]
        "SEQUENCE_PRIMER_PAIR_OK_REGION_LIST": [[fwd_start, fwd_len, rev_start, rev_len]],
    },
    # --- GLOBAL/primer args ---
    {
        "PRIMER_MIN_SIZE": 18,
        "PRIMER_OPT_SIZE": 21,
        "PRIMER_MAX_SIZE": 27,
        "PRIMER_MIN_TM": 58.0,
        "PRIMER_OPT_TM": 62.0,
        "PRIMER_MAX_TM": 66.0,

        # SantaLucia conditions (optional but recommended)
        "PRIMER_SALT_MONOVALENT": 50.0,   # mM
        "PRIMER_SALT_DIVALENT": 1.5,      # mM
        "PRIMER_DNTP_CONC": 0.2,          # mM
        "PRIMER_DNA_CONC": 250.0,         # nM

        # Product-size limits live HERE (not in OK_REGION_LIST)
        "PRIMER_PRODUCT_SIZE_RANGE": [[100, 3000]],
    }
)

print("PAIRS RETURNED:", res["PRIMER_PAIR_NUM_RETURNED"])
if res["PRIMER_PAIR_NUM_RETURNED"] == 0:
    print(res.get("PRIMER_ERROR", "No primers found; widen windows or relax Tm/size."))
else:
    for i in range(res["PRIMER_PAIR_NUM_RETURNED"]):
        F_seq = res[f"PRIMER_LEFT_{i}_SEQUENCE"]
        R_seq = res[f"PRIMER_RIGHT_{i}_SEQUENCE"]
        F_pos, F_len = res[f"PRIMER_LEFT_{i}"]
        R_pos, R_len = res[f"PRIMER_RIGHT_{i}"]
        print(f"\nPair {i}:")
        print("  Forward (LEFT) window 450..504")
        print("    seq :", F_seq)
        print("    pos :", F_pos, "len:", F_len)
        print("    Tm  :", res[f"PRIMER_LEFT_{i}_TM"])
        print("    GC% :", res[f"PRIMER_LEFT_{i}_GC_PERCENT"])

        print("  Reverse (RIGHT) window 939..1178")
        print("    seq :", R_seq)
        print("    pos :", R_pos, "len:", R_len)
        print("    Tm  :", res[f"PRIMER_RIGHT_{i}_TM"])
        print("    GC% :", res[f"PRIMER_RIGHT_{i}_GC_PERCENT"])

        print("  Predicted product size:", res[f"PRIMER_PAIR_{i}_PRODUCT_SIZE"])
