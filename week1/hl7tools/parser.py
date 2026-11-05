def split_segments(message: str) -> list[str]:
    """Split an HL7 message into segments."""
    # print(message)
    return message.strip().split("\r")


def segment_types(*segments: str) -> set[str]:
    """Return a set of unique segment types."""
    return {segment.split("|")[0] for segment in segments}


def describe(segment_type: str, **details) -> str:
    """Return a description of the segment type with details."""
    details_str = ", ".join(f"{key}={value}" for key, value in details.items())
    return f"{segment_type}: {details_str}"
