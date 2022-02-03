from datetime import datetime, timedelta




now = datetime.utcnow()

seconds = 5

in_seconds = now + timedelta(seconds=seconds)
txs = []

while datetime.utcnow() < in_seconds:
  txs.append(1)

print(len(txs)/seconds)