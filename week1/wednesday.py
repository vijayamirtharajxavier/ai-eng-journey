from hl7tools.parser import describe, segment_types, split_segments

SAMPLE_MSG = "MSH|^~\\&|LAB|HOSP\rPID|1||12345||DOE^JOHN\rPV1|1|O\rOBX|1|NM|GLU||98\r"


def main() -> None:
    segments = split_segments(SAMPLE_MSG)
    for seg in segments:
        print(seg)

    types = segment_types(*segments)
    print(f"Segment types: {types}")

    for seg in segments:
        if seg.startswith("PID"):
            fields = seg.split("|")
            print(describe("PID", patient_id=fields[3], name=fields[5]))


if __name__ == "__main__":
    main()
