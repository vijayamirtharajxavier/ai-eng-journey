def min_max(names: list[str]) -> tuple[str, str]:
    """Return the shortest and longest names."""
    return min(names, key=len), max(names, key=len)


def main() -> None:
    hl7_segments = ["MSH", "PID", "EVN", "PV1", "PID"]

    # Task 2: unique segments via a set
    unique = sorted(set(hl7_segments))
    print(f"Unique segments: {unique}")

    # Task 3: dict comprehension
    lengths = {segment: len(segment) for segment in hl7_segments}
    print(f"Segment lengths: {lengths}")

    # Task 4: tuple return + unpacking
    names = ["MSH", "PID", "EVNR", "PV1", "PID"]
    shortest, longest = min_max(names)
    print(f"Shortest: {shortest}, Longest: {longest}")

    # Task 5: list comprehension with a filter

    p_segments = [s for s in hl7_segments if s.startswith("P")]
    print(f"Segments starting with 'P': {p_segments}")
    p_segments_unique = list(dict.fromkeys(p_segments))
    print(f"5 Unique segments starting with 'P': {p_segments_unique}")


if __name__ == "__main__":
    main()
