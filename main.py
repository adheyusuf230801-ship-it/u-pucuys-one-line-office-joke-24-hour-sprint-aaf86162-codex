from pathlib import Path


SETUP = "I asked a quick question in the office chat; "
PUNCHLINE = "it got a project manager, a budget, and a meeting to decide who should answer it."
JOKE = SETUP + PUNCHLINE

if "\n" in JOKE or len(JOKE) > 200:
    raise ValueError("The joke must be one line and at most 200 characters.")


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
