from models.playlist import Playlist
from models.repos.a_playlist import APlaylist
import sqlite3

class PlaylistRepo(APlaylist):
    def create_playlist(self, model: Playlist) -> None:
        pass

    def update_playlist(self, pl_id: int, model: Playlist) -> None:
        pass

    def delete_playlist(self, pl_id: int) -> None:
        pass

    def get_playlist(self, pl_id: int) -> Playlist:
        pass

    def get_all_playlists(self) -> list[Playlist]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM playlists")
                for row in cursor:
                    pl = Playlist(playlist_id=row[0], playlist_name=row[1])
                    data_list.append(pl)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
