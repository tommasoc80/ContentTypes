##Content Types

This repository contains:
- the Content Type Dataset Version 1.5 (in the folder "Datasets");
- the [data statement](https://www.mitpressjournals.org/doi/pdf/10.1162/tacl_a_00041) related to CTD V1.5 (see below);
- a set of spreadsheets containing metadata about the documents included in the dataset, e.g. year of publication, author's name, author's nationality, author's gender (in the folder "Documents_Metadata");
- the data to replicate a set of experiments for the identification of Content Types (in the folder "Datasets");
- the best model for the identification of Content Types obtained adopting the [BiLSTM-CNN-CRF with ELMo-Representations for Sequence Tagging implementation](https://github.com/UKPLab/elmo-bilstm-cnn-crf) by Nils Reimers and Iryna Gurevych (in the folder "Best_Model").


------------

###Data statement

####CURATION RATIONALE: 
We adopt a broad perspective on texts selection assuming that good computational models for NLP must be able to deal with different genres (synchronic dimension) as well as with different times (diachronic dimension). This approach aims at facilitating the re-use of models in different fields of study, and promoting the cross-fertilisation among disciplines, especially in the area of Humanities. On the basis of this approach, we collected texts in English from three different genres: newspaper articles, travel reports, and travel guides. For each of these genres, we collected data published between the second half of the 1800s and the beginning of the 2000s. In designing the corpus, one of our goals was to keep the combination of time and genre as much balanced as possible, in terms of number of tokens and clauses. Furthermore, given the phenomenon under study, we decided to preserve documents' integrity rather than truncating them. 

####LANGUAGE VARIETY:
en-GB, en-US, en-AU.

####ANNOTATOR DEMOGRAPHIC
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

####SPEAKER DEMOGRAPHIC & SPEECH SITUATION: 
Information included in the spreadsheets. 

####TEXT CHARACTERISTICS: 
The combination of the time and genre dimensions gives rise to 6 sub-corpora within our dataset: Contemporary News, Historical News, Contemporary Travel Reports, Historical Travel Reports, Contemporary Travel Guides, Historical Travel Guides. 

