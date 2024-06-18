from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class PlaylistTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def make_playlist(self, agent, artist):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a Spotify playlist 50 songs long
            **Description**: Based on the user's artist input, create a 50 song long playlist on Spotify that includes songs from the artist and songs similar to the artist. You must include mostly songs that are not made by {artist}. The output should be a text list of all 50 songs as well as the title of the playlist itself.

            **Parameters**:
            - Artist: {artist}

            **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
        )

    def artist_information(self, agent, artist):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a summary about an artist
            **Description**: Create an in-depth summary about an artist with details about their genres, language, common styles, most common demographic, gender, as well as the qualities of their most popular songs. Keep it specific to the artist and do not include any information not involved with the specific artist. The output should be around 2 paragraphs long.

            **Parameters**:
            - Artist: {artist}

            **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
        )
    
    def similar_artists(self, agent, summary):
        return Task(
            description=dedent(
                f"""
            **Task**: Create a list of artists that share qualities to the selected artist
            **Description**: Create a list of 30 different artists similar to the summary of an artist provided. This list should include both male and female performers as well as groups of more than 1 person. Artists should not be repeated. Qualities do not have to match exactly, but the list should still include artists that are at least very similar in style to the summary.

            **Parameters**:
            - Summary: {summary}

            **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
        )
    
    def song_selection(self, agent, artists, summary):
        return Task(
            description=dedent(
                f"""
            **Task**: Create a list of 50 songs that come from the selected artist and match similar qualities to the summary provided
            **Description**: Create a list of 50 songs created by various artists on the list. These songs should come exclusively from the list of artists. Additionally, these songs should share similar qualities to the summary provided. They do not need to match exactly, but should at least share a similar style to the summary provided.

            **Parameters**:
            - Artists: {artists}
            - Summary: {summary}

            **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
        )
    
    def title_compilation(self, agent, songs, summary):
        return Task(
            description=dedent(
                f"""
            **Task**: Display the final playlist and come up with a creative name for it
            **Description**: Compile all 50 songs into a comprehensive, numbered playlist. It must include all 50 songs exactly once. Additionally, come up with a creative name for the playlist that links the main points of the summary to the songs on the list. You should display the entire list as well as the name at the top.

            **Parameters**:
            - Songs: {songs}
            - Summary: {summary}

            **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
        )