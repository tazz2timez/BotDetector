Python 3.14.3 (v3.14.3:323c59a5e34, Feb  3 2026, 11:41:37) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
# bot_detector.py
import sys
import subprocess

# Ensure pandas is installed
try:
    import pandas as pd
except ImportError:
    print("Pandas not found. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    import pandas as pd

# Sample dataset (self-contained, no external CSV needed)
data = {
    'IP_address': ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5'],
    'User_agent': ['Mozilla/5.0', 'Mozilla/5.0', 'Mozilla/5.0', 'Mozilla/5.0', 'Mozilla/5.0'],
    'Request_count': [5, 50, 3, 100, 2],
...     'Time_spent': [30, 300, 20, 600, 10],  # seconds
...     'Pages_visited': [5, 50, 3, 100, 2],
...     'Click_patterns': ['Normal', 'Rapid', 'Normal', 'Rapid', 'Normal'],
...     'Is_bot': ['No', 'Yes', 'No', 'Yes', 'No']
... }
... 
... # Load into pandas DataFrame
... df = pd.DataFrame(data)
... 
... # Bot detection function (enhanced scoring)
... def detect_bot(row):
...     score = 0
...     if row["Request_count"] > 40:
...         score += 1
...     if row["Click_patterns"].lower() == "rapid":
...         score += 1
...     if row["Time_spent"] < 15:
...         score += 1
...     if row["Pages_visited"] > 30 and row["Time_spent"] < 120:
...         score += 1
...     return "Yes" if score >= 2 else "No"
... 
... # Apply detection
... df["Detected_bot"] = df.apply(detect_bot, axis=1)
... 
... # Display results
... print("=== Bot Detection Results ===\n")
... print(df)
... 
... # Summary
... total_sessions = len(df)
... detected_bots = (df["Detected_bot"] == "Yes").sum()
... print("\n=== Summary ===")
... print(f"Total Sessions: {total_sessions}")
... print(f"Detected Bots: {detected_bots}")
... print(f"Detection Rate: {(detected_bots / total_sessions) * 100:.2f}%")
... 
... # Save results
... df.to_csv("bot_detection_results.csv", index=False)
