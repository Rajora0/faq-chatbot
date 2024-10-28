# Customer Support Chatbot with Streamlit 

## Description

This project implements a simple customer support chatbot using Streamlit for the user interface and a pre-trained machine learning model for intent classification. 

Users can interact with the chatbot by typing in their questions or requests. The chatbot will then predict the intent behind the user's message and provide a pre-defined response based on that intent.

## Features

- User-friendly chatbot interface powered by Streamlit.
- Intent classification using a pre-trained machine learning pipeline. 
- Customizable dictionary mapping intents to corresponding responses.

## Project Structure

```
chatbot-streamlit/
├── app.py                # Main Streamlit application script
├── text_processing.py   # Text preprocessing classes 
└── customer_support_pipeline.pkl     # Trained chatbot pipeline 
```

## Installation

1. Clone the repository: `git clone https://https://github.com/Rajora0/faq-chatbot.git`
2. Navigate to the project directory: `cd app`
3. Create a virtual environment (recommended): `python -m venv .venv`
4. Activate the virtual environment: 
    - Windows: `.venv\Scripts\activate`
    - Linux/macOS: `source .venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`

## Usage

1. Make sure the trained pipeline (`customer_support_pipeline.pkl`) is in the project directory.
2. Run the Streamlit app: `streamlit run app.py`
3. The chatbot interface will open in your web browser.
4. Start typing your messages in the input field.

## Customization

- **Train a new model:** To use a different intent classification model, train your own model and replace `customer_support_pipeline.pkl` with your saved pipeline file. 
- **Update intents and responses:** You can customize the `intent_responses` dictionary in `app.py` to modify existing responses or add new intents and their corresponding responses.

## Contributing

Contributions are welcome! Please open an issue or pull request if you have any suggestions or improvements.

## License

This project is licensed under the [MIT License](LICENSE).
