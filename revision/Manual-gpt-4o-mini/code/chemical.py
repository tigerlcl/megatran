def solution(input):
    import re
    from collections import defaultdict

    # Define atomic weights
    atomic_weights = {
        'H': 1,
        'He': 4,
        'Li': 7,
        'Be': 9,
        'B': 11,
        'C': 12,
        'N': 14,
        'O': 16,
        'F': 19,
        'Ne': 20,
        'Na': 23,
        'Mg': 24,
        'Al': 27,
        'Si': 28,
        'P': 31,
        'S': 32,
        'Cl': 35,
        'Ar': 40,
        'K': 39,
        'Ca': 40,
        'Sc': 45,
        'Ti': 48,
        'V': 51,
        'Cr': 52,
        'Mn': 55,
        'Fe': 56,
        'Co': 59,
        'Ni': 58,
        'Cu': 64,
        'Zn': 65,
        'Ga': 70,
        'Ge': 73,
        'As': 75,
        'Se': 78,
        'Br': 80,
        'Kr': 84,
        'Rb': 85,
        'Sr': 88,
        'Y': 89,
        'Zr': 91,
        'Nb': 93,
        'Mo': 96,
        'Tc': 98,
        'Ru': 101,
        'Rh': 103,
        'Pd': 106,
        'Ag': 108,
        'Cd': 112,
        'In': 115,
        'Sn': 118,
        'Sb': 121,
        'Te': 128,
        'I': 127,
        'Xe': 131,
        'Cs': 132,
        'Ba': 137,
        'La': 138,
        'Ce': 140,
        'Pr': 141,
        'Nd': 144,
        'Pm': 145,
        'Sm': 150,
        'Eu': 152,
        'Gd': 157,
        'Tb': 159,
        'Dy': 162,
        'Ho': 164,
        'Er': 167,
        'Tm': 169,
        'Yb': 173,
        'Lu': 175,
        'Hf': 178,
        'Ta': 181,
        'W': 184,
        'Re': 186,
        'Os': 192,
        'Ir': 192,
        'Pt': 195,
        'Au': 197,
        'Hg': 201,
        'Tl': 204,
        'Pb': 207,
        'Bi': 209,
        'Po': 209,
        'At': 210,
        'Rn': 222,
        'Fr': 223,
        'Ra': 226,
        'Ac': 227,
        'Th': 232,
        'Pa': 231,
        'U': 238,
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

    # Regular expression to match elements and their counts
    pattern = r'([A-Z][a-z]?)(\d*)|(\()|(\))(\d*)'
    stack = []
    molar_mass = 0

    for element, count, open_paren, close_paren, multiplier in re.findall(pattern, input):
        if element:  # If it's an element
            count = int(count) if count else 1
            molar_mass += atomic_weights[element] * count
        elif open_paren:  # If it's an opening parenthesis
            stack.append(molar_mass)
            molar_mass = 0
        elif close_paren:  # If it's a closing parenthesis
            count = int(multiplier) if multiplier else 1
            molar_mass = stack.pop() + molar_mass * count

    return int(molar_mass)