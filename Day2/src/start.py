"""
Application entry point for the day2 project
"""

import random


def generate_otp():
    """Generates a 6-digit OTP"""
    import random

    otp = random.randint(100000, 999999)
    return otp


if __name__ == "__main__":
    otp = generate_otp()
    print("generate otp:", otp)
