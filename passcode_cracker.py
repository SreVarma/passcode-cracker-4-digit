import time

# Just hardcoding this for now - will replace if we ever need it configurable
LOCK_CODE = "1234"  # Yeah, not very secure...

def does_code_match(code_guess):
    """
    Quick check to see if what we're trying matches the lock's code.
    Using zfill here so 7 becomes 0007, etc.
    """
    return str(code_guess).zfill(4) == LOCK_CODE


def try_break_lock():
    """
    Brute force attempt: literally try every number from 0 up to 9999.
    This isn't clever but hey, it works.
    """
    tries_count = 0
    time_started = time.time()

    # I could use itertools, but plain range is fine
    for attempt_num in range(0, 10000):  # Might as well make the bounds obvious
        tries_count += 1
        formatted = str(attempt_num).zfill(4)  # turning 5 -> '0005'

        print("Trying:", formatted)  # Debug spam - maybe remove later?

        if does_code_match(formatted):
            elapsed = time.time() - time_started
            print("\n*** Got it! Code is", formatted, "***")
            print("Took", tries_count, "attempts")
            print("Time spent (approx):", round(elapsed, 2), "seconds")
            break  # Found it, no need to keep looping
        else:
            # slight pause, feels more 'real'
            time.sleep(0.01)

    else:
        # Only runs if loop didn't break (so we failed)
        print("No luck cracking the code... something's off?")


if __name__ == "__main__":
    print("Okay, starting brute-force attempt now...")
    # note: might add CLI args later so code isn't hardcoded
    try_break_lock()
import time

# Just hardcoding this for now - will replace if we ever need it configurable
LOCK_CODE = "1234"  # Yeah, not very secure...

def does_code_match(code_guess):
    """
    Quick check to see if what we're trying matches the lock's code.
    Using zfill here so 7 becomes 0007, etc.
    """
    return str(code_guess).zfill(4) == LOCK_CODE


def try_break_lock():
    """
    Brute force attempt: literally try every number from 0 up to 9999.
    This isn't clever but hey, it works.
    """
    tries_count = 0
    time_started = time.time()

    # I could use itertools, but plain range is fine
    for attempt_num in range(0, 10000):  # Might as well make the bounds obvious
        tries_count += 1
        formatted = str(attempt_num).zfill(4)  # turning 5 -> '0005'

        print("Trying:", formatted)  # Debug spam - maybe remove later?

        if does_code_match(formatted):
            elapsed = time.time() - time_started
            print("\n*** Got it! Code is", formatted, "***")
            print("Took", tries_count, "attempts")
            print("Time spent (approx):", round(elapsed, 2), "seconds")
            break  # Found it, no need to keep looping
        else:
            # slight pause, feels more 'real'
            time.sleep(0.01)

    else:
        # Only runs if loop didn't break (so we failed)
        print("No luck cracking the code... something's off?")


if __name__ == "__main__":
    print("Okay, starting brute-force attempt now...")
    # note: might add CLI args later so code isn't hardcoded
    try_break_lock()
