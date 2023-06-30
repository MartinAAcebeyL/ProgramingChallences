#include <iostream>

const int MAX_SINGERS = 1000001; // Valor máximo para el número de cantantes

int main()
{
    int numSongs;
    std::cin >> numSongs;

    int singerCount[MAX_SINGERS] = {0}; // Array para contar el número de canciones por cantante

    for (int i = 0; i < numSongs; i++)
    {
        int singer;
        std::cin >> singer;
        singerCount[singer]++;
    }

    int maxCount = 0;
    int numFavouriteSingers = 0;

    for (int i = 0; i < MAX_SINGERS; i++)
    {
        if (singerCount[i] > maxCount)
        {
            maxCount = singerCount[i];
            numFavouriteSingers = 1;
        }
        else if (singerCount[i] == maxCount)
        {
            numFavouriteSingers++;
        }
    }

    std::cout << numFavouriteSingers << std::endl;

    return 0;
}