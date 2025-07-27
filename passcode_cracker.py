import time

# TODO: Move this to a config or CLI argument later
# For now, just hardcoding to something dumb/simple
LOCK_CODE = "8307"   # (don't tell anyone lol)

def code_matches(guess):
    """
    Check if the guess matches the lock's code.
    NOTE: Using zfill so '7' turns into '0007' - easier to compare.
    """
    # I thought about stripping spaces here, but nah, not needed.
    return str(guess).zfill(4) == LOCK_CODE


def brute_force_lock():
    """
    The laziest brute force ever: try 0000 through 9999 until we get it.
    Kinda silly, but hey... works fine for now.
    """
    start_time = time.time()
    attempts = 0

    # Could technically use itertools.product, but range is clearer here
    for candidate in range(10000):
        # increment attempts manually so it's more explicit
        attempts += 1
        padded_guess = str(candidate).zfill(4)  # ex: 5 → '0005'

        print(f"Trying code: {padded_guess}")  # Debug spam, can mute later

        if code_matches(padded_guess):
            # Stop timer here rather than after printing to keep timing accurate
            total_time = time.time() - start_time

            print("\n*** FOUND IT ***")
            print(f"Correct code is: {padded_guess}")
            print(f"Attempts made: {attempts}")
            print(f"Took about {round(total_time, 2)} seconds")
            break   # stop loop once we succeed

        # Adding a tiny sleep so output feels less like machine gun spam
        time.sleep(0.01)

    else:
        # This runs if we *never* hit break (shouldn't happen unless bug)
        print("Nope, none of the codes worked. Weird... check LOCK_CODE?")


if __name__ == "__main__":
    print("Starting brute-force attempt... (wish me luck!)\n")
    # Might refactor to allow custom codes via CLI later, for now just run it
    brute_force_lock()
