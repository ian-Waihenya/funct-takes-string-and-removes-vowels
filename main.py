def disemvowel(string_):
    vowels = "AEIOUaeiou"  # List of vowels to be removed
    result = ''.join([char for char in string_ if char not in vowels])
    return result
