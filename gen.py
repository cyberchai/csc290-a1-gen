def gen(fsa):
    # given some fsa, we need to make sure we generate a valid word in the language
    word = ""
    current = "A"
    for i in (len(fsa[1])-1):
        if fsa[1][i][0] == current:
            word = word + fsa[1][i][2]
            current = fsa[1][i][1]


        if current is in fsa[2]:
            return word
