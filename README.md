# scFv Structure Modelling
This repository lays out our process of predicting the structure for the anti-IL8 scFv format antibody. The amino acid sequence for the antibody has the following parts.

1. A signal peptide sequence to ensure that the antibody is secreted from the cell.

```
MPLLLLLPLLWAGALA
```

2. The variable heavy chain (VH) of the antibody.

```
EVQLLESGGGLVQPGGSLRLSCAASGFTFSYYGMGWVRQAPGKGLEWVSG
ISYSGSGTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCARDY
VGNLDYWGQGTLVTVSS
```

3. A linker sequence to connect the VH and VL chains.

```
GGGGSGGGGSGGGGS
```

4. The variable light chain (VL) of the antibody.

```
DIQMTQSPSSLSASVGDRVTITCRASQSISSYLNWYQQKPGKAPKLLIYA
ASSLQSGVPSRFSGSGSGTDFTLTISSLQPEDFATYYCQQSDTPSTFGQG
TKLEIK
```

5. A 3xFLAG and a 6xHis-tag sequence to facilitate purification of the antibody.

```
RTDYKDHDGDYKDHDIDYKDDDDKAAALPETGGHHHHHH
```


Therefore, the full amino acid sequence that we will work with is

```
MPLLLLLPLLWAGALAEVQLLESGGGLVQPGGSLRLSCAASGFTFSYYGM
GWVRQAPGKGLEWVSGISYSGSGTYYADSVKGRFTISRDNSKNTLYLQMN
SLRAEDTAVYYCARDYVGNLDYWGQGTLVTVSSGGGGSGGGGSGGGGSDI
QMTQSPSSLSASVGDRVTITCRASQSISSYLNWYQQKPGKAPKLLIYAAS
SLQSGVPSRFSGSGSGTDFTLTISSLQPEDFATYYCQQSDTPSTFGQGTK
LEIKRTDYKDHDGDYKDHDIDYKDDDDKAAALPETGGHHHHHH
```

Note that we keep the signal peptide and the tags attached during the modelling process, because we do not know whether or not (and how) they interact with Interleukin-8 during docking.

