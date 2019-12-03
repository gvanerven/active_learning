# -*- coding: utf-8 -*-
from jaci.dataset import Dataset
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd

class Iris(Dataset):
    def __init__(self, perc_label):
        dataset = datasets.load_iris()
        self.unlabel_features, self.label_features, self.unlabel_labels, self.label_labels = train_test_split(dataset.data,
            dataset.target, test_size=perc_label, random_state=42)

    def get_features(self):
        pass

    def shape(self):
        pass

    def next(self):
        pass

    def fetch_all(self):
        pass

    def save_new_unlabels(self, records):
        pass

    def save_labeled_records(self, records):
        pass

    def get_unlabeled_dataset(self):
        return self.unlabeled_dataset

    def get_labeled_dataset(self):
        return self.labeled_dataset

    def unlabeled_as_pandas(self):
        pass

    def labeled_as_pandas(self):
        pass