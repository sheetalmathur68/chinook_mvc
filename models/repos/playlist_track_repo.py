from models.playlist_track import PlaylistTrack
from models.repos.a_playlist_track import APlaylistTrack
import sqlite3

class PlaylistTrackRepo(APlaylistTrack):
    def create_playlist_track(self, model: PlaylistTrack) -> None:
        pass

    def update_playlist_track(self, pl_t_id: int, model: PlaylistTrack) -> None:
        pass

    def delete_playlist_track(self, pl_t_id: int) -> None:
        pass

    def get_playlist_track(self, pl_t_id: int) -> list:
        try:
            with sqlite3.connect("chinook.db") as conn:
                data = conn.execute("SELECT * FROM playlist_track WHERE PlaylistId = ?", (pl_t_id,))
                rows = data.fetchall()  # Fetch all rows matching the PlaylistId

                if rows:
                    # Create a list of PlaylistTrack objects for all matching rows
                    return [PlaylistTrack(playlist_id=row[0], track_id=row[1]) for row in rows]
                else:                                                            
                    print(f"No tracks found for PlaylistId {pl_t_id}")
                    return []
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []


    def get_all_playlist_tracks(self) -> list[PlaylistTrack]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM playlist_track")
                for row in cursor:
                    plt = PlaylistTrack(playlist_id=row[0], track_id=row[1])
                    data_list.append(plt)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
