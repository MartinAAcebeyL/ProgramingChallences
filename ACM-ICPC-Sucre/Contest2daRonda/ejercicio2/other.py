def generate_subsequences(s, k):
    subsequences = []
    n = len(s)
    for i in range(0, n, k):
        subsegment = s[i:i+k]
        subsequence = ""
        distinct_chars = set()
        for char in subsegment:
            if char not in distinct_chars:
                subsequence += char
                distinct_chars.add(char)
        subsequences.append(subsequence)
    return subsequences

generate_subsequences()