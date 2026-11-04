import sys

def greet(name: str) -> str:
    return f"Hello {name}, running Python {sys.version.split()[0]}"

if __name__ == "__main__":
    print(greet("Vijay"))
