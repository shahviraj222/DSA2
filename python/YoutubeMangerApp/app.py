import json

def load_data():
    try:
        with open('youtube_data.txt','r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube_data.txt','w') as file:
        json.dump(videos,file)

def list_all_video(videos):
    # Only for presentaiton
    print("\n")  
    print("*" * 137)
    print("\n")  
    temp = enumerate(videos,start=1)
    for index,vid in temp:
        print(f"{index}.{vid['name']},  Duration: {vid["time"]}")   
    print("\n")     
    print("*" * 137)

def add_video(videos):
    name = input("Enter the name video: ")
    time = input("Enter the time : ") 
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter Video no : "))
    name = input("Enter Updated Name : ")
    time = input("Enter Updated Time : ")
    videos[index-1] = {'name':name,'time':time}
    save_data_helper(videos)

def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter Video no : "))
    del videos[index-1]
    save_data_helper(videos)

def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager Application | Choose an option")
        print("1. List All The Video")
        print("2. Add Youtube Video")
        print("3. Update Youtube Video")
        print("4. Delete Youtube Video")
        print("5. Exit The App")

        choice = input("Enter Your Choice : ")

        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Envalid Choice")                

if __name__ == "__main__":
    main()

            