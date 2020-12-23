import numpy as np

import string

import re


columnsRefList = []


"""Programming assignment for NORITEX.com software engineering position.

Su tarea es implementar la función evaluar a continuación para la especificación
proporcionado en la cadena de documentación. Si la documentación está en alguna
muy ambiguo, envíe un correo electrónico a Nessim Btesh para obtener una aclaración.
Si cree que las funciones auxiliares auxiliares serían útiles, no dude en
escríbelos Puede cambiar cualquier cosa en este archivo, excepto que no está permitido
para alterar el nombre o la firma de la función de evaluación ().

Aunque le proporcionamos algunos casos de prueba, no asuma que estos cubren
todos los casos de esquina, y podemos usar un conjunto diferente de entradas para validar su
solución. Analizaremos su solución tanto para la corrección como para
estilo.

----------------------------------------------

Your task is to implement the function evaluate below to the specification
provided in the documentation string. If the documentation is in any
way ambiguous, please email Nessim Btesh for clarification.
If you feel that auxiliary helper functions would be helpful, feel free to
write them. You may change anything in this file except you are not permitted
to alter the name or function signature of evaluate().

Although we provide you with some test cases, do not assume that these cover
all corner cases, and we may use a different set of inputs to validate your
solution. We will be looking at your solution both for correctness and for
style.

Best of luck!
"""

# =============================================================================
#
# Implement this function
#
# =============================================================================


