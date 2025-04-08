# Ubongo_Translation_Tool

An AI-powered translation tool developed using OpenAI’s GPT model, designed to generate translations in various tones (formal, conversational, humorous). The tool includes a Flask backend and a JavaScript frontend, allowing for user interactivity and real-time feedback for continuous improvement.

## Features
- **Tone Customization**: Users can choose between formal, conversational, and humorous tones for translations.
- **Real-time Feedback**: Allows users to provide feedback, improving translation accuracy over time.
- **AI-powered**: Leverages OpenAI’s GPT model for accurate and dynamic translations.
- **Interactive Frontend**: Built with JavaScript to enhance user interaction.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: JavaScript, HTML, CSS
- **AI Model**: OpenAI GPT
- **Libraries**: Flask, OpenAI API, requests, etc.

## Installation Instructions
To get started, follow these steps:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/Ubongo_Translation_Tool.git

# 2. Navigate to the project directory
cd Ubongo_Translation_Tool

# 3. Create a virtual environment (optional but recommended)
python -m venv venv

# 4. Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 5. Install the required dependencies
pip install -r requirements.txt

# 6. Set up the OpenAI API key by adding it to your environment variables or the `.env` file.
