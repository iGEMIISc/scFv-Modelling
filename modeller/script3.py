from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='6y6c', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='6y6c', atom_files='6y6c.pdb')
aln.append(file='query.ali', align_codes='TvLDH')
aln.align2d()
aln.write(file='query-6y6c.ali', alignment_format='PIR')
aln.write(file='query-6y6c.pap', alignment_format='PAP')
