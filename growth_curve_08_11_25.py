import pandas as pd
import matplotlib.pyplot as plt

# Rebuild the dataset including the missing 4:55 and 6:26 entries,
# and ensure each row has an explicit time.
rows = [
    ("RM", "29:21",  -0.0016),
    ("30", "30:57",   0.0000),
    ("37", "31:25",  -0.0072),
    ("RM", "54:00",   0.0001),
    ("30", "55",      0.0089),
    ("37", "56",      -0.0002),
    ("RM", "1:23:14", 0.0025),
    ("30", "1:23:34", 0.0142),
    ("37", "1:23:34", 0.0012),
    ("RM", "1:58:11", -0.0004),
    ("30", "1:58:11", 0.0126),
    ("37", "1:58:11", 0.0011),
    ("RM", "2:30:00", 0.0009),
    ("30", "2:30:00", 0.0163),
    ("37", "2:30:00", -0.0001),
    ("RM", "3:09",    0.0032),
    ("30", "3:09",    0.0284),
    ("37", "3:09",    0.0022),
    ("RM", "3:45:00", 0.0016),
    ("30", "3:45:00", 0.0314),
    ("37", "3:45:00", 0.0055),
    ("RM", "4:55",    0.0027),
    ("30", "4:55",    0.0415),
    ("37", "4:55",    0.0365),
    ("RM", "6:26",   -0.0020),
    ("30", "6:26",    0.0608),
    ("37", "6:26",    0.1691),
]

df = pd.DataFrame(rows, columns=["Sample", "Time", "OD600"])

# Context-aware parser: 
# - "hh:mm:ss" -> hours, minutes, seconds
# - "mm:ss" (when first part >= 15) -> minutes, seconds (early measurements)
# - "hh:mm" (when first part <= 12 and we've already crossed 60 min previously) -> hours, minutes
def parse_time_series_to_minutes(times):
    mins = []
    seen_hour_format = False
    prev_min = None
    for t in times:
        parts = t.split(":")
        if len(parts) == 3:
            h, m, s = map(int, parts)
            total = h * 60 + m + s / 60.0
            seen_hour_format = True
        elif len(parts) == 2:
            a, b = map(int, parts)
            # Heuristic switch: if we've already seen hour-format or prev >= 60,
            # and the first part is plausibly an hour (<= 12), treat as hh:mm.
            if (seen_hour_format or (prev_min is not None and prev_min >= 60)) and a <= 12:
                total = a * 60 + b  # hh:mm
            else:
                total = a + b / 60.0  # mm:ss
        else:  # single number means minutes
            total = float(parts[0])
        mins.append(total)
        prev_min = total
    return mins

df["Time_min"] = parse_time_series_to_minutes(df["Time"].tolist())


# Plot each sample type
plt.figure(figsize=(8,6))
for sample in df["Sample"].unique():
    subset = df[df["Sample"] == sample]
    plt.plot(subset["Time_min"], subset["OD600"], marker='o', label=sample)

plt.xlabel("Time (minutes)")
plt.ylabel("OD600")
plt.title("OD600 Growth Curves")
plt.legend(title="Sample")
plt.grid(True)
plt.tight_layout()
plt.show()

