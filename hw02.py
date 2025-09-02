def is_valid_brackets(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

if __name__ == "__main__":
    print(is_valid_brackets("([]){}"))
    print(is_valid_brackets("([)]"))
