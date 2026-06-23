# Fraud Detection Transaction Analysis
# Pattern Matching + Anomaly Detection

import time

# Sample transaction descriptions
transactions = [
    "PAYMENT AMAZON 5000",
    "TRANSFER TO XYZ 10000",
    "CASH WITHDRAWAL 2000",
    "TRANSFER TO UNKNOWN 50000",
    "PAYMENT NETFLIX 799",
    "TRANSFER TO UNKNOWN 75000",
    "PAYMENT SWIGGY 450",
    "TRANSFER TO UNKNOWN 90000"
]

# Fraud pattern to detect
fraud_pattern = "TRANSFER TO UNKNOWN"

print("FRAUD DETECTION TRANSACTION ANALYSIS")
print("------------------------------------")

# Start execution time
start = time.perf_counter()

fraud_count = 0

print("\nAnalyzing Transactions...\n")

for transaction in transactions:

    # Pattern Matching
    if fraud_pattern in transaction:
        print(transaction, " ---> Potential Fraud Detected")
        fraud_count += 1

# Simple Anomaly Detection
print("\nAnomaly Detection Results:")

for transaction in transactions:
    amount = int(transaction.split()[-1])

    # Threshold-based anomaly detection
    if amount > 30000:
        print(transaction, " ---> High Value Transaction Alert")

# End execution time
end = time.perf_counter()

print("\nTotal Fraudulent Transactions Detected:", fraud_count)

print("\nExecution Time:", end - start, "seconds")

print("\nAnalysis:")
print("- Pattern matching identifies suspicious transaction sequences.")
print("- Anomaly detection flags unusually high-value transactions.")
print("- Efficient algorithms improve real-time detection capability.")
print("- Scalable platforms such as Apache Spark can process millions of transactions.")