def evaluate(m):
    """Evaluate all of the values in the spreadsheet.

    Given a matrix m of "arbitrary" size, evalute all of the cells in the
    spreadsheet and return the matrix with everything computed. We will assume
    that columns are denoted using a letter while rows are denoted by numbers.
    E.g "A1" is equivalent to ``m[0][0]`` while "C23" is ``m[22][2]``. 

    As such, here are some examples, assume we have the matrix:

        1   2
        3   4

    This, obviously, should just return the same matrix. Now, let's add some
    functions:

        1   =A1
        2   =A2 + 1

    This should evalute to:

        1   1
        2   3

    Now, let's take this one step further and add in a second level of
    reference:

        1           =A1 + 1
        =B1 + 1     =A2 + B1

    This should evalute to:

        1   2
        3   5

    If you are given a reference to a cell that has not been defined, you
    should raise a ReferenceError. For example, this should not work:

        1           =A5 + 2
        =B1 + 1     =A2 + 1

    If you find circular references, you should raise a ValueError. For example:

        =B1 + 1     =A1 + 1

    You can assume the following:
        - All "functions" will have = as the first character
        - The only operations that will be peformed are +, -, *, /
        - All input numbers will be integers (you may have some floats as a 
          result of division, however)
        - Each "function" will only be a direct reference or binary operation.
          I.e. It'll either be something like "=A1" or "=A1 + 1" but not
          "=A1 + 1 + 2"
        - Spaces in "functions" are meaningless. I.e. "=A1 + 1" is the same as
          "=A1+1" or "= A1  +   1". However, a negative sign must appear 
          right in front of the number. E.g. "=A1 +   -1" is valid, but
          "=A1 +  -  1" is not
        - There will be no column that goes past "Z" and capitalization in
          column names is ignored. I.e. "A1" is the same as "a1".

    :param m: The matrix to be evaluated. Each of the entries in the matrix
              will either be numbers or strings.
    :returns: A matrix of the same dimensions as :attr:`m` with all of the
              functions evaluated. All of the entries in this returned matrix
              should be numeric and not strings.
    :raises:
        :ValueError: If there is a problem parsing any of the input values
        :ReferenceError: If a cell is referenced that has not been defined
        :ValueError: If there is a circular reference
        :ZeroDivisionError: If there is a divide by zero

    --------------SPANISH ---------------------

    Evaluar todos los valores en la hoja de cálculo.

        Dada una matriz m de tamaño "arbitrario", evalúe todas las celdas en el
        hoja de cálculo y devolver la matriz con todo lo calculado. Asumiremos
        que las columnas se denotan con una letra, mientras que las filas se denotan con números.
        Por ejemplo, "A1" es equivalente a `` m [0] [0] `` mientras que "C23" es `` m [22] [2] ``.

        Como tal, aquí hay algunos ejemplos, supongamos que tenemos la matriz:

                1 2
                3 4

        Esto, obviamente, debería devolver la misma matriz. Ahora, agreguemos algunos
        funciones:

                1 = A1
                2 = A2 + 1

        Esto debería evaluar a:

                1 1
                2 3

        Ahora, vamos un paso más allá y agreguemos un segundo nivel de
        referencia:

                1 = A1 + 1
                = B1 + 1 = A2 + B1

        Esto debería evaluar a:

                1 2
                3 5

        Si se le da una referencia a una celda que no se ha definido, usted
        debería generar un ReferenceError. Por ejemplo, esto no debería funcionar:

                1 = A5 + 2
                = B1 + 1 = A2 + 1

        Si encuentra referencias circulares, debe generar un ValueError. Por ejemplo:

                = B1 + 1 = A1 + 1

        Puede asumir lo siguiente:
                - Todas las "funciones" tendrán = como primer carácter
                - Las únicas operaciones que se realizarán son +, -, *, /
                - Todos los números de entrada serán enteros (puede tener algunos flotantes como
                    resultado de la división, sin embargo)
                - Cada "función" solo será una referencia directa o una operación binaria.
                    Es decir. Será algo así como "= A1" o "= A1 + 1" pero no
                    "= A1 + 1 + 2"
                - Los espacios en "funciones" no tienen sentido. Es decir. "= A1 + 1" es lo mismo que
                    "= A1 + 1" o "= A1 + 1". Sin embargo, debe aparecer un signo negativo
                    justo en frente del número. P.ej. "= A1 + -1" es válido, pero
                    "= A1 + - 1" no es
                - No habrá columna que pase la "Z" y las mayúsculas en
                    los nombres de columna se ignoran. Es decir. "A1" es lo mismo que "a1".

        : param m: La matriz a evaluar. Cada una de las entradas en la matriz
                            serán números o cadenas.
        : devuelve: Una matriz de las mismas dimensiones que: attr: `m` con todos los
                            funciones evaluadas. Todas las entradas en esta matriz devuelta
                            debe ser numérico y no cadenas.
        : plantea:
                : ValueError: si hay un problema al analizar cualquiera de los valores de entrada
                : ReferenceError: si se hace referencia a una celda que no se ha definido
                : ValueError: si hay una referencia circular
                : ZeroDivisionError: si hay una división entre cero
        "" "
    """
    # pass

    #print('Matrix:', m)

    # There will be no column that goes past "Z"
    matrixColumns = len(m[0])
    # print(matrixColumns)
    if matrixColumns > 27:
        raise ValueError('Columns length more than Alphabet')

    # If all elements in matrix are numbers:
    check = False
    checkList = []
    negativeSign = ''

    for c in m:
        for item in c:

            # print(item)

            if item == "" or item == None:
                raise ValueError('Errors in input')

            # if item is a single string number
            if type(item) == str and len(item) == 1:
                #print('string:', item)
                #print('string length:', len(item))

                # print(m.index(c))
                # print(m[m.index(c)][c.index(item)])

                # convert to integer
                m[m.index(c)][c.index(item)] = int(
                    m[m.index(c)][c.index(item)])

                #print('m integers:', m)

            # if letter is uppercase convert to lowercase
            if type(item) == str and len(item) > 1:
                #print('True string:', item)

                # print(item.lower())
                # print(m[m.index(c)][c.index(item)])
                m[m.index(c)][c.index(item)] = item.lower()

                #print('m lowercase:', m)

                # negative sign must appear right in front of the number
                val = item[1:]
                r = re.compile("(\w).*?(\d+).*?([-+\/*]).*?(- ?).*?(\d+)")
                correct = r.match(val)
                if correct:
                    #print('Group 4', correct.group(4))
                    negativeSign = correct.group(4)

                # else:
                #     print("it is in front")

                #print('Negative Sign:', negativeSign)
                if (' ' in negativeSign) == True:
                    raise ValueError(
                        "negative sign must appear right in front of the number")

            checkList.append(item)
            #print('CheckList:', checkList)

    if all(isinstance(x, str) for x in checkList):
        #print('all are strings')
        raise ValueError('circular dependencies')

    if all(isinstance(x, int) for x in checkList):
        check = True

    if check == True:
        #print('They are all numbers', m)
        return m

    else:

        #print('There is no operation here')
        # print('Not all are numbers') #else: do the following

        # Get Alphabet letters:
        alphabet_string = string.ascii_lowercase
        alphabet_list = list(alphabet_string)
        # print(alphabet_list)

        # Extract columns of matrix:
        columns = list(zip(*m))
        #print('List of columns:', columns)

        # Assign Alphabet Letters to Matrix columns:
        columnsRefList = dict(zip(alphabet_list, columns))
        #print('Referece Dict:', columnsRefList)

        # print('')

        for col in m:
            for item in col:
                # print(item)

                # call function that checks value of item in the column with (regex)

                column = ''
                number = 0
                symbol = ''
                secondNumber = 0

                # Regex Option (more than just 1 number: =1-1):
                if type(item) == str and not item.lower().islower():

                    #print(item, 'Its only numbers')

                    pos_col = m.index(col)
                    pos_item = col.index(item)

                    val = item[1:]
                    r = re.compile("(\d+).*?([-+\/*]).*?(-?\d+)")
                    correct = r.match(val)
                    if correct:
                        # print(correct.group(1))
                        # print(correct.group(2))
                        # print(correct.group(3))

                        number = correct.group(1)
                        symbol = correct.group(2)
                        secondNumber = correct.group(3)

                        # Positions
                        #print('Matrix value position to change:', pos_item)
                        #print('Whats going to be changed:', m[pos_col][pos_item])

                        # Calculation
                        calc = eval(f'{number}{symbol}{secondNumber}')
                        calc = float(calc)
                        #print(f'Referece (Change To): {calc}')

                        # check if a float value is a whole number
                        if (calc).is_integer():
                            calc = int(calc)

                        # make the change:
                        m[pos_col][pos_item] = calc

                        # print('')

                    # else:
                    #     print("no match")

                # Regex Option (single string Example: a1):
                if type(item) == str and len(item) < 4:
                    #print('yes single string', item)

                    # print(col)
                    #print('position column:', m.index(col))
                    #print('Position item:', col.index(item))

                    pos_col = m.index(col)
                    pos_item = col.index(item)

                    # print(type(pos))
                    # checkRegex(item)

                    val = item[1:]
                    r = re.compile("(\w).*?(\d+)")
                    correct = r.match(val)
                    if correct:
                        # print(correct.group(1))
                        # print(correct.group(2))

                        column = correct.group(1)
                        number = correct.group(2)

                    # else:
                    #     print("no match")

                # print(column)
                # print(number)

                    # If value of column is in the Dictionary
                    if column in columnsRefList:
                        #print(f'yes, col {column} is:', columnsRefList[column])

                        # get the number after letter (regex):

                        number = int(number)
                        # print(number)

                        # assign current item row to row position of dict
                        #print(f'row {number} is: {columnsRefList[column][number-1]}')
                        #print('item:' ,item)

                        # avoid infinite recursion
                        if type(columnsRefList[column][number-1]) == str:
                            #print('The value will be a string')
                            continue

                        #print('index column:', list(columnsRefList).index(column))
                        # print('value (1):', columnsRefList[column][number-1])  # expected 1
                        #print('value (1):', columnsRefList[column].index(columnsRefList[column][number-1]))

                        #matrix_col = int(list(columnsRefList).index(column))
                        # print(matrix_col)

                        #matrix_row = int(columnsRefList[column].index(columnsRefList[column][number-1]))
                        # print(matrix_row)

                        #print('Dynamic position:', m[list(columnsRefList).index(column)][columnsRefList[column].index(columnsRefList[column][number-1])])
                        #print('Matrix value position to change:', pos_item)

                        #print('Whats going to be changed:', m[pos_col][pos_item])
                        m[pos_col][pos_item] = columnsRefList[column][number-1]

                        #print('Referece (Change To):', columnsRefList[column][number-1])
                        # print('')

                    else:
                        #print(column, 'does not exist')
                        raise ReferenceError('referencing cells out of range')

                if type(item) == str and len(item) > 4 and item[1:].startswith('-') and not item[2:][0].isdigit():

                    #print('starts with negative')

                    # print('Row:',col)
                    #print('position column:', m.index(col))
                    #print('Position item:', col.index(item))

                    pos_col = m.index(col)
                    pos_item = col.index(item)

                    # Regex
                    val = item[1:]
                    r = re.compile(
                        "(-?\w).*?(-?\d+).*?([-+\/*]).*?(\w+|-?\d.*)")
                    correct = r.match(val)

                    # if not correct:
                    #     print('not correct')
                    #raise ValueError('malformed formulas')

                    # malformed formulas
                    if correct:
                        # print(correct.group(1))
                        # print(correct.group(2))
                        # print(correct.group(3))
                        # print(correct.group(4))

                        # If after symbol is a number
                        if not correct.group(4).lower().islower():

                            #print('correct after symbol is a number')

                            negative = correct.group(1).strip(
                                '1234567890abcdefghijklmnopqrstuvwxyz')
                            column = correct.group(1).lstrip('-')
                            number = correct.group(2)
                            symbol = correct.group(3)
                            secondNumber = correct.group(4)

                            # print('Negative:', negative)
                            # print('Column:', column)
                            # print('Number Row:', number)
                            # print('Symbol:', symbol)
                            # print('Second Number:', secondNumber)

                            # print('')

                            if not int(number) >= 0:
                                # print('out')
                                raise ValueError('negative numbers')

                            if column in columnsRefList:
                                #print(f'yes, col {column} is:', columnsRefList[column])

                                # get the number after letter (regex):
                                number = int(number)
                                secondNumber = int(secondNumber)

                                # rase valueError out of range of row
                                if number > len(m):
                                    raise ReferenceError(
                                        'referencing cells out of range')

                                # assign current item row to row position of dict
                                #print(f'row {number} is: {columnsRefList[column][number-1]}')
                                #print('item:' ,item)

                                # avoid infinite recursion
                                if type(columnsRefList[column][number-1]) == str:
                                    #print('The value will be a string')
                                    continue

                                # print('Matrix value position to change:', pos_item)
                                # print('Whats going to be changed:', m[pos_col][pos_item])

                                # Calculation
                                calc = eval(
                                    negative+str(columnsRefList[column][number-1])+symbol+str(secondNumber))
                                calc = float(calc)

                                #print(f'Referece (Change To): {calc}')

                                # check if a float value is a whole number
                                if (calc).is_integer():
                                    calc = int(calc)

                                # make the change:
                                m[pos_col][pos_item] = calc

                                # print('')

                        # if after symbol is not a number
                        elif correct.group(4).lower().islower():

                            #print('correct after symbol its a letter')

                            # Regex 2
                            val = item[1:]
                            r = re.compile(
                                "(-?\w).*?(-?\d+).*?([-+\/*]).*?(\w+|-?\d.*)")
                            correct = r.match(val)

                            # if correct:
                            #     print(correct.group(1))
                            #     print(correct.group(2))
                            #     print(correct.group(3))
                            #     print(correct.group(4))

                            # Assign values
                            negative = correct.group(1).strip(
                                '1234567890abcdefghijklmnopqrstuvwxyz')
                            column = correct.group(1).strip('-1234567890')
                            number = correct.group(2)
                            symbol = correct.group(3)
                            secondLetter = correct.group(
                                4).strip('-1234567890')
                            secondNumber = correct.group(4).strip(
                                '-abcdefghijklmnopqrstuvwxyz')

                            # print('Negative', negative)
                            # print('Column:', column)
                            # print('Number Row:', number)
                            # print('Symbol:', symbol)
                            # print('Second Letter:', secondLetter)
                            # print('Second Number:', secondNumber)

                            # print('')

                            if column in columnsRefList:
                                #print(f'yes, col {column} is:', columnsRefList[column])
                                #print(f'yes, col {secondLetter} is:', columnsRefList[secondLetter])

                                # get the number after letter (regex):
                                number = int(number)
                                secondNumber = int(secondNumber)

                                # assign current item row to row position of dict
                                # print(f'row {number} is: {columnsRefList[column][number-1]}')
                                # print(f'row {secondNumber} is: {columnsRefList[secondLetter][secondNumber-1]}')
                                # print('item:' ,item)

                                if type(columnsRefList[column][number-1]) == str:
                                    #print('The value will be a string')
                                    continue

                                if type(columnsRefList[secondLetter][secondNumber-1]) == str:
                                    #print('The value will be a string')
                                    continue

                                # print('Matrix value position to change:', pos_item)
                                # print('Whats going to be changed:', m[pos_col][pos_item])

                                # Calculation
                                calc = eval(negative+str(columnsRefList[column][number-1])+symbol+str(
                                    columnsRefList[secondLetter][secondNumber-1]))
                                calc = float(calc)

                                #print(f'Referece (Change To): {calc}')

                                # check if a float value is a whole number
                                if (calc).is_integer():
                                    calc = int(calc)

                                # make the change:
                                m[pos_col][pos_item] = calc

                                # print('')

                # Regex Option (calculate with operator. Example: a2+1 or a2+b1):
                # maybe add that includes strings
                elif type(item) == str and len(item) > 4 and not item[1:].lstrip("-")[0].isdigit():

                    # print('yes make calculation of', item)

                    # print('Row:',col)
                    # print('position column:', m.index(col))
                    # print('Position item:', col.index(item))

                    pos_col = m.index(col)
                    pos_item = col.index(item)

                    # Regex
                    val = item[1:]
                    r = re.compile(
                        "(-?\w).*?(-?\d+).*?([-+\/*]).*?(\w+|-?\d.*)")
                    correct = r.match(val)

                    if not correct:
                        #print('not correct')
                        raise ValueError('malformed formulas')

                    # malformed formulas
                    # print(val)
                    fullmatch = re.match(
                        "(-?\w).*?(-?\d+).*?([-+\/*]).*?(\w+|-?\d.*)", val)
                    start, stop = fullmatch.span()
                    if stop-start == len(val):
                        #print("The entire string matched")
                        pass
                    else:
                        #print('did not matched entire string')
                        raise ValueError('malformed formulas')

                    if correct:
                        # print(correct.group(1))
                        # print(correct.group(2))
                        # print(correct.group(3))
                        # print(correct.group(4))

                        # If after symbol is a number
                        if not correct.group(4).lower().islower():

                            #print('correct after symbol is a number')

                            column = correct.group(1)
                            number = correct.group(2)
                            symbol = correct.group(3)
                            secondNumber = correct.group(4)

                            # print('Column:', column)
                            # print('Number Row:', number)
                            # print('Symbol:', symbol)
                            # print('Second Number:', secondNumber)

                            # print('')

                            if not int(number) >= 0:
                                # print('out')
                                raise ValueError('negative numbers')

                            if column in columnsRefList:
                                #print(f'yes, col {column} is:', columnsRefList[column])

                                # get the number after letter (regex):
                                number = int(number)
                                secondNumber = int(secondNumber)

                                # rase valueError out of range of fow
                                if number > len(m):
                                    raise ReferenceError(
                                        'referencing cells out of range')

                                # assign current item row to row position of dict
                                # print(f'row {number} is: {columnsRefList[column][number-1]}')
                                # print('item:' ,item)

                                # avoid infinite recursion
                                if type(columnsRefList[column][number-1]) == str:
                                    #print('The value will be a string')
                                    continue

                                # print('Matrix value position to change:', pos_item)
                                # print('Whats going to be changed:', m[pos_col][pos_item])

                                # Calculation
                                calc = eval(
                                    str(columnsRefList[column][number-1])+symbol+str(secondNumber))
                                calc = float(calc)

                                #print(f'Referece (Change To): {calc}')

                                # check if a float value is a whole number
                                if (calc).is_integer():
                                    calc = int(calc)

                                # make the change:
                                m[pos_col][pos_item] = calc

                                # print('')

                        # if after symbol is not a number
                        elif correct.group(4).lower().islower():

                            #print('correct after symbol its a letter')

                            # Regex 2
                            val = item[1:]
                            r = re.compile(
                                "(\w).*?(\d+).*?([-+\/*]).*?(\w).*?(-?\d+)")
                            correct = r.match(val)

                            # if correct:
                            #     print(correct.group(1))
                            #     print(correct.group(2))
                            #     print(correct.group(3))
                            #     print(correct.group(4))
                            #     print(correct.group(5))

                            # Assign values
                            column = correct.group(1)
                            number = correct.group(2)
                            symbol = correct.group(3)
                            secondLetter = correct.group(4)
                            secondNumber = correct.group(5)

                            # print('Column:', column)
                            # print('Number Row:', number)
                            # print('Symbol:', symbol)
                            # print('Second Letter:', secondLetter)
                            # print('Second Number:', secondNumber)

                            # print('')

                            if column in columnsRefList:
                                # print(f'yes, col {column} is:', columnsRefList[column])
                                # print(f'yes, col {secondLetter} is:', columnsRefList[secondLetter])

                                # get the number after letter (regex):
                                number = int(number)
                                secondNumber = int(secondNumber)

                                # assign current item row to row position of dict
                                # print(f'row {number} is: {columnsRefList[column][number-1]}')
                                # print(f'row {secondNumber} is: {columnsRefList[secondLetter][secondNumber-1]}')
                                # print('item:' ,item)

                                if type(columnsRefList[column][number-1]) == str:
                                    #print('The value will be a string')
                                    continue

                                if type(columnsRefList[secondLetter][secondNumber-1]) == str:
                                    #print('The value will be a string')
                                    continue

                                # print('Matrix value position to change:', pos_item)
                                # print('Whats going to be changed:', m[pos_col][pos_item])

                                # Calculation
                                calc = eval(str(columnsRefList[column][number-1])+symbol+str(
                                    columnsRefList[secondLetter][secondNumber-1]))
                                calc = float(calc)

                                #print(f'Referece (Change To): {calc}')

                                # check if a float value is a whole number
                                if (calc).is_integer():
                                    calc = int(calc)

                                # make the change:
                                m[pos_col][pos_item] = calc

                                # print('')

                    else:
                        #print("no match")
                        raise ValueError('malformed formulas')

                    # print('')

                # Regex Option (calculation starting with number):
                elif type(item) == str and len(item) > 4 and item[1:].lstrip("-")[0].isdigit():

                    # print('item startswith number')

                    # print('Row:',col)
                    # print('position column:', m.index(col))
                    # print('Position item:', col.index(item))

                    pos_col = m.index(col)
                    pos_item = col.index(item)

                    # Regex
                    val = item[1:]
                    r = re.compile("(-?\d+).*?([-+\/*]).*?(\w+|-?\d.*)")
                    correct = r.match(val)

                    if not correct:
                        #print('not correct')
                        raise ValueError('malformed formulas')

                    # malformed formulas
                    # print(val)
                    fullmatch = re.match(
                        "(-?\d+).*?([-+\/*]).*?(\w+|-?\d.*)", val)
                    start, stop = fullmatch.span()
                    if stop-start == len(val):
                        #print("The entire string matched")
                        pass
                    else:
                        #print('did not matched entire string')
                        raise ValueError('malformed formulas')

                    if correct:
                        # print(correct.group(1))
                        # print(correct.group(2))
                        # print(correct.group(3))

                        # If after symbol is a number
                        if not correct.group(3).lower().islower():

                            #print('correct after symbol is a number')

                            number = correct.group(1)
                            symbol = correct.group(2)
                            secondNumber = correct.group(3)

                            # print('Matrix value position to change:', pos_item)
                            # print('Whats going to be changed:', m[pos_col][pos_item])

                            # Calculation
                            calc = eval(f'{number}{symbol}{secondNumber}')
                            calc = float(calc)

                            #print(f'Referece (Change To): {calc}')

                            # check if a float value is a whole number
                            if (calc).is_integer():
                                calc = int(calc)

                            # make the change:
                            m[pos_col][pos_item] = calc

                            # print('')

                        elif correct.group(3).lower().islower():

                            #print('correct after symbol its a letter')

                            # Assign values
                            firstNumber = correct.group(1)
                            symbol = correct.group(2)
                            column = correct.group(3).strip('1234567890')
                            number = correct.group(3).lstrip(
                                'abcdefghilmnopqrstuvwxyz')

                            # print('firstNumber:', firstNumber)
                            # print('Symbol:', symbol)
                            # print('column:', column)
                            # print('Number Row:', number)

                            if column in columnsRefList:
                                #print(f'yes, col {column} is:', columnsRefList[column])
                                pass

                            # get the number after letter (regex):
                            number = int(number)

                            # assign current item row to row position of dict
                            #print(f'row {number} is: {columnsRefList[column][number-1]}')

                            # avoid infinite recursion
                            if type(columnsRefList[column][number-1]) == str:
                                #print('The value will be a string')
                                continue

                            # print('Matrix value position to change:', pos_item)
                            # print('Whats going to be changed:', m[pos_col][pos_item])

                            # Calculation
                            calc = eval(str(firstNumber)+symbol +
                                        str(columnsRefList[column][number-1]))
                            calc = float(calc)
                            #print(f'Referece (Change To): {calc}')

                            # check if a float value is a whole number
                            if (calc).is_integer():
                                calc = int(calc)

                            # make the change:
                            m[pos_col][pos_item] = calc

                            # print('')

                    else:
                        #print("no match")
                        raise ValueError('malformed formulas')

    # Check if all elements in matrix have been calculated to number if not do recursion
    check2 = False
    checkList2 = []

    for r in m:
        for i in r:
            checkList2.append(i)

    #print('CheckList2:', checkList2)

    if all(isinstance(x, (int, float)) for x in checkList2):
        check2 = True

    if check2 == True:
        #print('Output', type(m))
        return m
    else:
        #print('There are still strings left')
        return evaluate(m)  # recursion


