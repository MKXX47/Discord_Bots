# Discord Bot with OpenAI GPT-3 Integration

This Discord bot integrates with the OpenAI GPT-3 language model to answer questions that start with a question mark ("?"). It generates responses based on the provided question and sends them back to the user.

## Prerequisites

Before you can use this bot, you'll need the following:
- **Discord API Token:** Replace `<DISCORD_TOKEN>` with your Discord bot token.
- **OpenAI API Key:** Replace `<API_KEY>` with your OpenAI API key.

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/your-repo.git

2. Install the required Python packages:
pip install discord openai

3. Replace the placeholders in the code with your Discord API token and OpenAI API key:
```python
openai.api_key = "<API_KEY>"
client.run("<DISCORD_TOKEN>")
