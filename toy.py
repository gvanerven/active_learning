# -*- coding: utf-8 -*-
from jaci.dataset.scikit_learn import Iris

def main():
    """
    """
    ds = Iris()
    print(type(ds.as_pandas()))

if __name__ == "__main__":
    main()