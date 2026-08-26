from binascii import hexlify, unhexlify

def ecb_detect(ciphertext):
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    return len(blocks) - len(set(blocks))

if __name__ == "__main__":
    with open('./set1/input/8.txt', 'r') as f:
        hex_lines = [line.strip() for line in f]

    ciphertexts = [unhexlify(h) for h in hex_lines]
    n_dup = [ecb_detect(ciphertext) for ciphertext in ciphertexts]
    max_idx, max_dup = max(enumerate(n_dup), key=lambda x: x[1])
    print(f"ECB encrypted: {hex_lines[max_idx]}")