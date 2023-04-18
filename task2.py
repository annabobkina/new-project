
# Функция принимает на вход строку, которая
# состоит из скобок трех типов: круглые, квадратные
# и фигурные. Функция должна проверить, является ли
# переданная последовательность скобок сбалансированной
# или нет. Функция возвращает True, если последовательность
# сбалансирована, и False – в противном случае.
def is_balanced(line):
    stack = []
    line = list(line)
    open_brackets = ['(', '[', '{']
    dict_brackets = {')': '(', ']': '[', '}': '{'}
    for i in line:
        if i in open_brackets:
            stack.append(i)
        else:
            if len(stack) == 0:
                return false
                break
            else:
                if dict_brackets[i] in stack:
                    stack.remove(dict_brackets[i])
                else:
                    return False
                    break
    if len(stack) == 0:
        return True
    else:
        return False


def test_is_balanced():
    cases = {
        '((((((((())))))))': False,
        '{[()]}{{}}': True,
        '{[()]}{]{}}': False,
        '{{{((([[[]]])))}}}': True,
        '{}': True,
        '(': False,
        '(}': False,
        '(((())))[]{}': True,
        '((()': False,
        '[{}{})(]': False,
        '{[]{([[[[[[]]]]]])}}': True,
        '{[]{([[[[[[]])]]])}}': False,
    }
    for i, case in enumerate(cases.keys()):
        if is_balanced(case) == cases[case]:
            print(f'{i}: OK')
        else:
            print(f'{i}: Not OK')


def main():
    test_is_balanced()


if __name__ == '__main__':
    main()