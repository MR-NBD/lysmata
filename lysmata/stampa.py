from art import *


def print_Lysmata():
    font = "doom"
    # Testo da visualizzare
    text = "Lysmata"
    ascii_art = text2art(text, font=font)
    color = "\033[38;5;208m"
    print(color + ascii_art + "\033[0m")


# Animation
# animation = [
#    "[             ]",
#    "[=            ]",
#    "[==           ]",
#    "[===          ]",
#    "[====         ]",
#    "[ ====        ]",
#    "[  ====       ]",
#    "[   ====      ]",
#    "[    ====     ]",
#    "[     ====    ]",
#    "[      ====   ]",
#    "[       ====  ]",
#    "[        ==== ]",
#    "[         ====]",
#    "[          ===]",
#    "[           ==]",
#    "[            =]",
# ]
# an = 0
# Animation Print
# sys.stdout.write("\r" + "Fuzzing " + animation[an % len(animation)])
# sys.stdout.flush()
# an += 1
