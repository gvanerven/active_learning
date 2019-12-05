# -*- coding: utf-8 -*-
from jaci.dataset.scikit_learn import Iris

def main():
    """
    """
    ds = Iris()
    print(ds.shape())
    print(ds.shape_labeled())
    X = ds.get_unlabeled_dataset()
    y = ds.get_unlabeled_labels()
    #print(X[0,])
    print(type(y))
    print(y.shape)
    print("a:", y[0,])
    print(ds.insert_labeled_records(X[0,].reshape(1,4), y[0,]))

if __name__ == "__main__":
    main()