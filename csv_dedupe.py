"""Write a copy of a CSV with duplicate rows removed, order preserved."""

import csv
import sys


def dedupe(source, target):
    with open(source, newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.reader(handle))
    seen = set()
    kept = []
    for row in rows:
        key = tuple(row)
        if key not in seen:
            seen.add(key)
            kept.append(row)
    with open(target, "w", newline="", encoding="utf-8") as handle:
        csv.writer(handle).writerows(kept)
    print(f"{len(rows)} rows -> {len(kept)} unique rows written to {target}")


if __name__ == "__main__":
    dedupe(sys.argv[1], sys.argv[2])
