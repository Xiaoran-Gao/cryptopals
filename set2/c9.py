def pkcs7_padding(text, blocksize):
    """Pad the text using PKCS#7 to a specific block length (a multiple of blocksize)."""

    padding_len = blocksize - len(text) % blocksize
    text += padding_len * bytes([padding_len])

    return text

if __name__ == "__main__":
    assert pkcs7_padding(b"YELLOW SUBMARINE", 20) == b"YELLOW SUBMARINE\x04\x04\x04\x04"