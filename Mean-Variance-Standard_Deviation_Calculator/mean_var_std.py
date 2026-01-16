import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  c = np.array(list).reshape(3, 3)

  calculations = {
    'mean': [c.mean(axis=0).tolist(), c.mean(axis=1).tolist(), c.mean().tolist()],
    'variance': [c.var(axis=0).tolist(), c.var(axis=1).tolist(), c.var().tolist()],
    'standard deviation': [c.std(axis=0).tolist(), c.std(axis=1).tolist(), c.std().tolist()],
    'max': [c.max(axis=0).tolist(), c.max(axis=1).tolist(), c.max().tolist()],
    'min': [c.min(axis=0).tolist(), c.min(axis=1).tolist(), c.min().tolist()],
    'sum': [c.sum(axis=0).tolist(), c.sum(axis=1).tolist(), c.sum().tolist()]
  }

  return calculations