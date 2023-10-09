import time

import requests
import discord
import openai

# Replace <API_KEY> with your TMDb API key
API_KEY = '<API_KEY>'

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

# Replace <DISCORD_TOKEN> with your Discord bot token
client.run("<DISCORD_TOKEN>")
