def choose_favorite_singer(list_of_songs: list[int]) -> int:
    dict_of_songs = {}

    for song in list_of_songs:
        if song not in dict_of_songs:
            dict_of_songs[song] = 1
        else:
            dict_of_songs[song] += 1
    return max(dict_of_songs.values())


singers = input()
list_of_music = list(map(int, input().split()))
choose_favorite_singer(list_of_music)
print(choose_favorite_singer(list_of_music))