# =============================================================================
#
# Some example inputs and solutions to test against
#
# =============================================================================
testcase = []
solution = []

# Case: simple spreadsheet with strings and ints
testcase.append(
    [
        [1, "2"],
        ["3", 4]
    ]
)
solution.append(
    [
        [1, 2],
        [3, 4]
    ]
)

# Case: simple (non-recursive) formulas
testcase.append(
    [
        [1, "=A1+1"],
        [3, "=A2+1"]
    ]
)
solution.append(
    [
        [1, 2],
        [3, 4]
    ]
)

testcase.append(
    [
        [1, "=1-1"],
        [3, "=A2+1"]
    ]
)
solution.append(
    [
        [1, 0],
        [3, 4]
    ]
)


# Case: formulas referencing two cells
testcase.append(
    [
        [1,     "=A1+1", "=A1 + B1"],
        ["=B1", "3",     "=C1 + B2"]
    ]
)
solution.append(
    [
        [1, 2, 3],
        [2, 3, 6]
    ]
)

# Cases: formula referencing cells out of range
testcase.append(
    [
        [1,         "=A5 + 2"],
        ["=B1 + 1", "=A2 + 1"]
    ]
)
solution.append(ReferenceError)

testcase.append([[1, "=C1"]])
solution.append(ReferenceError)

