from collections import Counter
from collections import OrderedDict as OD

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

def main():
    cipher_text = list("YNHPFAZNXPOHCQYAWYRNWRJSCFOFORYAWYRPFTXMCBXFCAWJRECWCFCAWXWJYAWQFNTYFCAWAEYAVPTFCWZQHQFRVQFOXFXJJNRQQQRYTNCFHYAWYRNWQFORJRQCZWAEYN" +
    "HPFAZNXPOCYQHQFRVQVTQFURUXQRJAWECNVEATWJXFCAWQXPPMCRJYNHPFAZNXPOHPNRQRWFQXNCZANATQXWJQHQFRVXFCYFNRXFVRWFAEEATWJXFCAWXMCQQTRQJRECWC" +
    "WZYNHPFAZNXPOCYFXQKQXWJQAMICWZWRSYNHPFAZNXPOCYPNAUMRVQTQCWZRLCQFCWZFAAMQFORRVPOXQCQCQAWFORYMXQQCECYXFCAWAEETWJXVRWFXMYAWYRPFQXWJJR" +
    "VAWQFNXFCWZFORERXQCUCMCFHAEQAMICWZQRIRNXMYRWFNXMYNHPFAZNXPOCYPNAUMRVQ")

    # Letter
    print "---------------- Letter Frequency in Percentages ----------------"
    print "-----------------------------------------------------------------"
    letter = find_ngrams(cipher_text, 1)
    letter = Counter(letter)
    letter = OD(sorted(letter.items(), key=lambda x: x[1]))
    
    for l in range(1, len(letter)):
        print str(letter.keys()[l]) + ": " + str(1.0 * letter.values()[l]/ len(cipher_text) * 100)

    # Digrams
    print "------------------------ Digrams Frequency ----------------------"
    print "-----------------------------------------------------------------"
    digrams = find_ngrams(cipher_text, 2)
    digrams = Counter(digrams)
    digrams = OD(sorted(digrams.items(), key=lambda x: x[1]))

    for l in range(len(digrams) - 20, len(digrams)):
        print str(digrams.keys()[l]) + ": " + str(digrams.values()[l])

    # Digrams
    print "------------------------ Trigrams Frequency ---------------------"
    print "-----------------------------------------------------------------"
    trigrams = find_ngrams(cipher_text, 3)
    trigrams = Counter(trigrams)
    trigrams = OD(sorted(trigrams.items(), key=lambda x: x[1]))

    for l in range(len(trigrams) - 20, len(trigrams)):
        print str(trigrams.keys()[l]) + ": " + str(trigrams.values()[l])
    

if __name__ == "__main__":
    main()
