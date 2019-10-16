import sourses
from ourclass import Record


def countingOperands(words, i):
    operand = Record(words[i], 0, 0)

    if i + 1 < len(words) and words[i + 1] == '=':
        operand.initialization += 1
    else:
        operand.usability += 1
    return operand


def deleteRepeatObj(listOfObj):
    i = 0
    while i < len(listOfObj):
        j = 0
        while j < len(listOfObj):
            if listOfObj[i].name == listOfObj[j].name and j != i:
                listOfObj[i].initialization += listOfObj[j].initialization
                listOfObj[i].usability += listOfObj[j].usability
                del listOfObj[j]
            j += 1
        i += 1
    return listOfObj


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
            if sourses.operators_of_language_multi.get(word, 0) != 0 or sourses.word_operators_of_language.get(word,
                                                                                                               0) != 0 or sourses.methods_of_language.get(
                    word, 0) != 0:
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
        k = 1
        list = ''
        flag = 0
        while k < len(sourses.operators_bracket) and flag == 0:
            list = str.split(sourses.operators_bracket.get(k))
            k += 1
            if len(list) != 1:
                j = 1
                flag = 1
                while j < len(list):
                    if k != 9:
                        list.insert(j, sourses.operators_bracket.get(k))
                        j += 2
        resultLine.extend(list)
        i += 1

    m1 = 0
    while m1 < len(resultLine):
        if resultLine[m1] == '':
            del resultLine[m1]
        m1 += 1
    return resultLine
