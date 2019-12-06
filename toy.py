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
    print(ds.insert_labeled_records(X.iloc[[0]], y.iloc[[0]]))
    

if __name__ == "__main__":
    main()