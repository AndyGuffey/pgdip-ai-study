# Defines an OpenAI "function calling" tool schema: this tells the model an
# `add_numbers(a, b)` function is available, along with the shape of the
# arguments it must supply (two required numbers, `a` and `b`), so the model
# can respond with a structured tool call instead of freeform text when a
# request calls for adding two numbers.

tools = [{
    "type": "function",
    "function": {
        "name": "add_numbers",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "number",
                },
                "b": {
                    "type": "number"
                }
            },
            "required": ["a", "b"]
        }
    }
}]
