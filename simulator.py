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

# Read DFA from external JSON file
def loadexternaldata(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Example usage
dfa = loadexternaldata("testcase3.json")
simulate_dfa(dfa)