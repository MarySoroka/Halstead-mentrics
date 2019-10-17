import sourses
from ourclass import Record
from ourclass import RecordOperators


#cretion of object list
def countingOperators(word):
    operators = RecordOperators(word, 1)
    return operators


#cretion of object list
def countingOperands(words, i):
    operand = Record(words[i], 0, 0)
    if i + 1 < len(words) and words[i + 1] == '=':
        operand.initialization += 1
    elif i < len(words) and words[i - 1] == '=':
        operand.usability += 1
    elif i < len(words) and words[i-1] == ".":
        operand.usability += 1
    elif i +1 < len(words) and words[i-1] == "." and words[i+1] == ".":
        operand.usability += 1
    elif len(words) == 1:
        operand.initialization += 1
    else:
        operand.usability += 1
    return operand

#delete one of the same object and define usebility
def deleteRepeatObj(listOfObj):
    i = 0
    while i < len(listOfObj):
        j = 0
        while j < len(listOfObj):
            if listOfObj[i].name == listOfObj[j].name and j != i:
                listOfObj[i].initialization = listOfObj[i].initialization + listOfObj[j].initialization
                listOfObj[i].usability = listOfObj[i].usability + listOfObj[j].usability
                del listOfObj[j]
            j += 1
        i += 1
    i = 0
    while i < len(listOfObj):
        if listOfObj[i].usability == 0:
            del listOfObj[i]
        i += 1
    return listOfObj

#finding operators and operands
def findingOperators(words):
    i = 0
    listOfOperators = []
    listOfOperands = []
    while i < len(words):
        word = words[i]
        if len(word) == 1:
            res = sourses.operators_of_language_single.get(word, 0)
            # если входит то оператор, а если нет, то явный операнд
            if res != 0:
                listOfOperators.append(countingOperators(word))  # добавляю в список операторов
            else:
                if not(len(words[i-1]) > 0  and  words[i-1] == "=" and words[i] >= "0" and words[i] <= "9"):
                     listOfOperands.append(countingOperands(words, i))  # отправляем в какую-то функцию вычислять операнды
        elif len(word) > 1:
            if sourses.operators_of_language_multi.get(word, 0) != 0 or sourses.word_operators_of_language.get(word, 0) != 0 or sourses.methods_of_language.get(word, 0) != 0:
                listOfOperators.append(countingOperators(word))
            else:
                if not (len(words[i - 1]) > 0 and words[i - 1] == "=" and (bool(word.isdigit))):
                    listOfOperands.append(countingOperands(words, i))
        i += 1
    return listOfOperators, listOfOperands

#define list of words without the of being operand and operator together
def findDot(line):
    i = 0
    resultLine = []
    while i < len(line):
        str = line[i]
        word = findBrackets(str)
        if len(word) != 1:
            k = len(word) -1
            del line[i]
            while k >= 0:
                str1 = word[k]
                line.insert(i, str1)
                k -= 1
        i += 1
    ind = 0
    while ind < len(line):
        if line[ind] == ',':
            del line[ind]
        ind += 1
    resultLine.extend(line)

    return resultLine

#finding simbols in words which is in operators_bracket vocabulary and addition space before and after them
def findBrackets(word):
    k = 0
    while k < len(word) and k + 1 != " ":
        i = 1
        while i <= len(sourses.operators_bracket):
            if k+1 < len(word) and word[k+1] != '='and word[k] == sourses.operators_bracket[i] or k == len(word)-1 and word[k] == sourses.operators_bracket[i]:
                if k != 0:
                    word = word[0:k] + " " + word[k] + " " + word[k + 1: len(word)]
                else:
                    word = word[k] + " " + word[1: len(word)]
                k += 2
            i += 1
        k += 1
    return word.split()
