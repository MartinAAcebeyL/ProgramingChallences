def minion_game(string):
    n = len(string)
    vowels = 'AEIOU'
    kevin_score = sum(n-i for i in range(n) if string[i] in vowels)
    stuart_score = n*(n+1)//2 - kevin_score
    
    if kevin_score == stuart_score:
        return "Draw"
    elif kevin_score > stuart_score:
        return "Kevin {}".format(kevin_score)
    else:
        return "Stuart {}".format(stuart_score)


if __name__ == '__main__':
    s = input()
    print(minion_game(s))