# Case: circular dependencies
testcase.append(
    [
        ["=B1 + 1", "=A1 + 1"]
    ]
)
solution.append(ValueError)

# Case: highly recursive spreadsheet, all operations represented
testcase.append(
    [
        ["=C1+5", "=A3/2", "=c2-1"],
        ["=b3+7",       1, "=B1*4"],
        ["=B2+5", "=a1/5", "=A2-2"]
    ]
)
solution.append(
    [
        [16,   3,   11],
        [10.2, 1,   12],
        [6,   3.2,  8.2]
    ]
)

# Cases: malformed formulas
testcase.append([[1, "=A1 +"]])
solution.append(ValueError)

testcase.append([[1, "=A1+5+6+7"]])
solution.append(ValueError)

testcase.append([[1, "=A1 $ A1"]])
solution.append(ValueError)

# Case: division by zero
testcase.append([[1, "=A1 - 1", "=A1 / B1"]])
solution.append(ZeroDivisionError)

# Case: negative numbers
testcase.append([[1, "=A1 * -1"]])
solution.append([[1, -1]])

testcase.append([[-1, "=A1 * -5"]])
solution.append([[-1, 5]])

testcase.append([[1, "=-2 + a1"]])
solution.append([[1, -1]])

testcase.append([[1, "=A1 + -5"]])
solution.append([[1, -4]])

