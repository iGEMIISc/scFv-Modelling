# scFv Structure Modelling
This repository lays out our process of predicting the structure for the anti-IL8 scFv format antibody. The amino acid sequence for the antibody is

```
AEVQLLESGGGLVQPGGSLRLSCAASGFTFSYYGMGWVRQAPGKGLEWVS
GISYSGSGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCARD
YVGNLDYWGQGTLVTVSSGGGGSGGGGSGGGGSDIQMTQSPSSLSASVGD
RVTITCRASQSISSYLNWYQQKPGKAPKLLIYAASSLQSGVPSRFSGSGS
GTDFTLTISSLQPEDFATYYCQQSDTPSTFGQGTKLEIKRTDYKDHDGDYK
```

We attach a signal peptide to our sequence to ensure that the antibody is secreted from the cell. The signal peptide sequence is

```
MPLLLLLPLLWAGAL
```

Therefore, the full amino acid sequence that we will work with is

```
MPLLLLLPLLWAGALAEVQLLESGGGLVQPGGSLRLSCAASGFTFSYYGM
GWVRQAPGKGLEWVSGISYSGSGTYYADSVKGRFTISRDNSKNTLYLQMN
SLRAEDTAVYYCARDYVGNLDYWGQGTLVTVSSGGGGSGGGGSGGGGSDI
QMTQSPSSLSASVGDRVTITCRASQSISSYLNWYQQKPGKAPKLLIYAAS
SLQSGVPSRFSGSGSGTDFTLTISSLQPEDFATYYCQQSDTPSTFGQGTK
LEIKRTDYKDHDGDYK
```

Note that we keep the signal peptide attached during the modelling process, because we do not know whether or not (and how) the signal peptide interacts with Interleukin-8 during docking.

---
## AlphaFold2
AlphaFold2 is a deep learning system that predicts protein structures from amino acid sequences. We used the open-source distribution of AlphaFold2, [ColabFold](https://github.com/sokrypton/ColabFold) to predict the structure of the antibody. In particular, we used the [AlphaFold2_mmseqs2](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb) notebook.

AlphaFold generated 5 structures for the antibody, which in decreasing order of confidence are 

1. [Rank 1](https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20scFvStructurePrediction_44a20_0%20alphafold%20(colabfold)%20latest%20version/scFvStructurePrediction_4f267_unrelaxed_rank_001_alphafold2_ptm_model_3_seed_000.pdb)
2. [Rank 2](https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20scFvStructurePrediction_44a20_0%20alphafold%20(colabfold)%20latest%20version/scFvStructurePrediction_4f267_unrelaxed_rank_002_alphafold2_ptm_model_4_seed_000.pdb)
3. [Rank 3](https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20scFvStructurePrediction_44a20_0%20alphafold%20(colabfold)%20latest%20version/scFvStructurePrediction_4f267_unrelaxed_rank_003_alphafold2_ptm_model_5_seed_000.pdb)
4. [Rank 4](https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20scFvStructurePrediction_44a20_0%20alphafold%20(colabfold)%20latest%20version/scFvStructurePrediction_4f267_unrelaxed_rank_004_alphafold2_ptm_model_1_seed_000.pdb)
5. [Rank 5](https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20scFvStructurePrediction_44a20_0%20alphafold%20(colabfold)%20latest%20version/scFvStructurePrediction_4f267_unrelaxed_rank_005_alphafold2_ptm_model_2_seed_000.pdb)

The structure coverage plot for these models shows relatively high error near the ends, and in the middle. 

![](https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/(WITH%20SIGNAL%20PEPTIDE)%20scFvStructurePrediction_44a20_0%20alphafold%20(colabfold)%20latest%20version/scFvStructurePrediction_4f267_coverage.png)

This can be seen through the PAE (Predicted Aligned Error) plots, and the pLDDT plot as well.

![](https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/(WITH%20SIGNAL%20PEPTIDE)%20scFvStructurePrediction_44a20_0%20alphafold%20(colabfold)%20latest%20version/scFvStructurePrediction_4f267_pae.png)

![](https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/(WITH%20SIGNAL%20PEPTIDE)%20scFvStructurePrediction_44a20_0%20alphafold%20(colabfold)%20latest%20version/scFvStructurePrediction_4f267_plddt.png)

---
## SWISS-MODEL
SWISS-MODEL is a fully automated protein structure homology-modelling tool. The list of suggested templates can be found [here](https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/templates.txt). The top 2 templates, in order of expected quality (GMQE score), are

1. AlphaFold DB model of Q65ZC9_HUMAN
2. Crystal Structure of spFv GLK1 HL

We will use both of these templates to generate structures for the antibody, since they are obtained from drastically different methods: the former from deep learning, and the latter from X-ray crystallography.

The structure generated from the AlphaFold DB model of Q65ZC9_HUMAN is available [here](https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/models/01/model.pdb). 

![](https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/models/01/01.png)

The structure generated from the Crystal Structure of spFv GLK1 HL is available [here](https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/models/02/model.pdb).

![](https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/models/02/02.png)