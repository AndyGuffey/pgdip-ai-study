# 4-bit (QLoRA-style) quantized model loading via bitsandbytes.
# Note: this is a snippet, not a runnable script — it needs
# `from transformers import AutoModelForCausalLM` and a `model_name`
# string (e.g. from d1_minimal_sft_trainer_ex2.py) defined before use,
# and the `bitsandbytes` package installed.
from transformers import BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype="float16",
    bnb_4bit_quant_type="nf4"
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map="auto"
)