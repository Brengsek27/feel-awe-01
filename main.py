"""Main entry for feel-awe-01 competition.
Writes a fixed short text to an output file.
"""

import os
import sys

# The validation logic ensures the fixed text conforms to the competition constraints.

# Fixed text to be written – must stay exactly as specified.
TEXT = (
    "Far below, a river is cutting stone one grain at a time, patient as breath. "
    "It has been on its way for six million years and is not late. "
    "Your hurry is very young here. Already, it is tired."
)


def validate(text: str) -> None:
    """Validate that *text* is between 1 and 280 Unicode code points and not only whitespace.
    Raises a ``ValueError`` if the check fails.
    """
    codepoints = len(text)
    if not (1 <= codepoints <= 280):
        raise ValueError(f"Text must contain between 1 and 280 code points, got {codepoints}.")
    if text.strip() == "":
        raise ValueError("Text must contain non‑whitespace characters.")


def main() -> None:
    # Validate the constant text.
    validate(TEXT)

    out_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    # Encode without adding a newline.
    data = TEXT.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)

    # Report counts.
    print(f"Wrote {len(TEXT)} code points ({len(data)} bytes) to {out_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

