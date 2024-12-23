"""
Generate look-up table for the way different moves rearrange the stickers on the cube.
"""

# All moves can be expressed in terms of just U, x, and y!
# fmt: off
U_INDICES = [
     7,  8,  1,  2,  3,  4,  5,  6,
    17, 18, 19, 12, 13, 14, 15, 16,
    25, 26, 27, 20, 21, 22, 23, 24,
    33, 34, 35, 28, 29, 30, 31, 32,
     9, 10, 11, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48
]
X_INDICES = [
     9, 10, 11, 12, 13, 14, 15, 16,
    41, 42, 43, 44, 45, 46, 47, 48,
    23, 24, 17, 18, 19, 20, 21, 22,
     5,  6,  7,  8,  1,  2,  3,  4,
    35, 36, 37, 38, 39, 40, 33, 34,
    29, 30, 31, 32, 25, 26, 27, 28
]
Y_INDICES = [
     7,  8,  1,  2,  3,  4,  5,  6,
    17, 18, 19, 20, 21, 22, 23, 24,
    25, 26, 27, 28, 29, 30, 31, 32,
    33, 34, 35, 36, 37, 38, 39, 40,
     9, 10, 11, 12, 13, 14, 15, 16,
    43, 44, 45, 46, 47, 48, 41, 42
]
# fmt: on


FACES = list("UuFfRrBbLlDdxyz")
MOVES = [f"{face}{suffix}" for face in FACES for suffix in ["", "2", "'"]]


def compute_move_indices(rc: list[int], move: str) -> list[int]:
    """Compute the index list representing the given move."""
    if move.endswith("'"):
        m = move[:-1]
        return compute_moveseq_indices(rc, [m, m, m])
    elif move.endswith("2"):
        m = move[:-1]
        return compute_moveseq_indices(rc, [m, m])
    elif move == "x":
        return rearrange_cube(rc, X_INDICES)
    elif move == "y":
        return rearrange_cube(rc, Y_INDICES)
    elif move == "z":
        return compute_moveseq_indices(rc, ["x", "y", "x'"])
    elif move == "U":
        return rearrange_cube(rc, U_INDICES)
    elif move == "u":
        return compute_moveseq_indices(rc, ["D", "y"])
    elif move == "F":
        return compute_moveseq_indices(rc, ["x", "U", "x'"])
    elif move == "f":
        return compute_moveseq_indices(rc, ["B", "z"])
    elif move == "R":
        return compute_moveseq_indices(rc, ["z'", "U", "z"])
    elif move == "r":
        return compute_moveseq_indices(rc, ["L", "x"])
    elif move == "B":
        return compute_moveseq_indices(rc, ["x'", "U", "x"])
    elif move == "b":
        return compute_moveseq_indices(rc, ["F", "z'"])
    elif move == "L":
        return compute_moveseq_indices(rc, ["z", "U", "z'"])
    elif move == "l":
        return compute_moveseq_indices(rc, ["R", "x'"])
    elif move == "D":
        return compute_moveseq_indices(rc, ["x2", "U", "x2"])
    elif move == "d":
        return compute_moveseq_indices(rc, ["U", "y'"])
    else:
        raise ValueError(f"Unrecognized move {move}")


def compute_moveseq_indices(rc: list[int], moves: list[str]) -> list[int]:
    """Compute the index list representing the given sequence of moves."""
    for m in moves:
        rc = compute_move_indices(rc, m)
    return rc


def rearrange_cube(rc: list[int], indices: list[int]) -> list[int]:
    """Apply the algorithm specified by the given index list."""
    return [rc[i - 1] for i in indices]


def to_gsheet(indices: list[int]) -> list[int]:
    """Convert a list of indices to a Google Sheets array literal."""
    return "{" + ",".join([f"{i:>2}" for i in indices]) + "}"


def main() -> None:
    """Run the script."""
    for m in MOVES:
        indices = compute_move_indices(list(range(1, 49)), m)
        m_quoted = f'"{m}"' if len(m) == 2 else f'"{m}" '
        print(f"move = {m_quoted}, rearrange_cube(rc, {to_gsheet(indices)}),")


if __name__ == "__main__":
    main()
