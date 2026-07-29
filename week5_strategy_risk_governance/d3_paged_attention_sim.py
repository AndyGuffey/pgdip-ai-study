# Toy simulation of paged KV cache allocation (as used by vLLM-style
# serving engines): tokens are packed into fixed-size "pages"/blocks
# instead of one contiguous growing buffer, and a new page is started
# once the current one is full.
# Learning purpose: understand the core idea behind paged attention —
# allocating cache memory in fixed-size blocks to reduce fragmentation
# and enable efficient batching of variable-length sequences.

cache = []
BLOCK = 4  # tokens per block

def add_tokens(n):
    while n > 0:
        space = BLOCK - (len(cache[-1]) if cache else 0)
        take = min(space, n)
        if not cache or space == 0:
            cache.append([])  # new page
        cache[-1].extend([1]*take)
        n -= take

add_tokens(10)
print("Pages:", len(cache))