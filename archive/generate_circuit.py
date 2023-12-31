import sys

sys.path.append("../models")
import circuit
import pyperclip

coordinates = circuit.create_data_model()["locations"]

# The route given as a list of indices in the order they should be connected
route = [
    0,
    1,
    279,
    2,
    278,
    277,
    248,
    247,
    243,
    242,
    241,
    240,
    239,
    238,
    245,
    244,
    246,
    249,
    250,
    229,
    228,
    231,
    230,
    237,
    236,
    235,
    234,
    233,
    232,
    227,
    226,
    225,
    224,
    223,
    222,
    218,
    221,
    220,
    219,
    202,
    203,
    204,
    205,
    207,
    206,
    211,
    212,
    215,
    216,
    217,
    214,
    213,
    210,
    209,
    208,
    251,
    254,
    255,
    257,
    256,
    253,
    252,
    139,
    140,
    141,
    142,
    143,
    199,
    201,
    200,
    195,
    194,
    193,
    191,
    190,
    189,
    188,
    187,
    163,
    164,
    165,
    166,
    167,
    168,
    169,
    171,
    170,
    172,
    105,
    106,
    104,
    103,
    107,
    109,
    110,
    113,
    114,
    116,
    117,
    61,
    62,
    63,
    65,
    64,
    84,
    85,
    115,
    112,
    86,
    83,
    82,
    87,
    111,
    108,
    89,
    90,
    91,
    102,
    101,
    100,
    99,
    98,
    97,
    96,
    95,
    94,
    93,
    92,
    79,
    88,
    81,
    80,
    78,
    77,
    76,
    74,
    75,
    73,
    72,
    71,
    70,
    69,
    66,
    68,
    67,
    57,
    56,
    55,
    54,
    53,
    52,
    51,
    50,
    49,
    48,
    47,
    46,
    45,
    44,
    43,
    58,
    60,
    59,
    42,
    41,
    40,
    39,
    38,
    37,
    36,
    35,
    34,
    33,
    32,
    31,
    30,
    29,
    124,
    123,
    122,
    121,
    120,
    119,
    118,
    156,
    157,
    158,
    173,
    162,
    161,
    160,
    174,
    159,
    150,
    151,
    155,
    152,
    154,
    153,
    128,
    129,
    130,
    131,
    18,
    19,
    20,
    127,
    126,
    125,
    28,
    27,
    26,
    25,
    21,
    24,
    22,
    23,
    13,
    12,
    14,
    11,
    10,
    9,
    7,
    8,
    6,
    5,
    275,
    274,
    273,
    272,
    271,
    270,
    15,
    16,
    17,
    132,
    149,
    177,
    176,
    175,
    178,
    179,
    180,
    181,
    182,
    183,
    184,
    186,
    185,
    192,
    196,
    197,
    198,
    144,
    145,
    146,
    147,
    148,
    138,
    137,
    136,
    135,
    134,
    133,
    269,
    268,
    267,
    266,
    265,
    264,
    263,
    262,
    261,
    260,
    258,
    259,
    276,
    3,
    4,
    0,  # ... and so on for the full route
]


# Generate the TikZ code for the given route and coordinates
def generate_tikz_code(route, coordinates):
    this_part = ""
    tikz_code = """\\documentclass[tikz]{{standalone}}
    

\\begin{{document}}
\\begin{{tikzpicture}}

% Draw the path
\\draw[blue, thick] plot coordinates {{
"""
    # Add coordinates in the order of the route to create the path
    for index in route:
        if index < len(coordinates):
            x, y = coordinates[index]
            tikz_code += f"  ({x}, {y})\n"

    tikz_code += """}};
% Draw the nodes
"""
    # Add nodes for each coordinate

    for x, y in coordinates:
        tikz_code += (
            f"\\node[draw,circle,inner sep=0pt,minimum size=0.15cm, fill=white] (J) at ({x},{y})"
            + " {} ;\n"
        )
        this_part += (
            f"\\node[draw,circle,inner sep=0pt,minimum size=0.15cm, fill=white] (J) at ({x},{y})"
            + " {} ;\n"
        )

    tikz_code += """\\end{tikzpicture}
\\end{document}
"""
    return tikz_code, this_part


# Generate the TikZ code
tikz_code, this_part = generate_tikz_code(route, coordinates)

# Copy the generated TikZ code to the clipboard
pyperclip.copy(this_part)

# Print the code as well (for verification)
print("The TikZ code has been copied to your clipboard.")
print(tikz_code)
