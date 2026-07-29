# Calculates the memory footprint of a transformer's KV cache for a given
# model shape (layers, heads, head dimension) across a few sequence
# lengths, without running any actual inference.
# Learning purpose: build intuition for why KV cache size scales linearly
# with sequence length and model size, and why long-context inference is
# memory-bound rather than compute-bound.

import torch

layers = 32
heads = 32
head_dim = 128

for seq in [512, 2048, 8192]:
    size = layers * heads * seq * head_dim * 2  # K & V
    print(seq, "tokens ->", size/1e6, "MB")