#!/usr/bin/env python3

from __future__ import print_function
import BIOF1Validation
import logging
from CoNLL import readCoNLL 
import preprocessing_lite
import argparse
from conllFunctions import count_chunks
from conllFunctions import get_result
from conllFunctions import plot_results


parser = argparse.ArgumentParser()

parser.add_argument("-l","--label", help="specify label column name e.g CT_IOB where IOB is the schema used in the evaluation.")
parser.add_argument("test_run_path", help="the run to evaluate")
parser.add_argument("gold_run_path", help="the gold used in the avluation")
args = parser.parse_args()

labelKey = args.label

gusssedPath = args.test_run_path
goldPath = args.gold_run_path





casing2Idx = preprocessing_lite.getCasingVocab()
mappings = {'tokens': {}, 'casing': casing2Idx}
idx2Labels = {}


trainSentences = readCoNLL(gusssedPath, {0:'tokens', 1:labelKey}, None)
goldSentences = readCoNLL(goldPath, {0:'tokens', 1:labelKey}, None)


preprocessing_lite.extendMappings(mappings, trainSentences+goldSentences)

charset = {"PADDING":0, "UNKNOWN":1}
for c in " 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,-_()[]{}!?:;#'\"/\\%$`&=*+@^~|":
    charset[c] = len(charset)
mappings['characters'] = charset

idx2Labels = {v: k for k, v in mappings[labelKey].items()}

preprocessing_lite.addCharInformation(trainSentences)
preprocessing_lite.addCasingInformation(trainSentences)
preprocessing_lite.addCharInformation(goldSentences)
preprocessing_lite.addCasingInformation(goldSentences)



guessedMatrirx = preprocessing_lite.createMatrices(trainSentences, mappings, False)
goldMatrirx = preprocessing_lite.createMatrices(goldSentences, mappings, False)


correctLabels = [goldMatrirx[idx][labelKey] for idx in range(len(goldMatrirx))]
predictLabels = [guessedMatrirx[idx][labelKey] for idx in range(len(guessedMatrirx))]


encodingScheme = labelKey[labelKey.index('_')+1:]


pre, rec, f1 = BIOF1Validation.compute_f1(predictLabels, correctLabels, idx2Labels, 'B', encodingScheme)

print("Test-Data: Prec: %.4f, Rec: %.4f, F1: %.4f" % (pre, rec, f1))


# from index to labales 
label_pred = []
for sentence in predictLabels:
    for element in sentence:
        label_pred.append(idx2Labels[element])   

label_correct = []
for sentence in correctLabels:
    for element in sentence:
        label_correct.append(idx2Labels[element])

# use functions from conll script
(correct_chunks, true_chunks, pred_chunks, correct_counts, true_counts, pred_counts) = count_chunks(label_correct, label_pred)
result = get_result(correct_chunks, true_chunks, pred_chunks,correct_counts, true_counts, pred_counts, verbose=True)

plot_results(label_correct,label_pred)