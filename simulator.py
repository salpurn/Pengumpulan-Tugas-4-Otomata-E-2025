import json

def simulate_dfa(dfa):
    states = dfa["states"]
    alphabet = dfa["alphabet"]
    start_state = dfa["start_state"]
    accept_states = set(dfa["accept_states"])
    transitions = dfa["transitions"]
    test_string = dfa["test_string"]
    
    current_state = start_state
    path = [current_state]
    
    for symbol in test_string:
        if symbol not in alphabet:
            print("Error: Symbol not in alphabet.")
            return
        
        if current_state in transitions and symbol in transitions[current_state]:
            current_state = transitions[current_state][symbol]
            path.append(current_state)
        else:
            print("Error: No valid transition found.")
            return
    
    status = "ACCEPTED" if current_state in accept_states else "REJECTED"
    print("Path:", " → ".join(path))
    print("Status:", status)

# Read multiple DFA configurations from external JSON files
def load_external_data(*file_paths):
    dfas = []
    for file_path in file_paths:
        with open(file_path, "r") as file:
            dfas.append(json.load(file))
    return dfas

# Example usage
dfa_list = load_external_data("testcase1.json", "testcase2.json", "testcase3.json")
for dfa in dfa_list:
    simulate_dfa(dfa)
    print()

#Read DFA from singular external JSON file
#def loadexternaldata(file_path):
#    with open(file_path, "r") as file:
#        return json.load(file)

#Example usage
#dfa = loadexternaldata("testcase1.json")
#simulate_dfa(dfa)
