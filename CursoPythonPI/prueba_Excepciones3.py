def EvaluEdad(edad):
    if edad<20:
        return "Eres demasiado joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate"

print(EvaluEdad(19))
