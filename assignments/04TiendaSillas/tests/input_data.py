# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
         ["1"],
        ["",
        "[['a', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]",
        "Par",
        "[['a', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]",
        "Pares Jugador1: 1"
         ],
        '''Ejecucion del programa:
        1
        [['a', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
        Par
        [['a', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
        Pares Jugador1: 1
        '''
    ),
    (
         ["2"],
        ["", 
         "[['a', 'b', '?', '?', '?', '?'], ['?', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', 'b', '?', '?', '?', '?'], ['?', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]",
        "Par",
        "[['a', 'b', '?', '?', '?', '?'], ['?', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', 'b', '?', '?', '?', '?'], ['?', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]",
        "Pares Jugador2: 11"
         ],
        '''Ejecucion del programa:
       2
[['a', 'b', '?', '?', '?', '?'], ['?', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', 'b', '?', '?', '?', '?'], ['?', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
Par
[['a', 'b', '?', '?', '?', '?'], ['?', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', 'b', '?', '?', '?', '?'], ['?', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
Pares Jugador2: 11
        '''
    ),
    (
         ["3"],
        ["", 
      "[['a', 'b', '?', '?', '?', 'f'], ['g', 'h', 'i', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', 'b', '?', '?', '?', 'f'], ['g', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', 'q']]",
"Impar",
"[['a', 'b', '?', '?', '?', 'f'], ['g', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', 'b', '?', '?', '?', 'f'], ['g', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]",
"Pares Jugador23: 5"
         ],
        '''Ejecucion del programa:
       ...
       '''
    )
    
   
    
    
    


]
