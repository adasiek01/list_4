class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


import re, sys
def checking_HTML_correctness(filename):
    """
    Funkcja ma za zadanie sprawdzać poprawność składni dokumentu HTML.
    Jako argument przyjmuje nazwę pliku, który ma sprawdzić.
    Zwraca True jeśli dokument jest poprawny składniowo i False jeśli nie jest.
    """
    file_obj = open(filename, 'r')
    text = file_obj.read()

    text = re.sub("(<!--.*?-->)", "", text)
    no_comments = open("html.txt", 'w')
    no_comments.write(text)
    no_comments.close()

    output=""
    with open("html.txt") as f:
        for line in f:
            if not line.isspace():
                output+=line
    no_empty_lines = open("html.txt", 'w')
    no_empty_lines.write(output)     
    no_empty_lines.close()

    another_output = ""
    with open("html.txt", "r") as fd:
        for line in fd:
            line = line.replace("\r", "").replace("\n", "")
            another_output += line
    no_new_lines = open("html.txt", 'w')
    no_new_lines.write(another_output)
    no_new_lines.close()
        
    integrated_file = open("html.txt", 'r')
    integrated_text = integrated_file.read()
    final = integrated_text.split('<')

    final.pop(0)
    final.pop(0)

    not_closed_tags = ['img', 'br', 'BR', 'meta', 'link', 'hr' ]
    without_bracket = []
    without_space_bracket = []
    for i in range(0,len(final)):
        if ">" in final[i]:
            point = final[i].index(">")
            without_bracket.append(final[i][:point])
        else:
            without_bracket.append(final[i])

    for i in range(0,len(final)):    
        if " " in without_bracket[i]:
            point = without_bracket[i].index(" ")
            without_space_bracket.append(without_bracket[i][:point])
        else:
            without_space_bracket.append(without_bracket[i])

    ind = 0
    while ind<len(without_space_bracket):
        if without_space_bracket[ind] in not_closed_tags:
            without_space_bracket.remove(without_space_bracket[ind])
        else:
            ind +=1

    indx = 0
    html_stack = Stack()
    balanced = True
    while indx < len(without_space_bracket) and balanced:
        symbol = without_space_bracket[indx]
        if "/" not in symbol:  # znacznik otwierający
            html_stack.push(symbol)
        else:
            if html_stack.isEmpty():
                balanced = False
            else:
                top = html_stack.pop()
                if symbol != "/" + top:
                    balanced = False
        indx += 1

    if balanced and html_stack.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    print(checking_HTML_correctness("L4_ZAD4_sampleHTML_1.txt"))
    print(checking_HTML_correctness("L4_ZAD4_sampleHTML_2.txt"))
    print(checking_HTML_correctness("L4_ZAD4_sampleHTML_3.txt"))
