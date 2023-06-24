def merge_the_tools(string, k):
    subsequences = ""
    n = len(string)
    for i in range(0, n, k):
        subsegment = string[i:i+k]
        subsequence = ""
        distinct_chars = set()
        for char in subsegment:
            if char not in distinct_chars:
                subsequence += char
                distinct_chars.add(char)
        subsequences += subsequence+"\n"
    return subsequences


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
