import pylab

# You may have to change this path
WORDLIST_FILENAME = "C:/Wei Cui/Edx8.00x/6.00.2x Files/L4P5/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowelslist=['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u',]
    TracknumL=[];
    Pcount=0;
    for w in wordList:
        #some word in WordList;
        Vcount=0.0;
        for L in w:
            #Vcount=0;
            if L in vowelslist:
                Vcount=Vcount+1; #adds a vowel count
        #counted number of vowels in Word;
        TracknumL.append(Vcount/len(w));
        if Vcount/len(w)<=0.5:
            Pcount=Pcount+1;
    #now we have a list of number of vowels in Wordlist.
    pylab.hist(TracknumL, numBins);
    print len(TracknumL)
    pylab.show();
    print Pcount;

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
