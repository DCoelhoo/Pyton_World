from pathlib import Path

path = Path("../books/alice.txt")
contents = path.read_text(encoding="utf-8")

print(contents.lower().count("the "))

