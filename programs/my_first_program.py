from nada_dsl import *

def linear_congruential_generator(seed, multiplier, increment, modulus, n):
    result = seed
    for _ in range(n):
        result = (multiplier * result + increment) % modulus
    return result

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))  # Seed value
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))  # Multiplier value

    # Constants for the LCG as SecretIntegers
    increment = SecretInteger(Input(name="increment", party=party1))  # SecretInteger for increment
    modulus = SecretInteger(Input(name="modulus", party=party1))      # SecretInteger for modulus
    n = 10

    # Generate the pseudo-random number
    random_number = linear_congruential_generator(my_int1, my_int2, increment, modulus, n)

    # Output the pseudo-random number
    return [Output(random_number, "random_number_output", party1)]
