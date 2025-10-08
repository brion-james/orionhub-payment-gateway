#!/usr/bin/env python3
"""
Recreate the OrionHub payment gateway commit history with backdated commits.

Dates: 2025-10-07 to 2026-03-30
Times: between 22:00 and 02:59

Usage:
    python recreate_history.py /path/to/your/github/repo

If no path is given, it uses the current directory.
"""

import os
import random
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timedelta

# ============================================================
# CONFIG
# ============================================================

REPO_PATH = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

AUTHOR_NAME = "Brion James"
AUTHOR_EMAIL = "noxbot2005@gmail.com"

# Change this if you want the times to be local instead of UTC.
# Examples: "+0000", "+0530", "-0500"
TIMEZONE_OFFSET = "+0000"

PUSH_AT_END = False   # Set True if you want the script to run `git push`

TOTAL_COMMITS = 230

# ============================================================
# COMMIT MESSAGES
# ============================================================

commit_messages = [
    "Add payment transaction model",
    "Add transaction validation",
    "Improve payment request parsing",
    "Add gateway response handler",
    "Add transaction status constants",
    "Add payment provider configuration",
    "Update payment timeout",
    "Improve request logging",
    "Add payment error handling",
    "Add transaction identifier generation",
    "Improve validation error messages",
    "Add gateway health check",
    "Add payment provider client",
    "Refactor transaction creation",
    "Add transaction retry handling",
    "Update provider timeout",
    "Improve gateway logging",
    "Add failed transaction handling",
    "Add transaction status endpoint",
    "Improve API request validation",
    "Add currency validation",
    "Update payment configuration",
    "Add payment service tests",
    "Improve transaction test coverage",
    "Refactor provider client",
    "Add provider diagnostics",
    "Improve gateway error responses",
    "Add request correlation identifier",
    "Update transaction logging",
    "Improve API error handling",
    "Add transaction response formatter",
    "Refactor validation helpers",
    "Add gateway configuration loader",
    "Improve configuration validation",
    "Add development environment settings",
    "Update architecture notes",
    "Improve payment service structure",
    "Add transaction repository",
    "Refactor transaction service",
    "Add transaction lookup",
    "Improve lookup validation",
    "Add gateway request logging",
    "Update logging configuration",
    "Improve provider response parsing",
    "Add provider status mapping",
    "Refactor payment controller",
    "Improve controller validation",
    "Add transaction audit logging",
    "Update audit log format",
    "Improve transaction error reporting",
    "Add provider timeout handling",
    "Refactor gateway client",
    "Improve provider connection handling",
    "Add transaction cancellation support",
    "Update transaction status handling",
    "Improve cancellation validation",
    "Add payment gateway metrics",
    "Update gateway metrics",
    "Improve diagnostic logging",
    "Add service health diagnostics",
    "Refactor diagnostic helpers",
    "Update architecture documentation",
    "Improve deployment documentation",
    "Add local development instructions",
    "Update configuration examples",
    "Improve environment variable handling",
    "Add configuration defaults",
    "Refactor configuration loader",
    "Improve configuration errors",
    "Add request validation middleware",
    "Update API middleware",
    "Improve middleware logging",
    "Add request timing metrics",
    "Update request metrics",
    "Improve transaction performance",
    "Refactor transaction validation",
    "Add transaction schema checks",
    "Improve schema validation",
    "Add provider request formatter",
    "Update provider request format",
    "Improve provider compatibility",
    "Add provider error mapping",
    "Update provider error handling",
    "Improve retry behaviour",
    "Add retry backoff handling",
    "Update retry configuration",
    "Improve transaction recovery",
    "Add transaction recovery logging",
    "Refactor recovery service",
    "Improve recovery diagnostics",
    "Add payment gateway integration tests",
    "Update integration test fixtures",
    "Improve integration test coverage",
    "Add provider mock service",
    "Update provider mock responses",
    "Improve test utilities",
    "Refactor test helpers",
    "Add transaction edge case tests",
    "Improve validation test coverage",
    "Update payment service documentation",
    "Add API endpoint documentation",
    "Improve API examples",
    "Update deployment notes",
    "Add staging configuration",
    "Improve staging configuration",
    "Update production configuration template",
    "Add operational troubleshooting notes",
    "Improve troubleshooting documentation",
    "Add gateway maintenance script",
    "Update maintenance script",
    "Improve maintenance logging",
    "Add transaction cleanup utility",
    "Update cleanup utility",
    "Improve cleanup safety checks",
    "Add archive preparation notes",
    "Update archive documentation",
    "Review legacy dependencies",
    "Update dependency notes",
    "Improve package documentation",
    "Add release metadata",
    "Update release metadata",
    "Prepare version release",
    "Finalize release changes",
    "Update version information",
    "Improve release notes",
    "Add migration notes",
    "Update migration documentation",
    "Review payment provider integration",
    "Improve provider integration diagnostics",
    "Update gateway monitoring notes",
    "Add monitoring configuration",
    "Improve monitoring documentation",
    "Update operational runbook",
    "Review transaction logging",
    "Improve transaction audit records",
    "Update audit documentation",
    "Add legacy compatibility notes",
    "Improve compatibility handling",
    "Update compatibility documentation",
    "Review archived configuration",
    "Clean obsolete configuration entries",
    "Update archived project notes",
    "Prepare gateway archive",
    "Review legacy gateway structure",
    "Document remaining legacy components",
    "Update legacy component notes",
    "Prepare final archive review",
    "Review final repository contents",
    "Update final archive documentation",
    "Mark payment gateway for archival",
    "Archive OrionHub payment gateway",
]

