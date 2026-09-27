rules = [
    {
        "name": "Allow-Web-To-App-8080",
        "priority": 100,
        "source": "10.0.1.0/24",
        "destination": "10.0.2.0/24",
        "protocol": "TCP",
        "port": "8080",
        "action": "Allow"
    },
    {
        "name": "Allow-Web-ASG-To-App-8080",
        "priority": 120,
        "source": "asg-web",
        "destination": "asg-app",
        "protocol": "TCP",
        "port": "8080",
        "action": "Allow"
    }
]


def find_duplicates(rules):
    duplicates = []

    for i in range(len(rules)):
        for j in range(i + 1, len(rules)):
            rule1 = rules[i]
            rule2 = rules[j]

            if (
                rule1["source"] == rule2["source"]
                and rule1["destination"] == rule2["destination"]
                and rule1["protocol"] == rule2["protocol"]
                and rule1["port"] == rule2["port"]
                and rule1["action"] == rule2["action"]
            ):
                duplicates.append((rule1["name"], rule2["name"]))

    return duplicates


def find_asg_candidates(rules):
    candidates = []

    for rule in rules:
        if (
            rule["source"] == "10.0.1.0/24"
            and rule["destination"] == "10.0.2.0/24"
            and rule["protocol"] == "TCP"
            and rule["port"] == "8080"
            and rule["action"] == "Allow"
        ):
            candidates.append(rule["name"])

    return candidates


duplicates = find_duplicates(rules)
asg_candidates = find_asg_candidates(rules)


print("===================================")
print("     NSG RATIONALISATION REPORT")
print("===================================")

print("\nTotal Rules:", len(rules))

print("\nDuplicate Analysis:")
if duplicates:
    for rule1, rule2 in duplicates:
        print("Duplicate:", rule1, "<->", rule2)
else:
    print("No duplicate rules found.")

print("\nASG Rationalisation Analysis:")
if asg_candidates:
    for rule in asg_candidates:
        print("Candidate:", rule)
        print("Recommendation: Consider replacing the IP-based rule with ASG-based communication.")
else:
    print("No ASG replacement candidates found.")

print("\n===================================")
print("Analysis completed.")
print("===================================")