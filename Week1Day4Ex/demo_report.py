"""Integration script: uses the whole library. Run with: python3 demo_report.py"""
from test_utils.generators import generate_test_cases
from test_utils.helpers import sort_cases, slowest, count_by
from test_utils.decorators import timer


@timer
def build_demo_report(count=6, seed=7):
    """Return a multi-line report string (assume count >= 1).

    Line 1: 'TEST DATA REPORT'
    Line 2: 'Total: <count>'
    Line 3: 'Slowest: <id> (<duration:.2f> s)'
    Line 4: 'By priority: High=2, Low=1, Medium=3'   (priority names in alphabetical order)
    Then one line per case, slowest first: '<id> | <priority> | <status> | <duration:.2f> s'
    """
    # TODO (Milestone 5): cases = generate_test_cases(count, seed=seed); use slowest(), count_by(),
    #   sorted(counts) for the alphabetical priority names, and sort_cases(..., reverse=True).
    #   Build a list `lines`, then return "\n".join(lines).
    
    cases = generate_test_cases(count, seed=seed)

    slowest_case = slowest(cases)

    counts = count_by(cases, "priority")

    priority_parts = []
    
    for priority in sorted(counts):
        priority_parts.append(f"{priority}={counts[priority]}")

    priority_summary = ", ".join(priority_parts)

    sorted_cases = sort_cases(cases, "duration", reverse=True)

    lines = ["TEST DATA REPORT",
        f"Total: {count}",
        f"Slowest: {slowest_case['id']} ({slowest_case['duration']:.2f} s)",
        f"By priority: {priority_summary}"
    ]

    for case in sorted_cases:
        lines.append(f"{case['id']} | {case['priority']} | "f"{case['status']} | {case['duration']:.2f} s")

    return "\n".join(lines)


if __name__ == "__main__":
    print(build_demo_report())
