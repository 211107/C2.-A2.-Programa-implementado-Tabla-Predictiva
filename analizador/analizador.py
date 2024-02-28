grammar_table = {
    ('E', 'delete'): ['delete', 'D1'],
    ('D1', 'from'): ['from', 'I', 'O'],
    ('I', '[a-zA-Z]+'): ['L', 'R'],
    ('L', '[a-zA-Z]+'): ['[a-zA-Z]+'],
    ('R', '[a-zA-Z]+'): ['L', 'R'],
    ('R', 'where'): ['ε'],
    ('R', "'"): ['ε'],
    ('R', '$'): ['ε'],
    ('R', '='): ['ε'],
    ('O', 'where'): ['where', 'C'],
    ('O', '$'): ['ε'],
    ('C', '[a-zA-Z]+'): ['I', '=', 'V'],
    ('V', '[0-9]+'): ['D', 'RE'],
    ('V', "'"): ["'", 'I', "'"],
    ('RE', '[0-9]+'): ['D', 'RE'],
    ('RE', '$'): ['ε'],
    ('D', '[0-9]+'): ['[0-9]+']
}


#simbolos terminales obtenidos en la tabla
terminales = set([clave[1] for clave in grammar_table.keys()])
palabras_reservadas = ['delete', 'from', 'where']

#toma una lista de palabras y devuelve una de simbolos
def symbol_organizer(palabras):
    simbolos = []
    for palabra in palabras:
        if palabra in palabras_reservadas:
            simbolos.append(palabra)
        else:
            for letra in palabra:
                if letra.isalpha():
                    simbolos.append('[a-zA-Z]+')
                elif letra.isdigit():
                    simbolos.append('[0-9]+')
                else:
                    simbolos.append(letra)
    return simbolos

def analizador(entrada):
    stack = ['$', 'E']
    text = "Pila: " + str(stack) + "\n"
    #agrega el fin de cadena ala entrada
    entrada = entrada.strip() + ' $'
    palabras = entrada.split(' ')
    simbolos = symbol_organizer(palabras)
    #recorre los simbolos
    index = 0
    while True:
        #extrae el simbolo de la parte superior
        X = stack.pop()
        #obtiene el simbolo
        a = simbolos[index]
        text += f"\nToken actual: {a}\n"
        text += f"Pila: {stack}\n"
        if X in terminales:
            #si coincide  avanza y si es el fin  retorna el estado final
            if X == a:
                index += 1
                if X == '$':
                    return text
            else:
                return text + f"\nError de sintaxis: se esperaba '{X}' pero se encontró '{a}'"
        else:
            #si no es un terminal busca la produccion correspondiente en la tabla 
            if (X, a) in grammar_table:
                producciones = grammar_table[(X, a)]
                if producciones != ['ε']:
                    #agrega las producciones a la pila en inverso
                    for produccion in reversed(producciones):
                        stack.append(produccion)
            else:
                return text + f"\nError de sintaxis: no hay producción para '{X}' con '{a}'"

            
    
        