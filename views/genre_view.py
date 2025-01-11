from models.repos.genre_repo import GenreRepo
from models.genre import Genre

def view_genre():
    """Fetches and displays all genre types."""
    try:
        gr = GenreRepo()
        gagenre = gr.get_all_genres()
        if not gagenre:
            print("No genre types found.")
        else:
            print("Genre Table Data \n----------------")
            for li in gagenre:
                print(f"Id : {li.genre_id} , Name : {li.genre_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_genre_type_by_id(gt_id: int):
    """Fetches and displays a genre type by ID."""
    try:
        gtr = GenreRepo()
        gt = gtr.get_genre(gt_id)
        if gt:
            print(f"Id: {gt.genre_id}, Name: {gt.genre_name}")
        else:
            print(f"No genre type found with ID {gt_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def view_created_genre():
    """Create a Genre"""
    try:
        genreid = input("Enter Genre Id : ")
        genrename = input("Enter Genre Name : ")
        insertgenre = Genre(genreid,genrename)
        cgr = GenreRepo()
        cgr.create_genre(insertgenre)
        view_genre()
    except Exception as e:
        print(f"An error occured : {e}")

def view_update_genre():
    """Update a Genre"""
    try:
        genreid = input("Enter Genre Id : ")
        genrename = input("Enter Genre Name : ")
        ug = Genre(genreid,genrename)
        cgr = GenreRepo()
        cgr.update_genre(genreid,ug)
        view_genre()
    except Exception as e:
        print(f"An error occured : {e}")

def view_delete_genre():
    """Delete a genre"""
    try:
        genreid=input("Enter genre id which you want to delete : ")
        dgtr=GenreRepo()
        dgtr.delete_genre(genreid)
        view_genre()
    except Exception as e:
        print(f"An error occured : {e}")
     
if __name__ == "__main__":
    print("Choose an option:")
    print("1. View all genre types")
    print("2. View genre type by ID")
    print("3. Create genre type ")
    print("4. Update genre type ")
    print("5. Delete genre type ")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_genre()
    elif choice == "2":
        try:
            gt_id = int(input("Enter Genre Type ID: "))
            view_genre_type_by_id(gt_id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
    elif choice == "3":
        view_created_genre()
    elif choice == "4":
        view_update_genre()
    elif choice == "5":
        view_delete_genre()  
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4 or 5.")
    
    
    
    
    