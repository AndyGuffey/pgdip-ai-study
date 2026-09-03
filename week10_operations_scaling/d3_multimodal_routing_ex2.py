# Multimodal (text vs. vision) request routing demo.
# Routes plain text prompts to a cheaper text-only model and image inputs to
# a vision-capable model — a routing pattern that picks the cheapest model
# capable of handling each request's input type.
import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set in the environment.")

client = OpenAI(api_key=OPENAI_API_KEY)

def handle_text(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # text-focused / cheaper model
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

def handle_image(image_url: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",  # vision-capable model
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image in one sentence."},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            }
        ],
    )
    return response.choices[0].message.content

def multimodal_route(input_type: str, content: str) -> str:
    """
    Very simple multimodal router:
    - if input_type == 'text'  -> use text model
    - if input_type == 'image' -> use vision model on the image URL
    """
    if input_type == "text":
        return handle_text(content)
    elif input_type == "image":
        return handle_image(content)
    else:
        return "[ROUTER] Unknown input type."

if __name__ == "__main__":
    # Example 1: pure text query
    text_prompt = "Explain machine learning in one sentence"
    text_answer = multimodal_route("text", text_prompt)
    print("Text prompt:", text_prompt)
    print("Text response:", text_answer)

    # Example 2: real image route using an image URL
    image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"
    image_answer = multimodal_route("image", image_url)
    print("\nImage URL:", image_url)
    print("Image route response:", image_answer)