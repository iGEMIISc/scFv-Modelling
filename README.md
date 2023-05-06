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

<img src="https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20scFvStructurePrediction_44a20_0%20alphafold%20(colabfold)%20latest%20version/SCFVSTRUCTUREPREDICTION_4F267_UNRELAXED_RANK_001_ALPHAFOLD2_PTM_MODEL_3_SEED_000.PDB.png"  width="150" height="150">

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

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/models/01/01.png"  width="150" height="150">

The structure generated from the Crystal Structure of spFv GLK1 HL is available [here](https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/models/02/model.pdb).

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/models/02/02.png"  width="150" height="150">

---
## Modeller 
Modeller is a software package for protein structure modelling. We will use Modeller to generate structures for the antibody using templates obtained from querying BLAST and PDB. 

In terms of the _Max Score_ parameter, the best template from Smart BLAST among natural proteins is [immunoglobulin heavy variable 4-38-2-like](https://www.ncbi.nlm.nih.gov/protein/XP_011544500.1?report=genbank&log$=protalign&blast_rank=1&RID=5BXFUSF5011). The best template among synthetic constructs is [single-chain variable fragment antibody, partial](https://www.ncbi.nlm.nih.gov/protein/QNB92943.1?report=genbank&log$=protalign&blast_rank=4&RID=5BXFUSF5011). Note that the synthetic construct has a much higher expected quality than the natural protein.

The top four templates from PDB, in decreasing order of _score_, are

1. [6Y6C: Entity 2](https://www.rcsb.org/structure/6Y6C#entity-2)
2. [6YMQ: Entity 1](https://www.rcsb.org/structure/6YMQ#entity-1)
3. [6G8R: Entity 1](https://www.rcsb.org/structure/6G8R#entity-1)
4. [6YYE: Entity 2](https://www.rcsb.org/structure/6YYE#entity-2)

Templates from PDB showed a much higher expected quality. 

On checking alignment of `6Y6C` with our target sequence, it turned out that the best template for our antibody is chain-C of `6Y6C`. We then used modeller to produce the following structures for the antibody, in decreasing order of confidence.

1. [Rank 1](https://github.com/iGEMIISc/scFv-Modelling/blob/main/modeller/TvLDH.B99990001.pdb) (This model was further also run through an energy optimizer) 

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/modeller/TVLDH.B99990001.PDB.png"  width="150" height="150">

2. [Rank 2](https://github.com/iGEMIISc/scFv-Modelling/blob/main/modeller/TvLDH.B99990002.pdb)
3. [Rank 3](https://github.com/iGEMIISc/scFv-Modelling/blob/main/modeller/TvLDH.B99990003.pdb)
4. [Rank 4](https://github.com/iGEMIISc/scFv-Modelling/blob/main/modeller/TvLDH.B99990004.pdb)
5. [Rank 5](https://github.com/iGEMIISc/scFv-Modelling/blob/main/modeller/TvLDH.B99990005.pdb)