import os
import collections
import socket

# Define file paths
data_dir = "/home/data"
output_dir = os.path.join(data_dir, "output")
file1 = os.path.join(data_dir, "IF-1.txt")
file2 = os.path.join(data_dir, "AlwaysRememberUsThisWay-1.txt")
output_file = os.path.join(output_dir, "result.txt")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            words = f.read().lower().split()
        return collections.Counter(words)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return collections.Counter()

# Count words
count1 = count_words(file1)
count2 = count_words(file2)

# Compute required outputs
total_words1 = sum(count1.values())
total_words2 = sum(count2.values())
grand_total = total_words1 + total_words2

# Get the top 3 most frequent words
top_3_words1 = count1.most_common(3)
top_3_words2 = count2.most_common(3)

# Get IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Write results to output file
try:
    with open(output_file, 'w') as f:
        f.write(f"Total words in IF-1.txt: {total_words1}\n")
        f.write(f"Total words in AlwaysRememberUsThisWay-1.txt: {total_words2}\n")
        f.write(f"Grand total of words: {grand_total}\n")
        f.write(f"Top 3 words in IF-1.txt: {top_3_words1}\n")
        f.write(f"Top 3 words in AlwaysRememberUsThisWay-1.txt: {top_3_words2}\n")
        f.write(f"IP Address: {ip_address}\n")

    print("Successfully wrote to result.txt")
except Exception as e:
    print("Error writing to result.txt:", e)

# Print result.txt contents
if os.path.exists(output_file):
    with open(output_file, 'r') as f:
        print(f.read())
else:
    print("result.txt was not created.")
