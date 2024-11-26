def comments_correct(comments: str) -> bool:
    if len(comments) % 2 != 0:
        return False
    # create a variable that counts how many /* there are in the string
    # if there is a */ we remove one if there is /* we add one
    # if at the end the variable is not 0 the output will be false
    multi_line_comments = 0 
    
    # split the string per two characters {n}
    n = 2
    comment_list = [comments[i:i+n] for i in range(0, len(comments), n)]

    for comment in comment_list:
        if comment == "//":
            continue
        elif comment == "/*":
            multi_line_comments += 1
        elif comment == "*/":
            multi_line_comments -= 1
        else: return False # the two chars isn't a valid comment character set

    if multi_line_comments == 0: return True
    else: return False