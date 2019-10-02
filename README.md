## Content Types

This repository contains:
- the Content Type Dataset Version 1.5 (in the folder "Datasets");
- the [data statement](https://www.mitpressjournals.org/doi/pdf/10.1162/tacl_a_00041) related to CTD V1.5 (see below);
- a set of spreadsheets containing metadata about the documents included in the dataset, e.g. year of publication, author's name, author's nationality, author's gender (in the folder "Documents_Metadata");
- the data to replicate a set of experiments for the identification of Content Types (in the folder "Datasets");
- the best model for the identification of Content Types obtained adopting the [BiLSTM-CNN-CRF with ELMo-Representations for Sequence Tagging implementation](https://github.com/UKPLab/elmo-bilstm-cnn-crf) by Nils Reimers and Iryna Gurevych (in the folder "Best_Model").

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
|----------------------|:------------:|:------------:|:------------:|:  
| Baseline (majority) | 52.05 | 52.04 | 52.04 |  
| CRF | 51.64 | 51.64 | 51.64 |  
| CRF<sup>*</sup> | 63.29 | 63.29 | 63.29 |  
| bi-LSTM-CRF standard | 70.74 (0.151) | 70.32 (0.130) | 70.56 (0.148) |  
|**bi-LSTM-CRF ELMo** | **73.36 (0.568)** | **73.32 (0.556)** | **73.34 (0.591)** |


Results across Genres. Scores are the average of P and R per class over 5 multiple runs. Numbers in brackets indicate standard deviation.

| Train/Test |      News     |      News     |     Guides    |     Guides    |    Reports    |    Reports    |
|------------|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
|            |       P       |       R       |       P       |       R       |       P       |       R       |
| **News**       | 74.90 (1.074) | 76.68 (0.526) | 38.90 (0.919) | 43.10 (0.738) | 54.74 (0.861) | 59.74 (1.031) |
| **Guides**     | 60.44 (0.808) | 64.30 (1.635) | 64.62 (1.028) | 65.82 (1.202) | 55.02 (1.461) | 56.68 (1.121) |
| **Reports**    | 77.22 (0.901) | 78.26 (0.835) | 49.56 (1.006) | 51.12 (1.136) | 69.04 (0.709) | 69.56 (0.391) |



Results across Time. Scores are the average of P and R per class over 5 multiple runs. Numbers in brackets indicate standard deviation.

|  Train/Test  |  Contemporary |  Contemporary |   Historical  |   Historical  |
|:------------:|:-------------:|:-------------:|:-------------:|:-------------:|
|              |       P       |       R       |       P       |       R       |
| **Contemporary** | 73.26 (0.996) | 73.72 (0.804) | 67.54 (1.154) | 67.96 (0.541) |
| **Historical**   | 65.80 (1.902) | 67.20 (1.713) | 72.70 (1.004) | 73.30 (0.812) |


