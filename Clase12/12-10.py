#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 12.10


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


def funct_principal():
    iris_dataset = load_iris()
    iris_dataframe = pd.DataFrame(
        iris_dataset['data'], columns=iris_dataset.feature_names)
    iris_dataframe['target'] = iris_dataset['target']
    df = sns.load_dataset('tips')
    sns.pairplot(iris_dataframe, hue='target', palette='husl')
    plt.show()


if __name__ == "__main__":
    funct_principal()
