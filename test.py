song = [input(), input(), input(), input(), input()] #User input song
choice = input("Do you want to add a new song? ")

if choice == "Yes":

    add_song = input("Song name: ")
    ranking = int(input("Ranking:"))
    song.insert(ranking,add_song)
    song.pop(5)
    print(f'1. {song[0]}') 
    print(f'2. {song[1]}')
    print(f'3. {song[2]}')
    print(f'4. {song[3]}')
    print(f'5. {song[4]}')

elif choice == "No":
    choice2= input("Do you want to remove a song?")
    if choice2 =="Yes":
        delete_song = input("Song name:")
        if delete_song in song:
            song.remove(delete_song)
        else: 
            print("This song does not exist in the list")
if len(song) == 4:
    print(f'1. {song[0]}') 
    print(f'2. {song[1]}')
    print(f'3. {song[2]}')
    print(f'4. {song[3]}')
if len(song)==5:  
    print(f'1. {song[0]}') 
    print(f'2. {song[1]}')
    print(f'3. {song[2]}')
    print(f'4. {song[3]}')
    print(f'5. {song[4]}')     