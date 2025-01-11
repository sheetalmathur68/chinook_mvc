from models.repos.playlist_track_repo import PlaylistTrackRepo

def view_playlist_track():
    """Fetches and displays all media types."""
    try:
        pltr = PlaylistTrackRepo()
        gaplt = pltr.get_all_playlist_tracks()
        if not gaplt:
            print("No media types found.")
        else:
            print("Playlist Table Data \n----------------")
            for li in gaplt:
                print(f" Playlist Id : {li.playlist_id} , Track ID : {li.track_id}")
    except Exception as e:
        print(f"An error occurred: {e}")
def view_playlist_track_by_id(pl_t_id: int):
    """
    Fetches and displays all tracks associated with a given playlist ID.
    """
    try:
        print(f"Fetching playlist tracks for Playlist ID: {pl_t_id}...\n")

        # Create a PlaylistTrackRepo instance
        ptr = PlaylistTrackRepo()

        # Fetch the playlist tracks using the repository
        playlist_tracks = ptr.get_playlist_track(pl_t_id)  # Assuming this fetches multiple tracks
        
        if playlist_tracks:
            print(f"Tracks found for Playlist ID {pl_t_id}:\n")
            for track in playlist_tracks:
                print(f"Playlist ID: {track.playlist_id}, Track ID: {track.track_id}")
            print("\nFetch completed successfully.")
        else:
            print(f"No tracks found for Playlist ID {pl_t_id}.")

    except Exception as e:
        print(f"An error occurred while fetching playlist tracks: {e}")


        
        
if __name__ == "__main__":
    print("Choose an option:")
    print("1. View all playlist track")
    print("2. View playlist track by ID")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_playlist_track()
    elif choice == "2":
        try:
            pl_t_id = int(input("Enter playlist track ID: "))
            view_playlist_track_by_id(pl_t_id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
    else:
        print("Invalid choice. Please choose 1 or 2.")
    
    
    