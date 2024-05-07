import numpy as np

def calculate(myList):
    if len(myList) == 9:
        myArray = np.array([myList[:3],myList[3:-3],myList[-3:]])
        calculations                       = {}
        calculations['mean']               = [myArray.mean(axis=0).tolist(), myArray.mean(axis=1).tolist(), myArray.mean()]
        calculations['variance']           = [myArray.var(axis=0).tolist(), myArray.var(axis=1).tolist(), myArray.var()]
        calculations['standard deviation'] = [myArray.std(axis=0).tolist(), myArray.std(axis=1).tolist(), myArray.std()]
        calculations['max']                = [myArray.max(axis=0).tolist(), myArray.max(axis=1).tolist(), myArray.max()]
        calculations['min']                = [myArray.min(axis=0).tolist(), myArray.min(axis=1).tolist(), myArray.min()]
        calculations['sum']                = [myArray.sum(axis=0).tolist(), myArray.sum(axis=1).tolist(), myArray.sum()]
    else:
        raise ValueError('List must contain nine numbers.')
    return calculations