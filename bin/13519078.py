# TUGAS KECIL 2 STIMA
# JAMES CHANDRA / 13519078 / KELAS 02
# assumptions:
#     - penjadwalan akhir tidak melebihi 8 semester
#     - masukan berupa valid/directed acyclic graph


# DEFINISI FUNGSI

import os

def openFile(inputFile, outputDict):
# read file line by line, calls function to add read data as graph vertex
  with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), inputFile)) as f:
    for line in f:
      lineArray = line.strip(" .\n").split(", ")
      addVertex(lineArray, outputDict)

def addVertex(lineArray, outputDict):
# initializes key-value pair if first in one line, adds vertex if succeeding first class
  for i in range(len(lineArray)):
    if (i == 0):
      outputDict[lineArray[i]] = []
    else:
      outputDict[lineArray[0]].append(lineArray[i])

def takeClass(arrayResult, myDict):
# appends key to result array and sets dict key to empty / [None]
  for key in myDict:
    if (myDict[key] == []):
      arrayResult.append(key)
      myDict[key] = [None]

def deleteKeyValue(arrayResult, myDict):
# removes appropriate value of key (found in result array)
  for key in myDict:
    for keyDelete in arrayResult:
      if keyDelete in myDict[key]:
        myDict[key].remove(keyDelete)

def printConditional(arrayResult, myDict):
# prints according to dictionary/adjacency list condition
  if (list(myDict.values()).count([None]) == len(myDict)):
    print(*arrayResult, sep=", ", end=".\n")
  elif (len(arrayResult) == 0):
    return "error"
  else:
    print(*arrayResult, sep=", ")


# MAIN PROGRAM

# initialize dictionary
myDict = {}

# roman numbers substitution
romanNumbers = ["I     : ", "II    : ", "III   : ", "IV    : ", "V     : ", "VI    : ", "VII   : ", "VIII  : "]

# call openfile function
openFile("../test/test.txt", myDict)

# assumptions taken from qna: iterate for 8 semesters
for i in range(8):
  
  # determine if all values of each dictionary element is [none] or
  # all classes have been taken
  allNone = list(myDict.values()).count([None]) == len(myDict)
  
  if (not(allNone)):

    # initialize print array
    arrayResult = []

    print("Semester " + romanNumbers[i], end="")

    # call function to take class (append class to result array and set key's
    # value to [None] and call another function to remove the key's value from array)
    takeClass(arrayResult, myDict)
    deleteKeyValue(arrayResult, myDict)
    
    # print conditional, if returns error, then the graph is cyclic & invalid
    if (printConditional(arrayResult, myDict) == "error"):    
      print("\n\nInput error: graph given is cyclic and hence is invalid")
      break