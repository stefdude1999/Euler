import sys
from pathlib import Path

# Add the parent directory to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from CommonFunctions.sieve import prime_sieve

print(sum(prime_sieve(2000000)))