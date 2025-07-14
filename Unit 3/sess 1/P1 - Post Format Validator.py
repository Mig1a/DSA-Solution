def is_valid_post_format(posts):
    stack = []
    tag_map = {')': '(', ']': '[', '}': '{'}

    for char in posts:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != tag_map[char]:
                return False
            stack.pop()

    return not stack

print(is_valid_post_format("((){})"))
print(is_valid_post_format("()[]{}"))
print(is_valid_post_format("(]"))














