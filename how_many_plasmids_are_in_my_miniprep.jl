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