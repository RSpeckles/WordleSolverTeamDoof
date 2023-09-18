import random

class Solver:
    def __init__(self):
        f = open("5LetterDict.txt", "r")
        self.possibleWords = []
        count = 0
        self.word = "arrow"
        while True:
                line = f.readline()
                if not line:
                    break
                self.possibleWords.append(line)
                self.possibleWords[-1] = self.possibleWords[-1][:5]
        
    def solve(self, letters):
        if not letters:
            return "arrow"
        else:
            i = 0
            print("WORD: ", self.word)
            while i < len(self.possibleWords):
                flag = False
                for j in range(len(letters)):
                    #print(j)
                    if (i >= len(self.possibleWords)):
                        break
                    elif letters[j] == "c" and self.possibleWords[i][j] != self.word[j]:
                        #print(self.word[j], " NOT IN PLACE FOR ", self.possibleWords[i])
                        self.possibleWords.pop(i)
                        flag = True
                        break
                    elif letters[j] == "p" and self.word[j] not in self.possibleWords[i]:
                        #print(self.word[j], " NOT IN ", self.possibleWords[i])
                        self.possibleWords.pop(i)
                        flag = True
                        break
                    elif letters[j] == "n" and self.word[j] in self.possibleWords[i]:
                        #print(self.word[j], " IS IN ", self.possibleWords[i])
                        self.possibleWords.pop(i)
                        flag = True
                        break
                if flag == False:
                    i += 1
                        

                # flag = False
                # for j in letters["Green"]:
                #     if self.possibleWords[i][j[1]] != j[0]:
                #         self.possibleWords.pop(i)
                #         flag = True
                #         continue
                # if flag == True:
                #     continue
                # for j in letters["Red"]:
                #     if j in self.possibleWords[i]:
                #         self.possibleWords.pop(i)
                #         flag = True
                #         continue
                # if flag == True:
                #     continue
                # for j in letters["Yellow"]:
                #     if j not in self.possibleWords[i]:
                #         self.possibleWords.pop(i)
                #         continue
            
            self.word = self.possibleWords[random.randint(0,len(self.possibleWords)-1)]
            return self.word
                
