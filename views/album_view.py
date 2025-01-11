from models.repos.album_repo import AlbumRepo
from models.album import Album

def view_album():
    """Fetches and displays all album types."""
    try:
        gr = AlbumRepo()
        ga_alb = gr.get_all_albums()
        if not ga_alb:
            print("No Album types found.")
        else:
            print("Album Table Data \n----------------")
            for li in ga_alb:
                print(f"Album Id : {li.album_id} , Title : {li.album_title} , Artist Id = {li.artist_id}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_album_type_by_id(alb_id: int):
    """Fetches and displays a album type by ID."""
    try:
        albrepo = AlbumRepo()
        ga = albrepo.get_album(alb_id)
        if ga:
            print(f"Id: {ga.album_id}, Title: {ga.album_title}, Artist Id = {ga.artist_id}")
        else:
            print(f"No Album type found with ID {alb_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def view_created_album():
    """Create a Album"""
    try:
        albumid = input("Enter Album Id : ")
        albumtitle = input("Enter Album title : ")
        artistid = input("Enter Artist Id : ")
        insertalbum = Album(albumid,albumtitle,artistid)
        cgr = AlbumRepo()
        cgr.create_album(insertalbum)
        view_album()
    except Exception as e:
        print(f"An error occured : {e}")

def view_update_album():
    """Update a Album"""
    try:
        albumid = input("Enter Album Id : ")
        albumtitle = input("Enter Album title : ")
        artistid = input("Enter Artist Id : ")
        ug = Album(albumid,albumtitle,artistid)
        cgr = AlbumRepo()
        cgr.update_album(albumid,ug)
        view_album()
    except Exception as e:
        print(f"An error occured : {e}")

def view_delete_album():
    """Delete a Album"""
    try:
        albumid=input("Enter album id which you want to delete : ")
        dgtr=AlbumRepo()
        dgtr.delete_album(albumid)
        view_album()
    except Exception as e:
        print(f"An error occured : {e}")
     
if __name__ == "__main__":
    print("Choose an option:")
    print("1. View all album types")
    print("2. View album type by ID")
    print("3. Create album type ")
    print("4. Update album type ")
    print("5. Delete album type ")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_album()
    elif choice == "2":
        try:
            alb_id = int(input("Enter Album Type ID: "))
            view_album_type_by_id(alb_id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
    elif choice == "3":
        view_created_album()
    elif choice == "4":
        view_update_album()
    elif choice == "5":
        view_delete_album()  
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4 or 5.")
    