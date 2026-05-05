# Lakshya Raj
# 202501100700096
# ECE-B

# Create CS4.txt file
file = open("CS4.txt", "w")
file.write("""INFO User login successful
WARNING Low disk space
ERROR File not found
INFO Payment completed
WARNING Battery low
ERROR Network issue
INFO Logout successful""")
file.close()


# ---------------- Task 1: Basic File Reading ----------------
file = open("CS4.txt", "r")

# read()
content = file.read()
print("Full Content:\n", content)

lines = content.split("\n")

print("Total number of lines:", len(lines))

print("\nFirst 2 lines:")
print("\n".join(lines[:2]))

print("\nLast 2 lines:")
print("\n".join(lines[-2:]))

file.close()


# readline()
file = open("CS4.txt", "r")
print("\nUsing readline():")
print(file.readline())
print(file.readline())
file.close()


# readlines()
file = open("CS4.txt", "r")
print("\nUsing readlines():")
print(file.readlines())
file.close()


# ---------------- Task 2: Log Classification ----------------
file = open("CS4.txt", "r")
lines = file.readlines()

count_dict = {"INFO":0, "WARNING":0, "ERROR":0}

for line in lines:
    if "INFO" in line:
        count_dict["INFO"] += 1
    if "WARNING" in line:
        count_dict["WARNING"] += 1
    if "ERROR" in line:
        count_dict["ERROR"] += 1

print("\nLog Count:", count_dict)

file.close()


# ---------------- Task 3: Write Filtered Files ----------------
info_file = open("info_logs.txt", "w")
warning_file = open("warning_logs.txt", "w")
error_file = open("error_logs.txt", "w")

for line in lines:
    if "INFO" in line:
        info_file.write(line)

    if "WARNING" in line:
        warning_file.write(line)

    if "ERROR" in line:
        error_file.write(line)

info_file.close()
warning_file.close()
error_file.close()

print("\nFiltered files created successfully")


# ---------------- Task 4: Search Feature ----------------
keyword = input("\nEnter keyword to search: ")

file = open("CS4.txt", "r")
lines = file.readlines()

result = []

print("\nMatching lines:")
for line in lines:
    if keyword in line:
        print(line.strip())
        result.append(line)

file.close()

# Save results
res_file = open("search_result.txt", "w")
res_file.writelines(result)
res_file.close()

print("Search results saved successfully")


# ---------------- File Pointer (seek) Operations ----------------
file = open("CS4.txt", "rb")   # binary mode for negative seek

print("\nFirst 50 characters:")
print(file.read(50).decode())

# Beginning
file.seek(0)
print("\nAfter seek(0):")
print(file.read(50).decode())

# Middle
file.seek(len(content)//2)
print("\nFrom middle:")
print(file.read(50).decode())

# Last 100 characters
file.seek(-100, 2)
print("\nLast 100 characters:")
print(file.read().decode())

file.close()