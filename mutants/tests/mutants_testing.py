#!/usr/bin/env python3
"""Script to run mutation testing with mutmut and analyze survived mutants.

This script runs:
1. `uv run mutmut run`
2. `uv run mutmut results`
Then it parses the results for survived mutants, runs `uv run mutmut show`
for each to gather the diff, and writes all info directly to `tests/mutants.txt`.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

def run_command(cmd: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    """Run a system command and return the completed process."""
    return subprocess.run(cmd, shell=True, check=check, text=True, capture_output=True)

def main() -> None:
    # Ensure we are in the workspace root
    project_root = Path(__file__).resolve().parent.parent
    os.chdir(project_root)

    mutants_txt = Path("tests/mutants.txt")

    try:
        # Run mutmut run, inheriting stdout to print live progress to the console
        subprocess.run("uv run mutmut run", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Note: mutmut run completed with non-zero exit code: {e}", file=sys.stderr)
        # We continue because mutmut run returns non-zero when there are surviving mutants.

    try:
        # Run results in memory to capture the output list of mutants
        proc = run_command("uv run mutmut results")
        content = proc.stdout
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate mutants list: {e}", file=sys.stderr)
        sys.exit(1)

    # Find survived mutants
    # Format typically: "   isb.config.x_parse_languages__mutmut_6: survived"
    survived_matches = re.findall(r"(\S+):\s*survived", content)

    if not survived_matches:
        msg = "🎉 No surviving mutants found!"
        print(msg)
        mutants_txt.write_text(msg + "\n", encoding="utf-8")
        print(f"Result saved to {mutants_txt}")
        return

    analysis_results = []
    for i, mutant_name in enumerate(survived_matches):
        print(f"Getting info {i+1}/{len(survived_matches)} {mutant_name}...")
        separator = "=" * 80
        header = f"{separator}\nMUTANT: {mutant_name}\n"
        
        try:
            show_proc = run_command(f"uv run mutmut show {mutant_name}", check=False)
            diff_content = show_proc.stdout if show_proc.returncode == 0 else show_proc.stderr
            analysis_results.append(f"{header}{diff_content}\n")
        except Exception as e:
            analysis_results.append(f"{header}Failed to run mutmut show: {e}\n")

    # Save to output file
    mutants_txt.write_text("\n".join(analysis_results), encoding="utf-8")
    print(f"\nAnalysis complete. Detailed information saved directly to {mutants_txt}")

if __name__ == "__main__":
    main()