testcase.append([[1, "=A-1 + 1"]])
solution.append(ValueError)

testcase.append([[1, "=-A1 + 1"]])
solution.append([[1, 0]])

# Case: Errors in input
testcase.append([[-1, "=A1 + - 5"]])
solution.append(ValueError)

testcase.append([[""]])
solution.append(ValueError)

testcase.append([[None]])
solution.append(ValueError)

testcase.append([[None, "=A1"]])
solution.append(ValueError)

testcase.append([["A1"]])
solution.append(ValueError)

# Case There will be no column that goes past "Z":
testcase.append(np.zeros((5, 28)))
solution.append(ValueError)


def validate(proposed, actual):
    """Check if the proposed solution is the same as the actual solution.

    Feel free to modify this function as we will be testing your code with
    our copy of this function.

    :param proposed: The proposed solution
    :param actual: The actual solution
    :return: True if they are the same. Else, return False.
    """
    if proposed is None:
        print("Oops! Looks like your proposed result is None.")
        return False
    proposed_items = [item for sublist in proposed for item in sublist]
    actual_items = [item for sublist in actual for item in sublist]
    if len(proposed_items) != len(actual_items):
        print("Oops! There don't seem to be the same number of elements.")
        return False
    if proposed_items != actual_items:
        print("Oops! Looks like your proposed solution is not right...")
        return False
    return True


