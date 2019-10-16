import sourses
from ourclass import Record


def countingOperands(words, i):
    operand = Record(words[i], 1, 0)
    operand.name = words[i]
    if i+1<len(words) and words[i + 1] == '=':
        operand.initialization += 1
    else:
        operand.usability +=1
    return operand


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
                listOfOperators.append(word)  # добавляю в список операторов
            else:
                listOfOperands.append(countingOperands(words, i))  # отправляем в какую-то функцию вычислять операнды
        elif len(word) > 1:
            if sourses.operators_of_language_multi.get(word, 0) != 0 or sourses.word_operators_of_language.get(word, 0) != 0 or sourses.methods_of_language.get(word, 0) != 0:
                listOfOperators.append(word)
            else:
                listOfOperands.append(countingOperands(words, i))
        i += 1
    return listOfOperators, listOfOperands

def findDot(line):
    i = 0
    resultLine = []
    while i < len(line):
        str = line[i]
        list = str.split('.')
        if len(list) != 1:
            j = 1
            while j < len(list):
                list.insert(j, '.')
                j += 2
        resultLine.extend(list)
        i += 1
    return resultLine



