def solution(input):
    import re
    
    # Define atomic weights for elements
    atomic_weights = {
        'H': 1,
        'C': 12,
        'O': 16,
        'N': 14,
        'S': 32,
        'P': 31,
        'Cl': 35.5,
        'Br': 80,
        'I': 127,
        'He': 4,
        'Li': 6.94,
        'Be': 9.0122,
        'B': 10.81,
        'C': 12.01,
        'N': 14.01,
        'O': 16.00,
        'F': 19,
        'Ne': 20.18,
        'Na': 22.99,
        'Mg': 24.31,
        'Al': 26.98,
        'Si': 28.09,
        'P': 30.97,
        'S': 32.07,
        'Cl': 35.45,
        'Ar': 39.95,
        'K': 39.10,
        'Ca': 40.08,
        'Sc': 44.96,
        'Ti': 47.87,
        'V': 50.94,
        'Cr': 51.996,
        'Mn': 54.94,
        'Fe': 55.85,
        'Co': 58.93,
        'Ni': 58.69,
        'Cu': 63.55,
        'Zn': 65.38,
        'Ga': 69.72,
        'Ge': 72.63,
        'As': 74.92,
        'Se': 78.97,
        'Br': 79.90,
        'Kr': 83.80,
        'Rb': 85.47,
        'Sr': 87.62,
        'Y': 88.91,
        'Zr': 91.22,
        'Nb': 92.91,
        'Mo': 95.94,
        'Tc': 98,
        'Ru': 101.07,
        'Rh': 102.91,
        'Pd': 106.42,
        'Ag': 107.87,
        'Cd': 112.41,
        'In': 114.82,
        'Sn': 118.71,
        'Sb': 121.76,
        'Te': 127.60,
        'I': 126.90,
        'Xe': 131.29,
        'Cs': 132.91,
        'Ba': 137.33,
        'La': 138.91,
        'Ce': 140.12,
        'Pr': 140.91,
        'Nd': 144.24,
        'Pm': 145,
        'Sm': 150.36,
        'Eu': 151.96,
        'Gd': 157.25,
        'Tb': 158.93,
        'Dy': 162.50,
        'Ho': 164.93,
        'Er': 167.26,
        'Tm': 168.93,
        'Yb': 173.04,
        'Lu': 174.97,
        'Hf': 178.49,
        'Ta': 180.95,
        'W': 183.84,
        'Re': 186.21,
        'Os': 190.23,
        'Ir': 192.22,
        'Pt': 195.08,
        'Au': 196.97,
        'Hg': 200.59,
        'Tl': 204.38,
        'Pb': 207.2,
        'Bi': 208.98,
        'Po': 209,
        'At': 210,
        'Rn': 222,
        'Fr': 223,
        'Ra': 226,
        'Ac': 227,
        'Th': 232.04,
        'Pa': 231.04,
        'U': 238.03,
        'Np': 237,
        'Pu': 244,
        'Am': 243,
        'Cm': 247,
        'Bk': 247,
        'Cf': 251,
        'Es': 252,
        'Fm': 257,
        'Md': 258,
        'No': 259,
        'Lr': 262,
        'Rf': 267,
        'Db': 270,
        'Sg': 271,
        'Bh': 270,
        'Hs': 277,
        'Mt': 276,
        'Ds': 281,
        'Rg': 282,
        'Cn': 285,
        'Nh': 286,
        'Fl': 289,
        'Mc': 290,
        'Lv': 293,
        'Ts': 294,
        'Og': 294
    }
    
    def parse_formula(formula):
        stack = []
        i = 0
        while i < len(formula):
            if formula[i].isalpha():  # Element
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1
                element = formula[i:j]
                i = j
                # Check for quantity
                quantity = 0
                while i < len(formula) and formula[i].isdigit():
                    quantity = quantity * 10 + int(formula[i])
                    i += 1
                if quantity == 0:
                    quantity = 1
                stack.append((element, quantity))
            elif formula[i] == '(':  # Start of a group
                stack.append('(')
                i += 1
            elif formula[i] == ')':  # End of a group
                group = []
                while stack and stack[-1] != '(':
                    group.append(stack.pop())
                stack.pop()  # Remove the '('
                group.reverse()
                i += 1
                # Check for quantity after the group
                quantity = 0
                while i < len(formula) and formula[i].isdigit():
                    quantity = quantity * 10 + int(formula[i])
                    i += 1
                if quantity == 0:
                    quantity = 1
                for element, count in group:
                    stack.append((element, count * quantity))
            else:
                i += 1
        
        return stack
    
    def calculate_weight(parsed_formula):
        total_weight = 0
        for element, count in parsed_formula:
            total_weight += atomic_weights[element] * count
        return total_weight
    
    parsed_formula = parse_formula(input)
    output = int(calculate_weight(parsed_formula))
    
    return output