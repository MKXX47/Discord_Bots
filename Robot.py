import time

import requests
import discord
import openai

# Use the API key for OpenAI
openai.api_key = "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"

# Use the GPT-3 language model
model_engine = "text-davinci-003"

# Replace <API_KEY> with your TMDb API key
API_KEY = 'f829c05af5887538f100ecd7d49eb2b7'

# Discord client setup
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_message(message):
    if message.content.startswith("/movie"):
        # Extract the movie name from the message
        movie_name = message.content.split(" ")[1:]
        movie_name = " ".join(movie_name)

        # Search for the movie using the TMDb API
        response = requests.get(
            f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}").json()

        if response["total_results"] > 0:
            # Get the first result
            movie = response["results"][0]

            # Get the movie information
            movie_id = movie["id"]
            movie_info = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}").json()

            # Get the movie poster
            poster_path = movie_info.get("poster_path")
            if poster_path:
                poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
                poster_response = requests.get(poster_url)

                if poster_response.status_code == 200:
                    # Send the movie information and poster to Discord
                    with open("poster.jpg", "wb") as f:
                        f.write(poster_response.content)
                    await message.channel.send(file=discord.File("poster.jpg"),
                                               content=f"Title: {movie_info['title']}\n"
                                                       f"Release Date: {movie_info['release_date']}\n"
                                                       f"Overview: {movie_info['overview']}")
                else:
                    # Error getting poster
                    await message.channel.send("Error getting movie poster.")
            else:
                # No poster available
                await message.channel.send(f"Title: {movie_info['title']}\n"
                                           f"Release Date: {movie_info['release_date']}\n"
                                           f"Overview: {movie_info['overview']}\n"
                                           "No poster available.")
        else:
            # Movie not found
            await message.channel.send("Movie not found.")
    if message.content.startswith("/series"):
        # Extract the series name from the message
        series_name = message.content.split(" ")[1:]
        series_name = " ".join(series_name)

        # Search for the series using the TMDb API
        response = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={API_KEY}&query={series_name}").json()

        if response["total_results"] > 0:
            # Get the first result
            series = response["results"][0]

            # Get the series information
            series_id = series["id"]
            series_info = requests.get(f"https://api.themoviedb.org/3/tv/{series_id}?api_key={API_KEY}").json()

            # Get the series poster
            poster_path = series_info.get("poster_path")
            if poster_path:
                poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
                poster_response = requests.get(poster_url)

                if poster_response.status_code == 200:
                    # Send the series information and poster to Discord
                    with open("poster.jpg", "wb") as f:
                        f.write(poster_response.content)
                    await message.channel.send(file=discord.File("poster.jpg"),
                                               content=f"Title: {series_info['name']}\n"
                                                       f"First Air Date: {series_info['first_air_date']}\n"
                                                       f"Overview: {series_info['overview']}")
                else:
                    # Error getting poster
                    await message.channel.send("Error getting series poster.")
            else:
                # No poster available
                await message.channel.send(f"Title: {series_info['name']}\n"
                                           f"First Air Date: {series_info['first_air_date']}\n"
                                           f"Overview: {series_info['overview']}\n"
                                           "No poster available.")
        else:
            # Series not found
            await message.channel.send("Series not found.")
    if message.content.startswith("/spam"):

        raw = message.content.split(" ")[1:2]
        spam_num = int(raw[0])
        user = message.content.split(" ")[2:]
        user = " ".join(user)
        if spam_num > 100:
            spam_num = 100
            await message.channel.send(f'{user} wou well get spamed {spam_num} times :smiling_imp:')
            time.sleep(10)
            await message.channel.send(f'hak lfa9ira tmok {user}')
            time.sleep(10)
            await message.channel.send(f'5od {user}')
            time.sleep(10)
            await message.channel.send(f'zidek hadi {user} :joy:')
            for i in range(spam_num - 4):
                await message.channel.send(user)

        else:
            await message.channel.send(f'{user} wou well get spamed {spam_num} times :smiling_imp:')
            time.sleep(10)
            await message.channel.send(f'hak lfa9ira tmok {user}')
            time.sleep(10)
            await message.channel.send(f'5od {user}')
            time.sleep(10)
            await message.channel.send(f'zidek hadi {user} :joy:')
            for i in range(spam_num - 4):
                await message.channel.send(user)
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
client.run("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
