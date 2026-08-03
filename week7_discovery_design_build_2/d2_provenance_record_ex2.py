# Builds a provenance record for AI-generated content: bundles the
# content with metadata (creator, timestamp), serializes it
# deterministically (sorted keys), then fingerprints the whole thing with
# the same SHA-256 approach from
# week7_discovery_design_build_2/d2_content_fingerprint_ex1.py.
# Learning purpose: see how fingerprinting content alone isn't enough for
# provenance — binding metadata into the hash means any change to either
# the content or its claimed origin invalidates the fingerprint.

import json
import hashlib

def fingerprint(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()

def provenance_record(content, metadata):
    record = {
        "content": content,
        "metadata": metadata
    }
    serialized = json.dumps(record, sort_keys=True)
    return fingerprint(serialized)

metadata = {
    "creator": "AI Generator",
    "timestamp": "2026-01-03"
}

print(provenance_record("Hello world", metadata))