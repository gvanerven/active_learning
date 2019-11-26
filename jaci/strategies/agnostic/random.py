# -*- coding: utf-8 -*-
from jaci.strategies import Strategy

class RandomSampling(Strategy):

    def __init__(self, dataset):
        self.dataset = dataset

    def query_next(self):
        pass