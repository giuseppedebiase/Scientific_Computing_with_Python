def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        if '/' in problem or 'x' in problem:
            return "Error: Operator must be '+' or '-'."
    
    #Splits each operation in a list made by: ['Operand1', 'Operator', 'Operand2']
    problems_l = [problem.split(' ') for problem in problems]

    for problem in problems_l:
        if problem[0].isnumeric() == False or problem[2].isnumeric() == False:
            return 'Error: Numbers must only contain digits.'
    
    for problem in problems_l:
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    #Makes the two operands the same length by adding spaces before the shortest one
    for problem in problems_l:
        if len(problem[0]) > len(problem[2]):
            problem[2] = ' ' * (len(problem[0]) - len(problem[2])) + problem[2]
        elif len(problem[2]) > len(problem[0]):
            problem[0] = ' ' * (len(problem[2]) - len(problem[0])) + problem[0]
        #Adds a space after the operator
        problem[1] = problem[1] + ' '
    
    #First row of operands
    first_row = '  '
    for problem in problems_l:
        first_row += problem[0] + '      '
    first_row = first_row.rstrip('      ')

    #Second row of operands
    second_row = ''
    for problem in problems_l:
        second_row += problem[1] + problem[2] + '    '
    second_row = second_row.rstrip('    ')

    #Third row with dashes
    third_row = []
    for i in range (len(first_row)):
        if first_row[i] != ' ' or second_row[i] != ' ':
            third_row.append('-')
        else:
            third_row.append(' ')
    
    '''
    Fills some postions of the third row with '-'
    Lines 43-47 leave single-spaces gaps that must be filled. Example:
       32
    + 698
    - ---   
    '''
    for i in range (1, len(third_row) - 1):
        if third_row[i-1] == '-' and third_row[i+1] == '-':
            third_row[i] = '-'
    third_row = ''.join(third_row)

    problems = first_row + '\n' + second_row + '\n' + third_row

    #Solutions
    if show_answers == True:
        solutions = []

        #Adds or subtracts the two operators
        for problem in problems_l:
            if problem[1] == '+ ':
                solutions.append(int(problem[0]) + int(problem[2]))
            elif problem[1] == '- ':
                solutions.append(int(problem[0]) - int(problem[2]))

        #Adds spaces before the solution
        for i in range (len(solutions)):
            n_spaces = len(problems_l[i][1]) + len(problems_l[i][2]) - len(str(solutions[i]))
            solutions[i] = ' ' * n_spaces + str(solutions[i])

        solutions = '    '.join(solutions)

        problems += '\n' + solutions
        
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
