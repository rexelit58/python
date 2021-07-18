from pathlib import Path
path=Path()
# #searching a specific file
# for file in path.glob("*.py"):
#     print(file)

# searching all the file
for file in path.glob("*"):
    print(file)