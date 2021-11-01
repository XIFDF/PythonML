
import deepchem as dc
import numpy as np
N_samples = 50
n_features = 10
X = np.random.rand(N_samples, n_features)
y = np.random.rand(N_samples)
dataset = dc.data.NumpyDataset(X, y)
dataset.X.shape
(50, 10)
dataset.y.shape
(50,)

dataset = dc.data.DiskDataset.from_numpy(X, y)
dataset.X.shape
(50, 10)
dataset.y.shape
(50,)

smiles = [
  'O=Cc1ccc(O)c(OC)c1',
  'CN1CCC[C@H]1c2cccnc2',
  'C1CCCCC1',
  'c1ccccc1',
  'CC(=O)O',
]
properties = [0.4, -1.5, 3.2, -0.2, 1.7]
featurizer = dc.feat.CircularFingerprint(size=1024)
ecfp = featurizer.featurize(smiles)
ecfp.shape
(5, 1024)
dataset = dc.data.NumpyDataset(X=ecfp, y=np.array(properties))
len(dataset)
5