# ============================================================
# HELPERS
# ============================================================

def run(cmd, cwd=REPO_PATH, env=None, check=True):
    subprocess.run(cmd, cwd=cwd, env=env, check=check)


def random_datetime_range():
    """Return a random datetime between 2025-10-07 and 2026-03-30,
    hour in [22, 23, 0, 1, 2] (10:00 PM – 2:59 AM)."""
    start = datetime(2025, 10, 7)
    end = datetime(2026, 3, 30)
    days = (end - start).days

    day = start + timedelta(days=random.randint(0, days))
    hour = random.choice([22, 23, 0, 1, 2])
    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    return day.replace(hour=hour, minute=minute, second=second, microsecond=0)


def make_sorted_dates(count):
    dates = [random_datetime_range() for _ in range(count)]
    dates.sort()
    return dates


def write_file(rel_path, content):
    path = REPO_PATH / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def append_file(rel_path, content):
    path = REPO_PATH / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(content)


def git_commit(message, body=None, allow_empty=False, commit_dt=None):
    if commit_dt is None:
        commit_dt = random_datetime_range()

    env = os.environ.copy()
    date_str = commit_dt.strftime(f"%Y-%m-%dT%H:%M:%S{TIMEZONE_OFFSET}")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    cmd = ["git", "commit"]
    if allow_empty:
        cmd.append("--allow-empty")
    cmd.extend(["-m", message])
    if body:
        cmd.extend(["-m", body])

    run(cmd, env=env)


# ============================================================
# MAIN
# ============================================================

