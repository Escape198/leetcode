def rabin_karp_search(text, pattern):
    result = []
    if not pattern:
        return result

    n = len(text)
    m = len(pattern)

    if n < m:
        return result

    def hash_func(s):
        return sum(ord(s[i]) * 31 ** (m - 1 - i) for i in range(m))

    pattern_hash = hash_func(pattern)
    window_hash = hash_func(text[:m])

    if pattern_hash == window_hash and text[:m] == pattern:
        result.append(0)

    for i in range(1, n - m + 1):
        window_hash = (window_hash - ord(text[i - 1]) * 31 ** (m - 1)) * 31 + ord(text[i + m - 1])

        if pattern_hash == window_hash and text[i:i + m] == pattern:
            result.append(i)

    return result


text = "ababcababcabcabc"
pattern = "abc"
print(f"Все вхождения подстроки '{pattern}' в строке '{text}':")
print(rabin_karp_search(text, pattern))
