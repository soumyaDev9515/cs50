from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    Biconditional(AKnight,AND(AKnight,AKnave)),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(# A is a knight or a knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is a knight or a knave
    Or(BKnight, BKnave),
    # B cannot be both
    Not(And(BKnight, BKnave)),

    Biconditional(AKnight, And(AKnave, BKnave))
)
    


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
# A is a knight or a knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A said that has the same kind of B
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),

    # B said that A is a different type than him
    Implication(BKnight, Or(And(BKnight, AKnave), And(BKnave, AKnight))),
    Implication(BKnave, Not(Or(And(BKnave, AKnight), And(BKnight, AKnave)))),
)
    


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
   Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # C is a knight or a knave
    Or(CKnight, CKnave),
    Not(And(BKnight, BKnave)),
     Or(CKnight, CKnave),
     Not(And(CKnight, CKnave)),


    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),


    # B says "A said 'I am a knave'."
Biconditional(BKnight, Biconditional(AKnight, AKnave)),

    # B says "C is a knave."
    Biconditional(BKnight, CKnave),

    # C says "A is a knight."
    Biconditional(CKnight, AKnight),

    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
