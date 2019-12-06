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
        unlabeled_features, labeled_features, unlabeled_labels, labeled_labels = train_test_split(dataset.data,
            dataset.target, test_size=perc_label, random_state=42)
        self.unlabeled_features = pd.DataFrame(unlabeled_features, columns=dataset.feature_names)
        self.labeled_features = pd.DataFrame(labeled_features, columns=dataset.feature_names)
        self.unlabeled_labels = pd.DataFrame(unlabeled_labels, columns=["label"])
        self.labeled_labels = pd.DataFrame(labeled_labels, columns=["label"])

    def get_features(self):
        return self.unlabeled_features

    def shape(self):
        return self.unlabeled_features.shape

    def shape_labeled(self):
        return self.labeled_features.shape

    def next(self):
        self.count += 1
        return self.unlabeled_features[self.count]

    def fetch_all(self):
        return self.unlabeled_features

    def insert_new_unlabels(self, records):
        pass

    def insert_labeled_records(self, records, labels):
        bf = self.labeled_features.shape[0]
        self.labeled_features = np.append(self.labeled_features, records, axis=0)
        self.labeled_labels = np.append(self.labeled_labels, labels, axis=0)
        return self.labeled_features.shape[0] == bf + records.shape[0]

    def get_unlabeled_dataset(self):
        return self.unlabeled_features

    def get_unlabeled_labels(self):
        return self.unlabeled_labels

    def get_labeled_dataset(self):
        return self.labeled_features, self.label_labels
