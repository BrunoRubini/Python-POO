def validar_estandar_conocimiento(cantidad_cursos: int, antiguedad: int)-> bool:
    if antiguedad // 6 <= cantidad_cursos:
        return True
    else:
        return False