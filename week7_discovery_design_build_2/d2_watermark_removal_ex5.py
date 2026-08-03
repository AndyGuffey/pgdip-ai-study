# Strips the watermark marker from text and re-runs the same detector
# from week7_discovery_design_build_2/d2_watermark_detection_ex4.py
# against the cleaned version.
# Learning purpose: demonstrate that this style of watermarking is
# trivially defeated by a simple find-and-replace — a single string
# substitution removes the signal entirely, motivating the need for
# more robust (e.g. statistical/model-level) watermarking schemes.

def detect_watermark(text: str, marker="âŸ‚", threshold=0.05):
    tokens = text.split()
    ratio = tokens.count(marker) / max(len(tokens), 1)
    return ratio > threshold, ratio

def remove_marker(text, marker="âŸ‚"):
    return text.replace(marker, "")

wm = "This is a demo text with a watermark marker âŸ‚ inside."

cleaned = remove_marker(wm)
detected, score = detect_watermark(cleaned)

print("After editing:")
print("Detected:", detected, "Score:", score)