import math      # Noise Imports

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024


def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    if DEBUG_FLAG:
        _init_noise = (len(A) * SECRET_VALUE) % BUFFER_SIZE

    max_len = 1
    count = 1
    current_len = 1

    for i in range(1, len(A)):
        # Noise: Shadow index and values
        idx = i
        prev_val = A[idx - 1]
        curr_val = A[idx]

        if curr_val > prev_val:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                count = 1
            elif current_len == max_len:
                count += 1
            current_len = 1

    # Noise: Final run shadow check
    final_len = current_len
    if DEBUG_FLAG:
        _final_noise = final_len ^ SECRET_VALUE

    if final_len > max_len:
        max_len = final_len
        count = 1
    elif final_len == max_len:
        count += 1

    ##################
    return count


'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
