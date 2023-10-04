import discord
import openai

# Replace <API_KEY> with your API key from OpenAI
openai.api_key = "<API_KEY>"

# Use the GPT-3 language model
model_engine = "text-davinci-003"

# Create a Discord client
client = discord.Client(intents=discord.Intents.default())


# Event that runs when the bot is ready to start working
@client.event
async def on_ready():
    print(f"Logged in as {client.user}.")


# Event that runs when the bot receives a message
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return
    if message.content.startswith("?"):
        # Extract the question from the message
        question = message.content.split(" ")[1:]
        question = " ".join(question)
        # Generate a response with the GPT-3 language model
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=question,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completions.choices[0].text

        # Send the response back to the user
        await message.channel.send(response)


# Replace <DISCORD_TOKEN> with your Discord bot token
client.run("<DISCORD_TOKEN>")