### Source
O-IL8-15 Biological Probe, in Structural Genomics Consortium: [thesgc.org/biological-probes/il-8](https://www.thesgc.org/biological-probes/il-8)

---
## AlphaFold2
AlphaFold2 is a deep learning system that predicts protein structures from amino acid sequences. We used the open-source distribution of AlphaFold2, [ColabFold](https://github.com/sokrypton/ColabFold) to predict the structure of the antibody. In particular, we used the [AlphaFold2_mmseqs2](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb) notebook. This notebook differs from full AlphaFold2 and AlphaFold2 Colab in that it uses MMseqs2 (Many-against-Many sequence searching) in place of homology detection and MSA pairing.

We used ColabFold with two different schemes: one without templates, and one with PDB70 as a database for templates. We also relaxed the top structure in either scheme wish AMBER.

### With PDB70

The structure generated with PDB70 is available [here](https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20with%20PDB70/scFvModellingwithAlphaFoldwithpdb70_ee5cb_relaxed_rank_001_alphafold2_ptm_model_4_seed_000.pdb). 

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20with%20PDB70/rank1.png"  width="150">

### Without Templates

The structure generated with PDB70 is available [here](https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20Without%20Template/scFvModellingwithAlphaFoldnotemplate_ee5cb_relaxed_rank_001_alphafold2_ptm_model_4_seed_000.pdb). 

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20Without%20Template/rank1.png"  width="150">

Data for analysis is present in the ` AlphaFold Without Template` and `AlphaFold with PDB70` directories, along with other generated models. 

Both of these have very similar average predicted aligned errors, as well as predicted lDDT scores. For both of these, folding is poor near the ends where the signal peptide and flags were attached, and in the middle where the linker is present.

| With PDB70 | Without Templates |
|------------|-------------------|
|<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20with%20PDB70/pae-rank1.png" width="150">|<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20Without%20Template/pae-rank1.png" width="150">|
|<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20with%20PDB70/scFvModellingwithAlphaFoldwithpdb70_ee5cb_coverage.png" width=150>|<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20Without%20Template/scFvModellingwithAlphaFoldnotemplate_ee5cb_coverage.png" width=150>|
|<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20with%20PDB70/scFvModellingwithAlphaFoldwithpdb70_ee5cb_plddt.png" width=150>|<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20Without%20Template/scFvModellingwithAlphaFoldnotemplate_ee5cb_plddt.png" width=150>|

### Citations

1. Mirdita, M., Schütze, K., Moriwaki, Y., Heo, L., Ovchinnikov, S., & Steinegger, M. (2022). ColabFold: Making Protein folding accessible to all. Nature Methods.
2. Mirdita, M., Steinegger, M., & S"oding, J. (2019). MMseqs2 desktop and local web server app for fast, interactive sequence searches. Bioinformatics, 35(16), 2856–2858.
3. Mirdita, M., Driesch, L., Galiez, C., Martin, M., S"oding, J., & Steinegger, M. (2017). Uniclust databases of clustered and deeply annotated protein sequences and alignments. Nucleic Acids Res., 45(D1), D170–D176.
4. Mitchell, A., Almeida, A., Beracochea, M., Boland, M., Burgin, J., Cochrane, G., Crusoe, M., Kale, V., Potter, S., Richardson, L., Sakharova, E., Scheremetjew, M., Korobeynikov, A., Shlemov, A., Kunyavskaya, O., Lapidus, A., & Finn, R. (2019). MGnify: the microbiome analysis resource in 2020. Nucleic Acids Res..
5. Steinegger, M., Meier, M., Mirdita, M., V"ohringer, H., Haunsberger, S., & S"oding, J. (2019). HH-suite3 for fast remote homology detection and deep protein annotation. BMC Bioinform., 20(1), 473.
6. Berman, H., Henrick, K., & Nakamura, H.. (2003). Announcing the worldwide Protein Data Bank.
7. Eastman, P., Swails, J., Chodera, J., McGibbon, R., Zhao, Y., Beauchamp, K., Wang, L.P., Simmonett, A., Harrigan, M., Stern, C., Wiewiora, R., Brooks, B., & Pande, V. (2017). OpenMM 7: Rapid development of high performance algorithms for molecular dynamics. PLOS Comput. Biol., 13(7).



---
## SWISS-MODEL
<!-- SWISS-MODEL is a fully automated protein structure homology-modelling tool. The list of suggested templates can be found [here](https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/templates.txt). The top 2 templates, in order of expected quality (GMQE score), are

1. AlphaFold DB model of Q65ZC9_HUMAN
2. Crystal Structure of spFv GLK1 HL

We will use both of these templates to generate structures for the antibody, since they are obtained from drastically different methods: the former from deep learning, and the latter from X-ray crystallography.

The structure generated from the AlphaFold DB model of Q65ZC9_HUMAN is available [here](https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/models/01/model.pdb). 

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/models/01/01.png"  width="150" height="150">

The structure generated from the Crystal Structure of spFv GLK1 HL is available [here](https://github.com/iGEMIISc/scFv-Modelling/blob/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/models/02/model.pdb).

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/(WITH%20SIGNAL%20PEPTIDE)%20swissmodel/scFv_Structure_Prediction/models/02/02.png"  width="150" height="150"> -->

---
## I-TASSER

---
## Modeller 
Modeller is a software package for protein structure modelling. We will use Modeller to generate structures for the antibody using templates obtained from querying <!--BLAST and -->PDB. 

<!-- In terms of the _Max Score_ parameter, the best template from Smart BLAST among natural proteins is [immunoglobulin heavy variable 4-38-2-like](https://www.ncbi.nlm.nih.gov/protein/XP_011544500.1?report=genbank&log$=protalign&blast_rank=1&RID=5BXFUSF5011). The best template among synthetic constructs is [single-chain variable fragment antibody, partial](https://www.ncbi.nlm.nih.gov/protein/QNB92943.1?report=genbank&log$=protalign&blast_rank=4&RID=5BXFUSF5011). Note that the synthetic construct has a much higher expected quality than the natural protein.

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

--- -->