# =============================================================================
#
# A simple main function for you to run. You should be able to test your
# implementation by simply running this module. E.g.
#   python spreadsheet.py
#
# =============================================================================

def print_error(solution, result):
    """Helper to print the error string"""
    print("    Expected {}({}), got {}({})".format(
        type(solution), solution, type(result), result))


if __name__ == '__main__':
    """The main entry point for this module.

    The main entry point for the function that runs a couple tests to validate
    the implementation of evaluate().
    """

    # The number of test cases that are correct
    correct = 0

    for i in range(len(testcase)):

        print("Test {}.".format(i))

        try:
            result = evaluate(testcase[i])
        except Exception as exc:
            result = exc

        # If the result is a matrix, make sure we were expecting a matrix
        if isinstance(result, list):
            if isinstance(solution[i], list):
                if validate(result, solution[i]):
                    print("    OK.")
                    correct += 1
                else:
                    print("    Results don't match")
            else:
                print_error(solution[i], result)

        # If the result is an error, make sure we were expecting an error
        else:
            if isinstance(solution[i], list):
                print_error(solution[i], result)
            else:
                if result.__class__ == solution[i]:
                    print("    OK.")
                    correct += 1
                else:
                    print_error(solution[i], result)

    print("------------------------------------------------------")
    print("You got {} out of {} correct.".format(correct, len(testcase)))
