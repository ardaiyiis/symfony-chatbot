import sys
import google.generativeai as genai

def configure_model(api_key):
    """Configures the Generative AI model with the given API key."""
    genai.configure(api_key=api_key)
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 200,
    }
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]
    model = genai.GenerativeModel(
        model_name="gemini-1.0-pro",
        generation_config=generation_config,
        safety_settings=safety_settings
    )
    return model

def main():
    if len(sys.argv) < 3:
        print("Usage: python gemini.py <api_key> <user_input>")
        sys.exit(1)

    api_key = sys.argv[1]
    user_input = sys.argv[2]

    model = configure_model(api_key)
    convo = model.start_chat(history=[])

    try:
        convo.send_message(user_input)
        print(convo.last.text)
    except Exception as e:
        print(f'{type(e).__name__}: {e}')

if __name__ == "__main__":
    main()

  # TODO:
  # - Convorsation history must be arranged
