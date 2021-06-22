def multi_bracket_validation(input):   #given a string it will curent if the brackets inside it are opened or closed 
   
    open = ["(","[","{"]
    close = [")","]","}"]
    curent = []

    for i in input:

            if i in open:
                curent.append(open.index(i))

            elif i in close:
                if ((len(curent) > 0) and (close.index(i) == curent[-1])):
                    curent.pop()
                else:
                    return False

    if len(curent) == 0:
            return True
    else:
            return False

if __name__ == "__main__":
    print(multi_bracket_validation('({)}'))
    print(multi_bracket_validation('(some string)'))