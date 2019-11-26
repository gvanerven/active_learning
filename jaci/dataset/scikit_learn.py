# -*- coding: utf-8 -*-
from jaci.dataset import Dataset
from sklearn import skdatasets

class Iris(Dataset):
    def __init__(self):
        self.dataset = skdatasets.load_iris()