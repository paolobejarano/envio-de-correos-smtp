def palabra_se_encuentra_en_la_lista(palabra: str, lista: list) -> bool:
    si_se_encuentra = False
    for elemento in lista:
        if elemento == palabra:
            si_se_encuentra = True
            break
        else:
            return False
    return si_se_encuentra


def test_palabra_se_encuentra_en_lista():
    funciona_correctamente = True

    if palabra_se_encuentra_en_la_lista('a', ['a', 'b']) == True:
        funciona_correctamente = True
    else:
        funciona_correctamente = False

    if palabra_se_encuentra_en_la_lista('z', ['a', 'b', 'c']) == False:
        funciona_correctamente = True
    else:
        funciona_correctamente = False

    if palabra_se_encuentra_en_la_lista('d', ['a', 'b', 'c', 'd']) == True:
        funciona_correctamente = True
    else:
        funciona_correctamente = False

    return funciona_correctamente

print(test_palabra_se_encuentra_en_lista())
