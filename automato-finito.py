# Henrique Morais
# 11521ECP007
# AUTOMATO-FINITO
#-----------------------------------
# 
#   EXEMPLE OF ENTRIES:
#   ----------------------
#   NUMBER OF STATES:               3
#   QT SYMBOLS + SYMBOLS:           2 a b
#   QT ACCEPTED STATES + STATES:    1 2
#   NUMBER OF TRANSITIONS:          6
#   transition1                     0 a 1
#   transition2                     0 b 1
#   transition3                     1 a 1
#   transition4                     1 b 2
#   transition5                     2 a 0
#   transition6                     2 b 2
#   NUMBER OF CHAINS TO TEST:       5
#   chain1                          abbbba
#   chain2                          aabbbb
#   chain3                          bbabbabbabbb
#   chain4                          bbbbbbbbbbb
#   chain5(exemple of empty chain)  -
#
# 
# 
#

# Definiçoes de entrada
n = input() # Qtd estados
E = [2,'a','b'] # input().split(" ") # Qtd simbolos no alfabeto / alfabeto, <3 a b c> ou <6 a b c d e f>
F = input().split(" ") # Qtd de estados de aceitaçao / estados, <1 2> ou <4 0 1 2 3>
t = input() # Numero de transiçoes

n = int(n) 
t = int(t)
E = E[1:] # Lista dos meus simbolos do alfabeto

F = list(map(int,F[1:])) # Conjunto dos meus estados finais de aceitaçao (dtype == int)

T = [{l:[] for l in E} for i in range(n)]
for i in range(t): # Preenche todas as transiçoes na tabela de transiçoes criada acima
    tran = input().split(" ")
    start = int(tran[0])
    to = int(tran[2])
    symb = tran[1]
    T[start][symb].append(to)

# c = int(input()) # Numero de cadeias a serem avaliadas
# my_entries = []

# for i in range(c): # Preenchimento das cadeias de entradas
#     chain = input()
#     my_entries.append(chain)

# Inicio da verificaçao
def main(entry):
    states = [0] # Estado inicial sempre q_0
    if entry == '-': # A entrada vazia só aceita caso o estados estados de aceitaçao contenham q0
        for state in states:
            if state in F:
                print('aceita')
                return None
            else: 
                print('rejeita')
                return None

    final_states = test(entry, states, 0)
    if ContainFinalState(final_states): # Testa se a cadeia final gerada pertence a linguagem
        print('aceita --- ' + entry)
    # else:
    #     print('rejeita --- '+ entry)

def ContainFinalState(states): # Confere se algum estado do conjunto atual está contido nos estados finais
    if states == None: 
        return False
    for i in states:
        for c in F:
            if i == c: 
                return True
    return False

def test(entry, states, pos):
    if len(entry) == pos: 
        if ContainFinalState(states):
            return states   # Se estivermos percorrido toda 
                            # a cadeia estivermos em um conjunto que
                            # contém algum estado final
                            # retorna o conjunto de estados 
                            # que estão sendo analizados
        return None
    symb = entry[pos]
    # BACKTRACKING:
    for coming in states: # Percorre todos os possiveis
                          # estados em analize atualmente
        going = T[coming][symb]
        if len(going) == 0: 
            return None # Estado sem saída

        # Se houver transiçao, vai para o conjunto going
        # de estados e analisa o proximo elemento
        new_transition = test(entry,going,pos+1)
        if new_transition != None: 
            return new_transition
    return None

# CRIANDO OS INPUTS DE TESTE
from itertools import permutations as prm
a = ''
b = ''
total_list = []
num_elementos = 6
for i in range(1,num_elementos+1):
    a = a+'a'
    b = b+'b'
    possibilidades = prm(a+b,i) # Calculo das permutaçoes de a e b para i elementos
    my_list = list(dict.fromkeys(list(possibilidades))) # Remove as duplicatas
    for c in my_list:
        total_list.append("".join(c))

for i in total_list:
    main(i)