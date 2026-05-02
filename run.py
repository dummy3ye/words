import subprocess
import sys

def run_command(command, shell=True):
    print(f"[*] Running: {command}")
    result = subprocess.run(command, shell=shell, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[!] Error running {command}:")
        print(result.stderr)
        return False
    print(result.stdout.strip())
    return True

def main():
    steps = [
        "node src/urls.js",
        "python src/main.py",
        "python src/semi.py",
        "python src/cleanup.py",
        "python src/parser.py"
    ]
    
    for step in steps:
        if not run_command(step):
            print("[!] Pipeline failed.")
            sys.exit(1)
            
    print("\n[+++] Full pipeline completed successfully!")
    print("[+++] Check the 'dist/' folder for results.")

if __name__ == "__main__":
    main()
