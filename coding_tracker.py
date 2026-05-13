# Medical Coding Productivity Tracker
# Beginner GitHub project

coders = [
    {"name": "Asha Patel", "charts": 52, "hours": 8, "accuracy": 96},
    {"name": "Maria Lopez", "charts": 48, "hours": 7.5, "accuracy": 95},
    {"name": "Jennifer Smith", "charts": 60, "hours": 8, "accuracy": 98},
    {"name": "Nina Shah", "charts": 55, "hours": 8, "accuracy": 97},
    {"name": "Emily Brown", "charts": 50, "hours": 7, "accuracy": 94}
]

print("MEDICAL CODING PRODUCTIVITY REPORT")
print("----------------------------------")

for coder in coders:
    charts_per_hour = coder["charts"] / coder["hours"]

    print("Coder:", coder["name"])
    print("Charts coded:", coder["charts"])
    print("Hours worked:", coder["hours"])
    print("Accuracy:", str(coder["accuracy"]) + "%")
    print("Charts per hour:", round(charts_per_hour, 2))
    print("----------------------------------")