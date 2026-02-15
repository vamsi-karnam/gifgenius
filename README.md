# gifgenius
A chatbot that tries to reply with the perfect witty GIF for anything you ask it.

## Instructions
1. Clone the repo to local
2. Install the requirements
   - pip install requirements.txt
4. Get an API key from [Klipy](https://klipy.com/developers)
5. Get an API key from [OpenAI](https://platform.openai.com/api-keys)
6. Navigate to "klipy_gifs"
7. Create a ".env" file and write the following into the file:
   - KLIPY_API_KEY="klipy_api_key_in_quotes"
   - OPENAI_API_KEY="openai_api_key_in_quotes"
8. From a terminal run:
   - streamlit run .\chatbot_app.py
