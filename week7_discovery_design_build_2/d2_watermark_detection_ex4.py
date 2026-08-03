# Detects the watermark embedded by
# week7_discovery_design_build_2/d2_text_watermark_ex3.py: counts marker
# tokens as a fraction of total tokens and flags the text as watermarked
# if that ratio exceeds a threshold.
# Learning purpose: see the detection side of watermarking — a cheap,
# approximate signal (marker density) rather than a cryptographic
# guarantee, and how the threshold trades off false positives/negatives.

def detect_watermark(text: str, marker="âŸ‚", threshold=0.05):
    tokens = text.split()
    ratio = tokens.count(marker) / max(len(tokens), 1)
    return ratio > threshold, ratio

# Example watermarked text (simple demo with a few marker tokens)
wm = "This is a demo text with a watermark marker âŸ‚ inside."

detected, score = detect_watermark(wm)
print("Detected:", detected, "Score:", score)