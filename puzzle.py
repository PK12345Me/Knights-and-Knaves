from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
"""clauses are disjunctive (with v/or)"""

S = And(AKnave, AKnight)

knowledge0 = And(Implication(Implication(AKnight, Not(S)), AKnave))


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
"""S = AKnave ^ BKnave """

knowledge1 = And(
    # Implication(Implication(AKnave, Not(And(AKnave, BKnave))), BKnight)
    Implication(Implication(AKnave, Not(And(AKnave, BKnave))), AKnave),
    Implication(AKnave, BKnight),
)


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

knowledge2 = And(
    Implication(AKnight, BKnight),
    Implication(BKnight, Not(AKnight)),
    Implication(Implication(BKnight, Not(And(AKnight, BKnight))), AKnave),
    Biconditional(AKnave, BKnight),
)


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Implication(BKnight, AKnave),
    Implication(AKnave, Not(BKnight)),  # coz B is lying
    Implication(Not(BKnight), CKnight),
    Biconditional(CKnight, AKnight),
    Implication(Biconditional(CKnight, AKnight), BKnave),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
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
