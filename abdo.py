def revers(text):
    test=""
    i=-1
    while i:
        test+=text[i]
        i-=1
        if len(test) == len(text):
            break
    return test