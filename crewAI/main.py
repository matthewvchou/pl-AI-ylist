import os
from crewai import Crew

from textwrap import dedent
from agents import PlaylistAgents
from tasks import PlaylistTasks

from dotenv import load_dotenv
load_dotenv()


class PlaylistCrew:
    def __init__(self, artist):
        self.artist = artist
        self.summary = None
        self.artists = None
        self.songs = None

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = PlaylistAgents()
        tasks = PlaylistTasks()

        # Define your custom agents and tasks here
        music_critic = agents.music_critic()
        artist_specialist = agents.artist_specialist()
        artist_finder = agents.artist_finder()
        song_specialist = agents.song_specialist()
        playlist_assembler = agents.playlist_assembler()

        # Custom tasks include agent name and variables as input
        make_playlist = tasks.make_playlist(
            music_critic,
            self.artist
        )

        artist_information = tasks.artist_information(
            artist_specialist,
            self.artist
        )

        similar_artists = tasks.similar_artists(
            artist_finder,
            self.artists,
            self.summary
        )

        song_selection = tasks.song_selection(
            song_specialist,
            self.artists,
            self.summary
        )

        title_compilation = tasks.title_compilation(
            playlist_assembler,
            self.songs,
            self.summary
        )

        # Define your custom crew here
        crew = Crew(
            agents=[music_critic, artist_specialist, artist_finder, song_specialist, playlist_assembler],
            tasks=[make_playlist, artist_information, similar_artists, song_selection, title_compilation],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to PlAIylist!")
    print("-------------------------------")
    artist = input(dedent("""What artist do you like?: """))

    custom_crew = PlaylistCrew(artist)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom playlist:")
    print("########################\n")
    print(result)