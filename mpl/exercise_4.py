def remove_from_start(s: str, n: int) -> str:
    """Remove characters from index 0 up to n, return the remaining string."""
    return s[n:]

print(remove_from_start("Hello, World!", 7))  # "World!"
print(remove_from_start("abcdef", 3))          # "def"
print(remove_from_start("Python", 0))          # "Python"  (nothing removed)
print(remove_from_start("Python", 6))          # ""        (all removed)