# Hashes two near-identical dataset versions (an MD5 digest of the data)
# to show even a single changed value produces a completely different
# hash, then splits a dataset into train/eval slices.
# Learning purpose: understand dataset versioning/fingerprinting (via
# content hashing) as an ML ops practice for detecting exactly when
# training data has changed, alongside the basic train/eval split it
# would apply to.

import hashlib

def dataset_hash(data):
    return hashlib.md5(str(data).encode()).hexdigest()

data_v1 = [1, 2, 3, 4, 5]
data_v2 = [1, 2, 3, 4, 6]  # small change

print("v1 hash:", dataset_hash(data_v1))
print("v2 hash:", dataset_hash(data_v2))

train = data_v1[:3]
eval_set = data_v1[3:]

print("Train:", train)
print("Eval:", eval_set)