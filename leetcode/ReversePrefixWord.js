let reversePrefix = function (word, ch) {
    const reverseIndex = word.indexOf(ch);
    const reverseString = word.slice(0, reverseIndex+1).split('').reverse('').join('')
    return reverseString + word.slice(reverseIndex+1)
};


reversePrefix("abcdefd", "d")//dcbaefd
// reversePrefix("xyxzxe", "z")//dcbaefd
// reversePrefix("abcd", "z")//abcd
