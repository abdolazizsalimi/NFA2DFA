import pandas as pd

nfa = {}

n = int(input(" num of states : "))
t = int(input(" num of transitions : "))


# init NFA ->
for i in range(n):
    state = input("state name :")
    nfa[state] = {}
    for j in range(t):
        path = input("path : ")
        print("Enter end state from state {} travelling through path {} :" .format(state,path))
        reaching_state = [x for x in input().split()]
        nfa[state][path] = reaching_state

#show NFA 
print("\n NFA :\n")
print(nfa)
print("\n NFA Table :\n")
nfa_table =  pd.DataFrame(nfa)
print(nfa_table.transpose())


#step 1 
print("Enter final state of NFA : ")
nfa_final_list = [x for x in input().split()]
new_states_list = [] 
dfa = {}

keys_list = list(list(nfa.keys())[0])
path_list = list(nfa[keys_list[0]].keys())
dfa[keys_list[0]] = {}
for k in range(t):
    temp ="".join(nfa[keys_list[0]][path_list[k]])
    dfa[keys_list[0]][path_list[k]] = temp 
    #check trap
    if temp not in  keys_list:
        new_states_list.append(temp)
        keys_list.append(temp)

#step 2        
while len(new_states_list) != 0 :
    dfa[new_states_list[0]] = {}
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp  = []
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[j]]
                s ="".join(temp)
                if s not in keys_list:
                    new_states_list.append(s)
                    keys_list.append(s)
                dfa[new_states_list[0]][path_list[i]] = s
    new_states_list.remove(new_states_list[0])



#show DFA 
print("\nDFA :\n")
print(dfa)
print("\nPrinting DFA table : \n")
dfa_table  = pd.DataFrame(dfa)
print(dfa_table.transpose)