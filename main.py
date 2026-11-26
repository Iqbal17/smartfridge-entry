"""Roast the Smart Fridge: One Line, Best Laugh Wins — entry for make.fun.

Candidate lines weighed (draft pass):
1. "My fridge rated my 3 a.m. snack 'a cry for help' and locked itself;
   bold talk from an appliance whose whole job is enabling me."
   - Rejected: good attitude, but the fridge-locking-you-out angle is one
     several entrants reach for; freshness is scored second.
2. "My smart fridge has a camera, a diet plan, and strong opinions —
   congratulations, we invented a mother-in-law that keeps cheese cold."
   - Strong: the roast lands on a comparison nobody in the field used,
     and every clause adds a new absurd feature. Chosen as the base.
3. "The fridge sends expiration alerts for yogurt but stays silent about
   its own software from 2021 — physician, patch thyself."
   - Rejected: the patch gag is niche; a judge skimming pairs may miss
     the reference, while candidate 2 lands instantly.

The brief warns a stock milk-ordering joke loses, so no milk, no grocery
auto-orders: the final roasts the fridge's personality instead.

Revision pass (v1 -> final): the draft ended "a mother-in-law that keeps
cheese cold", which momentarily reads as praise for the mother-in-law.
Adding "also" — "that also keeps cheese cold" — makes the cold-keeping
the consolation prize of the invention, so the punchline lands as a
roast of the fridge rather than a compliment to it. Length re-checked
against the 160-char gate after the edit.
"""

import os

ENTRY = (
    "My smart fridge has a camera, a diet plan, and strong opinions — "
    "congratulations, we invented a mother-in-law that also keeps "
    "cheese cold."
)

MAX_CHARS = 160


def build_entry() -> str:
    """Return the single roast line, guarding the competition gate."""
    line = ENTRY.strip()
    if not line or "\n" in line:
        raise ValueError("entry must be exactly one non-empty line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, gate is {MAX_CHARS}")
    return line


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(build_entry() + "\n")


if __name__ == "__main__":
    main()
