from tensor_intro_to_python.is_prime import is_prime


def prime_numbers(num, i=2):
    while i <= num:
        if is_prime(i):
            print(i)
            i += 1
        else:
            i += 1
    return 'Finish!'
