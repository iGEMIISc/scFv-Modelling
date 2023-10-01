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

We used ColabFold with two different schemes: one without templates, and one with PDB70 as a database for templates. We also relaxed the top structure in either scheme with AMBER.

### With PDB70

The structure generated with PDB70 is available [here](https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20with%20PDB70/scFvModellingwithAlphaFoldwithpdb70_ee5cb_relaxed_rank_001_alphafold2_ptm_model_4_seed_000.pdb). 

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20with%20PDB70/rank1.png"  width="150">

### Without Templates

The structure generated without templates is available [here](https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20Without%20Template/scFvModellingwithAlphaFoldnotemplate_ee5cb_relaxed_rank_001_alphafold2_ptm_model_4_seed_000.pdb). 

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/AlphaFold%20Without%20Template/rank1.png"  width="150">

Data for analysis is present in the `AlphaFold Without Template` and `AlphaFold with PDB70` directories, along with other generated models. 

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
SWISS-MODEL is a fully automated protein structure homology-modelling tool. SWISS-MODEL searches for templates against the SWISS-MODEL template library (STML). The list of suggested templates can be found [here](https://github.com/iGEMIISc/scFv-Modelling/blob/main/SWISS%20MODEL/templates.txt). The top 2 templates, in order of expected quality (GMQE score), are

1. AlphaFold DB model of Q65ZC9_HUMAN (Q65ZC9.1.A)
2. Crystal Structure of spFv GLK1 HL (8dy0.1.A)

We used both of these templates to generate structures for the antibody, since they are obtained from drastically different paradigms–the former from deep learning, and the latter from X-ray crystallography. Both have nearly the same sequence identity with the antibody, as well as GMQE scores.

### Q65ZC9.1.A
The structure generated from the AlphaFold DB model of Q65ZC9_HUMAN is available [here](https://github.com/iGEMIISc/scFv-Modelling/blob/main/SWISS%20MODEL/models/01/model.pdb). 

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/SWISS%20MODEL/models/01/01.png"  width="150">

### 8dy0.1.A
The structure generated from the Crystal Structure of spFv GLK1 HL is available [here](https://github.com/iGEMIISc/scFv-Modelling/blob/main/SWISS%20MODEL/models/02/model.pdb)

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/SWISS%20MODEL/models/02/02.png"  width="150">

More details about the models can be found in the `SWISS MODEL` directory.

### Citations

1. Waterhouse, A., Bertoni, M., Bienert, S., Studer, G., Tauriello, G., Gumienny, R., Heer, F.T., de Beer, T.A.P., Rempfer, C., Bordoli, L., Lepore, R., Schwede, T. SWISS-MODEL: homology modelling of protein structures and complexes. Nucleic Acids Res. 46(W1), W296-W303 (2018).
2. Bienert, S., Waterhouse, A., de Beer, T.A.P., Tauriello, G., Studer, G., Bordoli, L., Schwede, T. The SWISS-MODEL Repository - new features and functionality. Nucleic Acids Res. 45, D313-D319 (2017).
3. Studer, G., Tauriello, G., Bienert, S., Biasini, M., Johner, N., Schwede, T. ProMod3 - A versatile homology modelling toolbox. PLOS Comp. Biol. 17(1), e1008667 (2021).  
4. Studer, G., Rempfer, C., Waterhouse, A.M., Gumienny, G., Haas, J., Schwede, T. QMEANDisCo - distance constraints applied on model quality estimation. Bioinformatics 36, 1765-1771 (2020).
5. Bertoni, M., Kiefer, F., Biasini, M., Bordoli, L., Schwede, T. Modeling protein quaternary structure of homo- and hetero-oligomers beyond binary interactions by homology. Scientific Reports 7 (2017).

---
## I-TASSER
I-TASSER (Iterative Threading ASSEmbly Refinement) is a protein structure prediction server, that identifies structural templates from the PDB by multiple threading approach (LOMETS), and constructs structures by iterative template-based fragment assembly simulations. I-TASSER used Crystal structure of SARS spike protein receptor, [2ghw](https://www.rcsb.org/structure/2ghw) as the template in its more reliable structure.

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/I-TASSER/model1.png"  width="150">

Other templates used by I-TASSER were also proteins whose structures are known through experimental techniques like X-ray diffraction or electron microscopy. More details about these models can be found in the `I-TASSER` directory.


### Citations
1. Wei Zheng, Chengxin Zhang, Yang Li, Robin Pearce, Eric W. Bell, Yang Zhang. Folding non-homology proteins by coupling deep-learning contact maps with I-TASSER assembly simulations. Cell Reports Methods, 1: 100014 (2021).
2. Chengxin Zhang, Peter L. Freddolino, and Yang Zhang. COFACTOR: improved protein function prediction by combining structure, sequence and protein-protein interaction information. Nucleic Acids Research, 45: W291-299 (2017).
3. Jianyi Yang, Yang Zhang. I-TASSER server: new development for protein structure and function predictions, Nucleic Acids Research, 43: W174-W181, 2015.

---
## Modeller 
Modeller is a software package for protein structure modelling. We will use Modeller to generate structures for the antibody using templates obtained from querying PDB. We identified [6Y6C: Entity 2](https://www.rcsb.org/structure/6Y6C#entity-2) from the PDB as the top template for our antibody. This protein is an extracellular domain with an scFv-fragment. This template had a sequence identity of 93% with our antibody, and an E-value of 1.087e-135.

Chain-C of `6Y6C` aligned the best with our target sequence, which we determined using Modeller. We then used Modeller to produce the a structure for our anti-body using this chain. We ran the structure through energy-optimization as well, but it seemed that the structure was already optimized since there was no change in its DOPE score.

The structure generated by Modeller is available [here](https://github.com/iGEMIISc/scFv-Modelling/blob/main/Modeller/il8.B99990001.pdb).

<img src="https://raw.githubusercontent.com/iGEMIISc/scFv-Modelling/main/Modeller/model1.png"  width="150">

More details about the modelling process can be found in the `Modeller` directory.

### Citations

1. B. Webb, A. Sali. Comparative Protein Structure Modeling Using Modeller. Current Protocols in Bioinformatics 54, John Wiley & Sons, Inc., 5.6.1-5.6.37, 2016.
2. M.A. Marti-Renom, A. Stuart, A. Fiser, R. Sánchez, F. Melo, A. Sali. Comparative protein structure modeling of genes and genomes. Annu. Rev. Biophys. Biomol. Struct. 29, 291-325, 2000.
3. A. Sali & T.L. Blundell. Comparative protein modelling by satisfaction of spatial restraints. J. Mol. Biol. 234, 779-815, 1993.
4. A. Fiser, R.K. Do, & A. Sali. Modeling of loops in protein structures, Protein Science 9. 1753-1773, 2000.

---

## Comparative Analysis with ProDy

We select the 6 models discussed above for comparative analysis, to determine the most accurate and reliable model. All data in this section has been generated using ProDy. It is a software package for protein dynamics, sequence and structural analysis. The analysis here, is based on the number of resolved atoms. Higher is the accuracy of the model, if the number of resolved atom is more. The number of resolved atoms for each model is given below.

| Model | Number of Resolved Atoms |
|-------|--------------------------|
| AlphaFold2 with PDB70 |  4281 |
| AlphaFold2 without Templates |  4281 |
| SWISS-MODEL Q65ZC9.1.A |  1769 |
| SWISS-MODEL 8dy0.1.A |  1733 |
| I-TASSER |  4277 |
| Modeller |  2201 |

This immediately places the I-TASSER model in a much more reliable position than models generated by SWISS-MODEL and Modeller. In fact, it gets quite close to the coverage of AlphaFold2 models which were AI-generated. 

### Root Mean Square Deviation (RMSD)

We now see the RMSD of the AlphaFold2 and I-TASSER models with respect to each other. RMSD determines the similarity between the two models. It provides the average deviation of corresponding atoms in the two models. This is done after superimposing the models on the same reference structure, through the Kabsch algorithm. Kabsch algorithm is a method of calculating the optimal translation and rotation which produces least value of RMSD. Lesser the value of RMSD, more similar are the two models.

| | AlphaFold2 with PDB70 | AlphaFold2 without Templates | I-TASSER |
|---|---|---|---|
| AlphaFold2 with PDB70 | 0 | 1.53 | 12.17 |
| AlphaFold2 without Templates | 1.53 |0 | 12.57 |
| I-TASSER | 12.17 | 12.57 | 0 |

The AlphaFold2 model generated with PDB70 therefore appears to be the most reliable, since it is the closest to other structures. 

### Citations
1. Zhang S, Krieger JM, Zhang Y, Kaya C, Kaynak B, Mikulska-Ruminska K, Doruker P, Li H, Bahar I ProDy 2.0: Increased scale and scope after 10 years of protein dynamics modelling with Python 2021 Bioinformatics, btab187.
2. Bakan A, Meireles LM, Bahar I ProDy: Protein Dynamics Inferred from Theory and Experiments 2011 Bioinformatics 27(11):1575-1577
3. Bakan A, Dutta A, Mao W, Liu Y, Chennubhotla C, Lezon TR, Bahar I Evol and ProDy for Bridging Protein Sequence Evolution and Structural Dynamics 2014 Bioinformatics 30(18):2681-2683
