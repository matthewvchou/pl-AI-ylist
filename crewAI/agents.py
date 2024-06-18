from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from crewai_tools import SerperDevTool
search_tool = SerperDevTool()


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class PlaylistAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    def music_critic(self):
        return Agent(
            role="Professional Music Critic",
            backstory=dedent(f"""Professional music critic. You have decades of experience making playlists"""),
            goal=dedent(f"""
                        Create a Spotify playlist 50 songs long that includes songs that are similar to the selected artist, song, or album. The playlist should include a creative title as well. The output should be a text list of all songs on the playlist headed by the playlist title.                         
                        """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            llm=self.OpenAIGPT35
        )

    def artist_specialist(self):
        return Agent(
            role="Musical Artist Specialist",
            backstory=dedent(f"""Musical artist specialist. You only listen to the given artist and know everything there is to know about them."""),
            goal=dedent(f"""
                        Create a summary about an artist with details about their genres, language, common styles, most common demographic, gender, origin, as well as the qualities of their most popular songs.
                        """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            llm=self.OpenAIGPT35
        )

    def artist_finder(self):
        return Agent(
            role="Musical Artist Finder",
            backstory=dedent(f"""Musical artist finder. You specialize in finding musical artists that create music similar to a specific description."""),
            goal=dedent(f"""
                        Create list of 30 artists that fit various qualities of the summary provided. The artists included do not have to fit all of the qualities included, but should be similar in at least most of the qualities.
                        """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            llm=self.OpenAIGPT35
        )
    
    def song_specialist(self):
        return Agent(
            role="Song Specialist",
            backstory=dedent(f"""Song specialist. You have listened to every song in the world and are an expert at discerning which songs are similar."""),
            goal=dedent(f"""
                        Make a list of songs that is similar the summary of an artist and a list of artists that are similar to them. Make this list diverse and do not include too many songs from the same artist.
                        """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            llm=self.OpenAIGPT35
        )
    
    def playlist_assembler(self):
        return Agent(
            role="Hit Playlist Maker",
            backstory=dedent(f"""Hit playlist maker. You are a famous and creative playlist maker that makes hit playlists. You have years of experience creating playlists on Spotify"""),
            goal=dedent(f"""
                        Given a list of songs, create a Spotify playlist with a creative name that relates to the theme, genre, and artist of focus that only includes every song on the list.
                        """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35
        )