# -*- coding: utf-8 -*-

class Dataset:
    self.dataset = None

    def __init__(self):
        pass

    def get_features(self):
        pass

    def get_labels(self):
        pass

    def shape(self):
        pass

    def next(self):
        pass

    def fetch_all(self):
        pass

    def read_batch(self, size_batch):
        pass

    def get_dataset(self):
        return self.dataset