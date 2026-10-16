"""Data generators. Every generator accepts an optional `seed` so a failing test can be re-run
with exactly the same data. Use a PRIVATE generator: rng = random.Random(seed)
(never random.seed(...), which would change the global random state for everyone)."""
import random
import string

PRIORITIES = ("Low", "Medium", "High")
STATUSES = ("New", "Passed", "Failed")


def generate_username(prefix="user", length=4, seed=None):
    """Return a username like 'user4821': prefix followed by `length` random digits."""
    # TODO: rng = random.Random(seed); join rng.choice(string.digits) `length` times
    
    rng = random.Random(seed)
    username = prefix + ''.join(rng.choice(string.digits) for _ in range(length))
    
    return username


def generate_usernames(count, seed=None):
    """Return a list of `count` UNIQUE usernames like 'user4821' (count must be 9000 or less)."""
    # TODO: rng + a list + a set `seen`; a while loop until you have `count` unique names
    
    rng = random.Random(seed)
    usernames = []
    seen = set()

    while len(usernames) < count:
        username = generate_username(seed = rng.randint(0, 1000000))

        if username not in seen:
            usernames.append(username)
            seen.add(username)

        if len(seen) >= 9000:
            return False

    return usernames


def generate_password(length=12, seed=None):
    """Return a random password of exactly `length` characters (assume length >= 4)
    that always contains an uppercase letter, a lowercase letter and a digit.
    FOR TEST DATA ONLY: random is not secure."""
    # TODO: rng; start with one upper, one lower, one digit; fill up with a loop; rng.shuffle; join
    
    rng = random.Random(seed)

    

    d = rng.choice(string.digits)
    char = rng.choice(string.ascii_uppercase + string.ascii_lowercase) + d
    
    while len(char) < length:
        
        # if char.isupper():
        #     upper = True
        # elif char.islower():
        #     lower = True
        # elif char.isdigit():
        #     digit = True

        char += (rng.choice(string.ascii_letters))

    
    return char


def generate_test_id(number, prefix="TC", digits=3):
    """Return a zero-padded test ID: generate_test_id(7) -> 'TC-007'."""
    # TODO: str(number), then pad with '0' * (digits - len(text))
    
    return f"{prefix}-{number:0{digits}}"


def make_test_case(test_id, name, **options):
    """Return a NEW test-case dict with defaults, overridden/extended by keyword options.

    Defaults: priority 'Medium', status 'New', duration 0.0.
    make_test_case('TC-001', 'Login', priority='High', browser='Chrome') adds/overrides keys.
    """
    # TODO: build the defaults dict, then case.update(options); return case
    test_case = {"id": test_id, "name": name, "priority": "Medium", "status": "New", "duration": 0.0}

    test_case.update(options)
    return test_case


def generate_test_cases(count, seed=None):
    """Return `count` test-case dicts with IDs TC-001, TC-002, ... and names 'Test case 1', ...

    priority and status are random picks from PRIORITIES / STATUSES;
    duration is a random value from 0.10 to 5.00 seconds (2 decimals).
    """
    # TODO: rng = random.Random(seed); loop number in range(1, count + 1); reuse generate_test_id and make_test_case
    test_cases = []
    rng = random.Random(seed)

    for number in range(1, count + 1):
        test_id = generate_test_id(number)
        name = f"Test case {number}"
        priority = rng.choice(PRIORITIES)
        status = rng.choice(STATUSES)
        duration = round(rng.uniform(0.10, 5.00), 2)

        test_cases.append(make_test_case(test_id, name, priority=priority, status=status, duration=duration))

    return test_cases
