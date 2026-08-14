from c3 import *

if __name__ == "__main__":
    best_score = 0
    best_key = ''
    best_decipherd_msg = ''
    best_line_num, line_num = 0, 0

    with open('./set1/input/4.txt', 'r') as f:
        for line in f:
            line_num += 1
            key, decipherd_msg, curr_score = xor_decipher(line.strip())
            if curr_score >= best_score:
                best_score = curr_score
                best_key = key
                best_decipherd_msg = decipherd_msg
                best_line_num = line_num
        
        print(f"The encrypted string is in line {best_line_num}.")
        print(f"The key is {best_key}.")
        print(f"The deciphered message is \"{best_decipherd_msg}\".")