from functions.get_file_content import get_file_content
import os

def main():
    print("Testing get_file_content function...")
    
    # Test 1: lorem.txt truncation
    print("\n--- Test 1: lorem.txt truncation ---")
    content = get_file_content("calculator", "lorem.txt")
    print(f"Content length: {len(content)}")
    if "[...File" in content and "truncated at" in content:
        print("Truncation message found.")
        print("Last 100 chars:", content[-100:])
    else:
        print("Truncation message NOT found.")

    # Test 2: main.py
    print("\n--- Test 2: calculator/main.py ---")
    print(get_file_content("calculator", "main.py"))

    # Test 3: pkg/calculator.py
    print("\n--- Test 3: calculator/pkg/calculator.py ---")
    print(get_file_content("calculator", "pkg/calculator.py"))

    # Test 4: /bin/cat (should error) 
    print("\n--- Test 4: /bin/cat ---")
    print(get_file_content("calculator", "/bin/cat"))

    # Test 5: pkg/does_not_exist.py (should error)
    print("\n--- Test 5: calculator/pkg/does_not_exist.py ---")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()
