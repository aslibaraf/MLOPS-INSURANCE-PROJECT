from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
print(os.getenv("MongoDB_Password"))
from from_root import from_root

# Get the path to the root directory
root_path = from_root()
print(f"Root Directory: {root_path}")
from from_root import from_root
import os

# Access a file in the root directory
file_path = from_root("data", "example_file.txt")
print(f"Full File Path: {file_path}")

# Check if the file exists
if os.path.exists(file_path):
    print("File found!")
else:
    print("File not found!")
