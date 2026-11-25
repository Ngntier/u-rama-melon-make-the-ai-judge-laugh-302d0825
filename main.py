import os


ENTRY = "The office fire drill is the only meeting where everyone shows up, nobody talks over anyone, and we all leave early — and it's the only one nobody scheduled."


def validate(text):
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")
    return text


def main():
    line = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
