# -*- coding: utf-8 -*-
from jaci.dataset import Dataset
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

class Iris(Dataset):
    def __init__(self, perc_label=0.3):
        self.count = -1
        dataset = datasets.load_iris()
        self.unlabel_features, self.label_features, self.unlabel_labels, self.label_labels = train_test_split(dataset.data,
            dataset.target, test_size=perc_label, random_state=42)

    def get_features(self):
        return self.unlabel_features

    def shape(self):
        return self.unlabel_features.shape

    def shape_labeled(self):
        return self.label_features.shape

    def next(self):
        self.count += 1
        return self.unlabel_features[self.count]

    def fetch_all(self):
        return self.unlabel_features

    def insert_new_unlabels(self, records):
        pass

    def insert_labeled_records(self, records, labels):
        bf = self.label_features.shape[0]
        print(records.shape)
        print(labels.shape)
        print(self.label_features.shape)
        print(self.label_labels.shape)
        self.label_features = np.append(self.label_features, records, axis=0)
        self.label_labels = np.append(self.label_labels, labels, axis=0)
        return self.label_features.shape[0] == bf + records.shape[0]

    def get_unlabeled_dataset(self):
        return self.unlabel_features

    def get_unlabeled_labels(self):
        return self.unlabel_labels

    def get_labeled_dataset(self):
        return self.label_features, self.label_labels

    def unlabeled_as_pandas(self):
        pass

    def labeled_as_pandas(self):
        pass