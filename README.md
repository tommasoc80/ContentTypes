## Content Types

This repository contains:
- the Content Type Dataset Version 1.5 (in the folder "Datasets");
- the latest version of the guidelines for annotating Content Types;
- the [data statement](https://www.mitpressjournals.org/doi/pdf/10.1162/tacl_a_00041) related to CTD V1.5 (see below);
- a set of spreadsheets containing metadata about the documents included in the dataset, e.g. year of publication, author's name, author's nationality, author's gender (in the folder "Documents_Metadata");
- the data to replicate a set of experiments for the identification of Content Types (in the folder "Datasets");
- the best model for the identification of Content Types obtained adopting the [BiLSTM-CNN-CRF with ELMo-Representations for Sequence Tagging implementation](https://github.com/UKPLab/elmo-bilstm-cnn-crf) by Nils Reimers and Iryna Gurevych (in the folder "Best_Model");
- the data used to calculate the Inter-Annotator Agreement (in the folder "IAA"): the script used for calculating Cohen's k is [online](https://github.com/johnnymoretti/CAT_R_Kappa_Cohen);

This work builds on ([Sprugnoli et al., 2017](https://www.aclweb.org/anthology/E17-2042.pdf)) where we first tested our annotation scheme and run preliminary experiments using linear models. Data related to this previous work is available on a separate [repository](https://github.com/dhfbk/content-types).



------------

### Data statement

#### CURATION RATIONALE: 
We adopt a broad perspective on texts selection assuming that good computational models for NLP must be able to deal with different genres (synchronic dimension) as well as with different times (diachronic dimension). This approach aims at facilitating the re-use of models in different fields of study, and promoting the cross-fertilisation among disciplines, especially in the area of Humanities. On the basis of this approach, we collected texts in English from three different genres: newspaper articles, travel reports, and travel guides. For each of these genres, we collected data published between the second half of the 1800s and the beginning of the 2000s. In designing the corpus, one of our goals was to keep the combination of time and genre as much balanced as possible, in terms of number of tokens and clauses. Furthermore, given the phenomenon under study, we decided to preserve documents' integrity rather than truncating them. 

#### LANGUAGE VARIETY:
en-GB, en-US, en-AU.

#### ANNOTATOR DEMOGRAPHIC
**Annotator #1:**
Age: 36 years old
Gender: female
Race/ethnicity: caucasian
Native language: Italian
Socioeconomic status
Training in linguistics/other relevant discipline: MA in Computational Linguistics

**Annotator #2:**
Age: 37 years old
Gender: male
Race/ethnicity: caucasian
Native language: Italian
Socioeconomic status
Training in linguistics/other relevant discipline: PhD in Computational Linguistics

**Annotator #3:**
Age: 25 years old
Gender: female
Race/ethnicity: caucasian
Native language: Italian
Socioeconomic status
Training in linguistics/other relevant discipline: MA in Linguistics

#### SPEAKER DEMOGRAPHIC & SPEECH SITUATION: 
Information included in the spreadsheets. 

#### TEXT CHARACTERISTICS: 
The combination of the time and genre dimensions gives rise to 6 sub-corpora within our dataset: Contemporary News, Historical News, Contemporary Travel Reports, Historical Travel Reports, Contemporary Travel Guides, Historical Travel Guides. 

------------

### Results
Results on the identification of CTs. Scores for bi-LSTM models are based on the average of P, R, and F1 per class over 5 multiple runs. Numbers in brackets indicate standard deviation. Bold numbers highlight the best results. 

| **Model** | P | R | F1 |
|----------------------|:------------:|:------------:|:------------:|  
| Baseline (majority) | 52.05 | 52.04 | 52.04 |  
| CRF | 11.15 | 31.70 | 16.49 |  
| bi-LSTM-CRF standard (w. Komninos and Manandhar (2016)) | 70.74 (0.15) | 70.32 (0.13) | 70.56 (0.14) |  
| bi-LSTM-CRF ELMo  | 71.92 (0.80) | 73.18 (0.78) | 72.55 (0.78) |
| bi-LSTM-CRF ELMo+ (w. Komninos and Manandhar (2016)) | 73.8 (0.56) | 73.32 (0.55) | 73.34 (0.59) |
|**bi-LSTM-CRF ELMo+ (w. word2vec)** | **73.86 (0.95)** | **73.80 (0.96)** | **73.82 (0.94)** |


Results across Genres. Scores are the average of P and R per class over 5 multiple runs. Numbers in brackets indicate standard deviation.

| Train/Test |      News     |      News     |     Guides    |     Guides    |    Reports    |    Reports    |
|------------|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
|            |       P       |       R       |       P       |       R       |       P       |       R       |
| **News**       | 73.37 (1.73) | 74.45 (1.26) | 38.70 (2.03) | 39.10 (2.93) | 57.68 (1.35) | 61.20 (0.68) |
| **Guides**     | 64.42 (1.90) | 64.38 (2.04) | 64.82 (0.89) | 65.84 (0.75) | 53.70 (2.46) | 55.32 (2.74) |
| **Reports**    | 75.37 (1.25) | 77.18 (1.08) | 50.18 (0.36) | 50.80 (0.50) | 68.12 (0.44) | 70.00 (0.60) |



Results across Time. Scores are the average of P and R per class over 5 multiple runs. Numbers in brackets indicate standard deviation.

|  Train/Test  |  Contemporary |  Contemporary |   Historical  |   Historical  |
|:------------:|:-------------:|:-------------:|:-------------:|:-------------:|
|              |       P       |       R       |       P       |       R       |
| **Contemporary** | 72.00 (0.86) | 72.98 (0.83) | 66.68 (0.97) | 68.42 (1.29) |
| **Historical**   | 66.56 (1.19) | 67.40 (1.30) | 71.65 (1.19) | 73.23 (0.67) |


