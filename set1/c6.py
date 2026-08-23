from binascii import hexlify, unhexlify
from base64 import b64decode, b64encode
from itertools import combinations
from c3 import *

def hamming_dist(b1, b2):
    """Compute the Hamming distance, which is the number of differing bits.

    >>> hamming_dist(b"this is a test", b"wokka wokka!!!")
    37
    """

    dist = 0

    bin1 = ''.join(format(i, '08b') for i in b1)
    bin2 = ''.join(format(i, '08b') for i in b2)

    for i, j in zip(bin1, bin2):
        if i != j:
            dist += 1

    return dist

def best_keysize(ciphertext, lower_bound, upper_bound):
    """Determine the keysize with the smallest normalized edit distance."""

    keysize_dic = {i: None for i in range(lower_bound, upper_bound + 1)}

    for k in list(keysize_dic.keys()):
        blocks = [
            ciphertext[: k],
            ciphertext[k: 2*k],
            ciphertext[2*k: 3*k],
            ciphertext[3*k: 4*k]
        ]
        dist = []
        for block1, block2 in combinations(blocks, 2):
            dist.append(hamming_dist(block1, block2) / k)

        keysize_dic[k] = sum(dist) / len(dist)
    
    keysize_lis_asc = sorted(keysize_dic, key=keysize_dic.get)

    return keysize_lis_asc[0]

def solver(keysize, ciphertext):
    """Find the key, and break the ciphered text."""

    # Break the text into blocks and transpose
    t_blocks = [ciphertext[i::keysize] for i in range(keysize)]
    t_blocks_hex = [hexlify(b) for b in t_blocks]
    key = [xor_decipher(h)[0] for h in t_blocks_hex]
    
    return key

if __name__ == "__main__":
    b64_text = open('./set1/input/6.txt', 'r').read()
    text = b64decode(b64_text)
    keysize = best_keysize(text, 2, 40)
    print(''.join(solver(keysize, text)))