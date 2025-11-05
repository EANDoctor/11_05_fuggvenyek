word1 = input("Kérem az első szót:")
word2 = input("Kérem a második szót:")
word3 = input("Kérem a harmadik szót:")

words = [word1, word2, word3]

words.append(word1)
words.append(word2)
words.append(word3)

def shortest_word_search(wordlist):
    shortest = len(wordlist[0])
    shortest_word = wordlist[0]
    for word in wordlist:

        if len(word) < shortest:
            shortest = len(word)
            shortest_word = word

    print(f"A legrövidebb szó: {shortest_word} karakterszáma. {shortest}")


szok = ["alma", "körte", "banán", "kiwi", "eper"]

# shortest_word_search(words)
shortest_word_search(szok)