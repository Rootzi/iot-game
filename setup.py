import sys
import subprocess
import os

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

setupcwd=os.getcwd()
