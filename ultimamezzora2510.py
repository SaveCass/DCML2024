import pandas as pd
import sklearn as s
from sklearn.model_selection import train_test_split

if __name__ == "__main__":

    #0_load dataset PANDAS / NUMPY 
    my_dataset = pd.read_csv("labelled_dataset.csv")
    label_obj = my_dataset["label"]
    data_obj = my_dataset.drop(columns=["label"])

    #1_split
    train_data, test_data, train_label, test_label = \
    train_test_split(my_dataset,label_obj,test_size = 0.8)

    #2_choose classiFIRE SCIKIT LEARN
    a=1
    #3_train

    #4_test