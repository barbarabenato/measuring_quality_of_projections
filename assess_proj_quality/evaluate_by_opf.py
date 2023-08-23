import sys
import csv
import numpy as np
from label_propag import OPFSemi
from sklearn.metrics import cohen_kappa_score

if len(sys.argv) != 4:
    sys.exit('\tusage evaluate_by_opf.py <X_2d_data> <y_2d_data> <perc of sup samples>')

# reading 2d data
X = np.array(list(csv.reader(open(sys.argv[1], "r"), quoting=csv.QUOTE_NONNUMERIC)), dtype="float32")
y = np.array(list(csv.reader(open(sys.argv[2], "r"), quoting=csv.QUOTE_NONNUMERIC)), dtype="int8").squeeze()
perc_samples = float(sys.argv[3])

# randomly choosing supervised samples
idx_samples = np.random.randint(0, high=len(X), size=(int(len(X)*perc_samples),))

# propagating labels
y_labeled = OPFSemi(X, y, idx_samples)

# calculating metric
kappa = cohen_kappa_score(y, y_labeled)
print("Kappa: %.6f" % (kappa))
