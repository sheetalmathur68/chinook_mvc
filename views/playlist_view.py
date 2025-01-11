from models.repos.playlist_repo import PlaylistRepo

def view_playlist():
    """Fetches and displays all media types."""
    try:
        plr = PlaylistRepo()
        gapl = plr.get_all_playlists()
        if not gapl:
            print("No media types found.")
        else:
            print("Playlist Table Data \n----------------")
            for li in gapl:
                print(f"Id : {li.playlist_id} , Name : {li.playlist_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def hello():
    print("Hello User")

if __name__=="__main__":
    view_playlist()
    
    