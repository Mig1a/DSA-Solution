import re
def validate_html_tags(html):
    comb = {"</div>":"<div>", "</p>":"<p>", "</a>":"<a>"}
    stack = []
    parts = re.findall(r'<[^>]+>', html)
    for i in parts:
        if stack and i in ("</div>","</p>","</a>"):
            if stack[-1] == comb[i]:
                stack.pop()
            else:
                return False
        elif not stack and i in ("</div>","</p>","</a>"):
            return False
        else:
            stack.append(i)
    return not stack
html = "<div><p></p></div>"
print(validate_html_tags(html))

html_2 = "<div><p></div></p>"
print(validate_html_tags(html_2))

html_3 = "<div><p><a></a></p></div>"
print(validate_html_tags(html_3))

html_4 = "<div><p></a></p></div>"
print(validate_html_tags(html_4))