def main():
    REPO_PATH.mkdir(parents=True, exist_ok=True)
    os.chdir(REPO_PATH)

    # Initialize git if needed
    if not (REPO_PATH / ".git").exists():
        run(["git", "init", "-b", "main"])

    run(["git", "config", "user.name", AUTHOR_NAME])
    run(["git", "config", "user.email", AUTHOR_EMAIL])

    # Total commits = 1 initial + 230 loop + 3 final
    total_commits = 1 + TOTAL_COMMITS + 3
    dates = make_sorted_dates(total_commits)
    date_iter = iter(dates)

    # --------------------------------------------------------
    # Initial project structure
    # --------------------------------------------------------

    for d in ["src", "config", "docs", "tests", "scripts", "assets", "lib"]:
        (REPO_PATH / d).mkdir(parents=True, exist_ok=True)

    write_file("README.md", """# OrionHub Payment Gateway

Legacy payment gateway integration used by the OrionHub platform.

## Status

This repository has been archived following the retirement of the
legacy OrionHub payment processing architecture.

## Components

- Payment request handling
- Transaction validation
- Gateway communication
- Internal API integration
- Logging and diagnostics

This project is no longer under active development.
""")

    write_file("src/payment.js", """const crypto = require("crypto");

function createTransaction(amount, currency) {
    return {
        id: crypto.randomUUID(),
        amount,
        currency,
        status: "pending"
    };
}

module.exports = {
    createTransaction
};
""")

    write_file("config/payment.conf", """[payments]
provider=orionpay
currency=LKR
timeout=5000
retry_count=3

[logging]
level=info
""")

    write_file("docs/architecture.md", """# OrionHub Payment Gateway Architecture

The legacy payment gateway sits between OrionHub and the external
payment provider.

OrionHub
    |
    v
Payment Gateway
    |
    v
OrionPay
    |
    v
Transaction Provider
""")

    write_file("tests/payment.test.js", """const assert = require("assert");

function validateAmount(amount) {
    return Number.isFinite(amount) && amount > 0;
}

assert.strictEqual(validateAmount(100), true);
assert.strictEqual(validateAmount(-1), false);
""")

    write_file("assets/README.txt", """Legacy OrionHub project assets.

Some historical assets were retained during archival.
""")

    write_file("lib/validator.js", """function validateTransaction(transaction) {
    if (!transaction) return false;
    if (!transaction.amount) return false;
    if (!transaction.currency) return false;

    return true;
}

module.exports = {
    validateTransaction
};
""")

    run(["git", "add", "-A"])
    git_commit(
        "Initialize OrionHub payment gateway",
        commit_dt=next(date_iter)
    )

    # --------------------------------------------------------
    # Realistic commit history
    # --------------------------------------------------------

    print(f"[+] Generating {TOTAL_COMMITS} commits...")

    for i in range(1, TOTAL_COMMITS + 1):
        idx = (i - 1) % len(commit_messages)
        message = commit_messages[idx]

        mod = i % 6
        if mod == 0:
            append_file("src/payment.js", f"// Maintenance revision {i}\n")
        elif mod == 1:
            append_file("config/payment.conf", f"# Configuration revision {i}\n")
        elif mod == 2:
            append_file("docs/architecture.md", f"- Documentation revision {i}\n")
        elif mod == 3:
            append_file("tests/payment.test.js", f"// Test revision {i}\n")
        elif mod == 4:
            append_file("assets/README.txt", f"Legacy maintenance note {i}\n")
        elif mod == 5:
            append_file("lib/validator.js", f"// Validation revision {i}\n")

        run(["git", "add", "-A"])

        # Flag fragment 1
        if i == 157:
            git_commit(
                "Review archived deployment identifier",
                "Historical reference fragment:\n\nEC\n\nContinue investigating related archive records.",
                commit_dt=next(date_iter)
            )
            continue

        # Flag fragment 2
        if i == 173:
            git_commit(
                "Inspect legacy deployment record",
                "Recovered reference fragment:\n\nLIP\n\nThe remaining archive material should be reviewed.",
                commit_dt=next(date_iter)
            )
            continue

        # Flag fragment 3
        if i == 191:
            git_commit(
                "Review final archived reference",
                "Recovered reference fragment:\n\nSE{shadow_profile}\n\nCombine the fragments recovered from the related archive records.",
                commit_dt=next(date_iter)
            )
            continue

        # Normal commit
        git_commit(message, commit_dt=next(date_iter))

    # --------------------------------------------------------
    # Historical C1 artifact
    # --------------------------------------------------------

    print("[+] Adding historical project artifact...")

    write_file("assets/legacy/README.txt", """Historical OrionHub deployment artifact.

Recovered from an archived development state.

This artifact is retained as part of the legacy investigation
and leads into the next challenge.
""")

    run(["git", "add", "-A"])
    git_commit(
        "Recover archived OrionHub deployment artifact",
        commit_dt=next(date_iter)
    )

    # --------------------------------------------------------
    # Final archive commits
    # --------------------------------------------------------

    write_file("docs/archive-status.md", """# Archive Status

Project: OrionHub Payment Gateway

Status: Discontinued

The OrionHub payment gateway was retained for historical and
migration purposes after the legacy payment architecture was retired.
""")

    run(["git", "add", "-A"])
    git_commit(
        "Document legacy project archive status",
        commit_dt=next(date_iter)
    )

    git_commit(
        "Remove internal development tooling",
        allow_empty=True,
        commit_dt=next(date_iter)
    )

    # --------------------------------------------------------
    # Done
    # --------------------------------------------------------

    print()
    print("============================================================")
    print(" DONE")
    print("============================================================")
    print(f"Repository: {REPO_PATH}")
    print()
    print("Push to GitHub with:")
    print("  git push -u origin main")
    print()

    if PUSH_AT_END:
        run(["git", "push", "-u", "origin", "main"])


if __name__ == "__main__":
    main()