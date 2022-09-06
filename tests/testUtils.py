def oo(t):
    if type(t) == list:
        t = list(map(lambda x: str(x), t))
        out_string = "{" + " ".join(t) + "}"
        print(out_string)
        return out_string
    else:
        out_string = o(t)
        print(out_string)
        return out_string

    