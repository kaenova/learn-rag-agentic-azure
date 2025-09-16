
import os
import subprocess

def main():
    # Get the directory where the script is located
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Launch Jupyter Notebook in that directory
    subprocess.run([".venv/bin/python3", "-m", "jupyter", "lab"], cwd=project_dir)

if __name__ == "__main__":
    main()
