# our function
def GetNameFamily(name  ,family,middle=''):
    if middle:
        return rf"{name} {middle} {family}"
    else:
        return rf"{name} {family}"