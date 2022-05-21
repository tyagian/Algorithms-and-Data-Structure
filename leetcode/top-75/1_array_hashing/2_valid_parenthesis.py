#https://leetcode.com/problems/valid-parentheses/
# This can be solved by stack also but using hash-map here.
class test:
    def valid_parenthesis(s):
        brackets_dict = {'(':')' , '[':']' , '{':'}'}
        open_brackets = []

        for bracket in s:
            if bracket in brackets_dict:
                open_brackets.append(bracket)
            else:
                # if open_brack list not empty and open_brackets[-1] is value of key in brackets_dict 
                if len(open_brackets) and brackets_dict[open_brackets[-1]] == bracket:
                    del open_brackets[-1]
                else:
                    return False
        return open_brackets == []
# time: O(n)
# space: O(n)
def main():
    input_ = "{()[]}"
    output = test.valid_parenthesis(input_)
    print (output)

if __name__ == '__main__':
    main()
