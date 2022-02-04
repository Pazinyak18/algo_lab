from knut_morris import kmp
if __name__ == '__main__':
    s = "abcabeabcabcabdrabcabdtuyeabcabdwrt"
    sub = "abcabd"
    P = kmp(s, sub)
    print(P)
    for i in P:
        print(s[i:i + len(sub)])