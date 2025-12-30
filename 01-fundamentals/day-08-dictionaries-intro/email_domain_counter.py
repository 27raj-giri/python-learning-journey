emails = ["@gmail.com", "@gmail.com", "@yahoo.com", "@hotmail.com", "@yahoo.com"]
counts = {}

for email in emails:
    domain = email.split('@')[1]
    counts[domain] = counts.get(domain, 0) + 1

print(counts)
