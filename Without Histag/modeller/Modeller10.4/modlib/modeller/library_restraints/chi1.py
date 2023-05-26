#   residue    weights                  means        stdevs
chi1 = [
    ( 'CYS', (0.265, 0.565, 0.171), (3.17022, -1.14843, 1.12277), (0.14626, 0.15516, 0.16266) ),
    ( 'ASP', (0.320, 0.508, 0.172), (3.24893, -1.19974, 1.08123), (0.16336, 0.14539, 0.13771) ),
    ( 'GLU', (0.330, 0.580, 0.089), (3.18505, -1.15401, 1.12574), (0.16179, 0.14975, 0.17715) ),
    ( 'PHE', (0.339, 0.545, 0.116), (3.15049, -1.14965, 1.10183), (0.16389, 0.18029, 0.16598) ),
    ( 'HIS', (0.328, 0.544, 0.128), (3.20460, -1.13516, 1.10078), (0.18431, 0.17680, 0.17680) ),
    ( 'ILE', (0.093, 0.776, 0.132), (3.30373, -1.10671, 1.06797), (0.15202, 0.12776, 0.11153) ),
    ( 'LYS', (0.337, 0.588, 0.074), (3.17720, -1.14860, 1.13062), (0.14067, 0.15184, 0.14818) ),
    ( 'LEU', (0.312, 0.675, 0.014), (3.13095, -1.13429, 1.12329), (0.13648, 0.15219, 0.20979) ),
    ( 'MET', (0.293, 0.629, 0.078), (3.17912, -1.15785, 1.12905), (0.15499, 0.13683, 0.15760) ),
    ( 'ASN', (0.296, 0.562, 0.142), (3.26830, -1.18700, 1.09676), (0.17383, 0.16720, 0.14434) ),
    ( 'PRO', (0.512, 0.488), (-0.49428, 0.52569), (0.10263, 0.11310) ),
    ( 'GLN', (0.313, 0.612, 0.075), (3.19483, -1.14773, 1.12190), (0.15603, 0.14539, 0.15760) ),
    ( 'ARG', (0.339, 0.569, 0.092), (3.18191, -1.15855, 1.13185), (0.16232, 0.15429, 0.16738) ),
    ( 'SER', (0.235, 0.287, 0.478), (3.11384, -1.11544, 1.13586), (0.15533, 0.13125, 0.15080) ),
    ( 'THR', (0.080, 0.433, 0.487), (-3.03460, -1.06448, 1.06133), (0.13910, 0.10699, 0.13544) ),
    ( 'VAL', (0.741, 0.185, 0.074), (3.06881, -1.07617, 1.11963), (0.11624, 0.10472, 0.14102) ),
    ( 'TRP', (0.340, 0.502, 0.159), (3.16585, -1.18403, 1.07024), (0.17000, 0.17698, 0.17314) ),
    ( 'TYR', (0.344, 0.538, 0.118), (3.13967, -1.13429, 1.10881), (0.17191, 0.17785, 0.17645) ),
  ]

def make_restraints(atmsel, restraints, num_selected):
    from modeller import forms, physical, features
    for (res, weights, means, stdevs) in chi1:
        for a in atmsel.find_chi1_dihedrals(res, num_selected):
            r = forms.MultiGaussian(physical.chi1_dihedral,
                                    features.Dihedral(*a), weights, means,
                                    stdevs)
            restraints.add(r)