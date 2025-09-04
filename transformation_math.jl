# pGLO is 5371 bp 
# i have 98ng/ul from miniprep
# total i believe there is about 75 ul (at least thats how much elution buffer)
n_bp = 5371
per_bp = 653.9 #g/mol/bp
ng = 98

pglo_mm = per_bp * n_bp

g = ng*1e-9

avo= 6.022e23
n_pglo = g/pglo_mm*avo
# 1.68 billion plasmid molecules 

ml_culture = 5.5 
ecoli_conv_const = 8e8
od600 = .4 # start of mid-log (ideal for transformations)
# cells_per_ml = OD * C * dilution factor
cells_per_ml = od600 * ecoli_conv_const * 1

cells = cells_per_ml * ml_culture

# we resuspend `cells` into 50 uL of transformation soln
# and we use 1uL of pGLO soln 