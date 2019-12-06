# -*- coding: utf-8 -*-

class Dataset:

    def __init__(self):
        self.unlabeled_dataset = None
        self.labeled_dataset = None
        pass

    def get_features(self):
        pass

    def shape(self):
        pass

    def next(self):
        pass

    def fetch_all(self):
        pass

    def insert_new_unlabels(self, records):
        pass

    def insert_labeled_records(self, records):
        pass

    def get_unlabeled_dataset(self):
        return self.unlabeled_dataset

    def get_labeled_dataset(self):
        return self.labeled_dataset

