import pandas as pd
import numpy as np
import sklearn
import os
from importlib import resources
from test_tscai_1.utils import transform_labels, read_all_datasets, prepare_data
import torch
from torch.utils.data import DataLoader, TensorDataset


def Classifiers(datasets_dict, dataset_names, classifier_names):

    for dataset_name in dataset_names:
        for classifier_name in classifier_names:
            print('Classifier Type: ', classifier_name)   
            trainloader, valloader, input_shape, nb_classes = prepare_data(datasets_dict, dataset_name, classifier_name)
            
            if classifier_name == 'fcn':
                from test_tscai_1.models import fcn
                print('Everything is ok and now FCN is calling')
                return fcn.fit(trainloader, valloader, input_shape, nb_classes)

            elif classifier_name == 'cnn':
                from test_tscai_1.models import cnn
                print('Everything is ok and now CNN is calling')
                return cnn.fit(trainloader, valloader, input_shape, nb_classes)

            elif classifier_name == 'mlp':
                from test_tscai_1.models import mlp
                print('Everything is ok and now MLP is calling')
                return mlp.fit(trainloader, valloader, input_shape, nb_classes)

            elif classifier_name == 'resnet':
                from test_tscai_1.models import resnet
                print('Everything is ok and now RESNET is calling')
                return resnet.fit(trainloader, valloader, input_shape, nb_classes)

            elif classifier_name == 'inception':
                from test_tscai_1.models import inception
                print('Everything is ok and now INCEPTION is calling')
                return inception.fit(trainloader, valloader, input_shape, nb_classes)