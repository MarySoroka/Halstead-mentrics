import sourses


listOfOperators = []


def countingOperands(words,i):




def findingOperators(words):
    i = 0
    while i < len(words):
        word = words[i]
        if len(word) == 1:
            res = sourses.operators_of_language_single.get(word, 0)
            # если входит то оператор, а если нет, то явный операнд
            if res != 0:
                listOfOperators.append(words)#добавляю в список операторов
            else:
                countingOperands(words,i)#отправляем в какую-то функцию вычислять операнды
        elif len(word) > 1:
            if sourses.operators_of_language_multi.get(word, 0) != 0 or sourses.word_operators_of_language.get(word, 0) != 0 or sourses.methods_of_language.get(word, 0) != 0:
                listOfOperators.append(words)
            else:
                countingOperands(words,i)









