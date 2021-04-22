import numpy
import nltk
from nltk.tokenize import word_tokenize

class BIOnBijan:
    def __init__(self , Seq):
        self.fileName = "‌Test_Bijan.txt"
        self.Seq = Seq
        self.listOfBigrams = []
        self.bigramCounts = {}
        self.unigramCounts = {}
        self.listOfProb = {}
        
    def createBigram(self , data):
        for i in range(len(data)):
            if i < len(data) - 1:

                self.listOfBigrams.append((data[i], data[i + 1]))

                if (data[i], data[i+1]) in self.bigramCounts:
                    self.bigramCounts[(data[i], data[i + 1])] += 1
                else:
                    self.bigramCounts[(data[i], data[i + 1])] = 1

            if data[i] in self.unigramCounts:
                self.unigramCounts[data[i]] += 1
            else:
                self.unigramCounts[data[i]] = 1


        return self.listOfBigrams, self.unigramCounts, self.bigramCounts
    
    
    def addOneSmothing(self):
        
        self.listOfBigrams , self.unigramCounts , self.bigramCounts = self.createBigram(self.Seq)
    
        for bigram in self.listOfBigrams:
            self.listOfProb[bigram] = (self.bigramCounts.get(bigram) + 1)/(self.unigramCounts.get(bigram[0]) + len(self.unigramCounts))


        return self.listOfProb
    
    def Bigram_Score(self):
        
        bigramAddOne = self.addOneSmothing()
        
        lenn = len(self.Seq)
        sent1 = [line.rstrip('\n') for line in open(self.fileName,encoding="utf-8")]
        seq1 = []
        bigSeq = []
        for i in range(len(sent1)) :
            for j in word_tokenize(sent1[i]):
                seq1.append(j)
        for i in range(len(seq1)):
                if i < len(seq1) - 1:
                    bigSeq.append((seq1[i], seq1[i + 1]))


        probTest = (self.unigramCounts[seq1[0]])/(lenn)

        for i in range(len(bigSeq)):
            if bigSeq[i] in self.listOfBigrams:
                probTest = probTest*bigramAddOne[bigSeq[i]]
            elif bigSeq[i][0] in seq:
                probTest = probTest*(1/(self.unigramCounts[bigSeq[i][0]] + len(self.unigramCounts)))
            else :
                probTest = probTest*(1/(len(self.unigramCounts)))

        return probTest
    
     

def Load_Bijan_corpus():
    sent = []
    filename = "Bijan_Corpus.txt"

    for line in open(filename,'r', encoding="utf-8"):   
        sent.append(line)

    seq = []        
    for i in range(len(sent)):
        sent[i] = sent[i].replace("\n","")
        seq.append(sent[i].split(" ")[0])
        
    return seq
    


if __name__ == "__main__":
    
    seq = Load_Bijan_corpus()
    bigram = BIOnBijan(seq)
    Prob = bigram.Bigram_Score()
    
    print(Prob)
    
    
        
    