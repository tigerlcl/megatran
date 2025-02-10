import re

def solution(input):
    # Atomic weights of elements
    atomic_weights = {
        'H': 1, 'He': 4, 'Li': 7, 'Be': 9, 'B': 11, 'C': 12, 'N': 14, 'O': 16, 'F': 19, 'Ne': 20,
        'Na': 23, 'Mg': 24, 'Al': 27, 'Si': 28, 'P': 31, 'S': 32, 'Cl': 35.5, 'Ar': 40, 'K': 39, 'Ca': 40,
        'Sc': 45, 'Ti': 48, 'V': 51, 'Cr': 52, 'Mn': 55, 'Fe': 56, 'Co': 59, 'Ni': 59, 'Cu': 64, 'Zn': 65,
        'Ga': 70, 'Ge': 73, 'As': 75, 'Se': 79, 'Br': 80, 'Kr': 84, 'Rb': 85, 'Sr': 88, 'Y': 89, 'Zr': 91,
        'Nb': 93, 'Mo': 96, 'Tc': 98, 'Ru': 101, 'Rh': 103, 'Pd': 106, 'Ag': 108, 'Cd': 112, 'In': 115, 'Sn': 119,
        'Sb': 122, 'Te': 128, 'I': 127, 'Xe': 131, 'Cs': 133, 'Ba': 137, 'La': 139, 'Ce': 140, 'Pr': 141, 'Nd': 144,
        'Pm': 145, 'Sm': 150, 'Eu': 152, 'Gd': 157, 'Tb': 159, 'Dy': 162, 'Ho': 165, 'Er': 167, 'Tm': 169, 'Yb': 173,
        'Lu': 175, 'Hf': 178, 'Ta': 181, 'W': 184, 'Re': 186, 'Os': 190, 'Ir': 192, 'Pt': 195, 'Au': 197, 'Hg': 201,
        'Tl': 204, 'Pb': 207, 'Bi': 209, 'Th': 232, 'Pa': 231, 'U': 238, 'Np': 237, 'Pu': 244, 'Am': 243, 'Cm': 247,
        'Bk': 247, 'Cf': 251, 'Es': 252, 'Fm': 257, 'Md': 258, 'No': 259, 'Lr': 262, 'Rf': 267, 'Db': 270, 'Sg': 271,
        'Bh': 270, 'Hs': 277, 'Mt': 276, 'Ds': 281, 'Rg': 282, 'Cn': 285, 'Nh': 284, 'Fl': 289, 'Mc': 288, 'Lv': 293,
        'Ts': 294, 'Og': 294
    }
    
    def parse_formula(formula):
        # Regular expression to match elements and their counts
        element_pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
        stack = []
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append('(')
                i += 1
            elif formula[i] == ')':
                i += 1
                num = ''
                while i < len(formula) and formula[i].isdigit():
                    num += formula[i]
                    i += 1
                num = int(num) if num else 1
                temp = []
                while stack and stack[-1] != '(':
                    elem, count = stack.pop()
                    temp.append((elem, count * num))
                stack.pop()  # Remove the '('
                for elem, count in temp:
                    stack.append((elem, count))
            else:
                match = element_pattern.match(formula, i)
                elem = match.group(1)
                num = match.group(2)
                num = int(num) if num else 1
                stack.append((elem, num))
                i = match.end()
        return stack
    
    def calculate_molecular_weight(parsed_formula):
        weight = 0
        for elem, count in parsed_formula:
            weight += atomic_weights[elem] * count
        return weight
    
    parsed_formula = parse_formula(input)
    molecular_weight = calculate_molecular_weight(parsed_formula)
    return molecular_weight