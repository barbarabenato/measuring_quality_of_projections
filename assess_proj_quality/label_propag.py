import pyift.pyift as ift
import sys
import numpy as np

def OPFSemi(x, y, samples, conf=0.0):
    """ 
    It creates iftdataset format and calls OPFSemi.
    :param x: data features
    :param y: data labels
    :param samples: index of samples to be considered as supervised
    :param conf_threshold: threshold value to be used for OPFSemi confidence [0,1]. 
    Samples with threshold up to the confidence will be selected to retrain the feature
    learning in the next iteration. To select all samples, conf_threshold=0.0
    return: pseudolabels and confidence values
    """
    x = np.asarray(x, dtype="float32")
    y = np.asarray(y.reshape(y.shape[0],), dtype="int32")
    # creating opfdataset with provided features
    Z = ift.CreateDataSetFromNumPy(x, y+1) # opf dataset considers labels as [1,n]
    # defining status as training (4) for all samples
    stat = np.full((x.shape[0],), fill_value=(4), dtype="uint32")
    # defining status as supervised (68) for supervised samples
    stat[samples] = 68
    Z.SetStatus(np.array(stat, dtype="int32"))
    Z.SetTrueLabels(np.array(y+1, dtype="int32"))
    Z.SetNTrainSamples(x.shape[0])

    # creating graph and obtaining certainty values
    graph = ift.SemiSupTrain(Z)
    
    labels = Z.GetLabels()-1

    return labels