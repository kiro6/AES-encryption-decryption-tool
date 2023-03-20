import sys
import time
import argparse
s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

inv_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)


def sub_bytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = s_box[s[i][j]]


def inv_sub_bytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = inv_s_box[s[i][j]]


def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]


def inv_shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]


def add_round_key(s, k):
    for i in range(4):
        for j in range(4):
            s[i][j] ^= k[i][j]


def mix_columns(state):
    mix_column_matrix = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]

    new_state = [[0 for _ in range(4)] for _ in range(4)]

    for col in range(4):
        new_state[0][col] = (mix_column_matrix[0][0] * state[0][col]) ^ (mix_column_matrix[0][1] * state[1][col]) ^ (
                    mix_column_matrix[0][2] * state[2][col]) ^ (mix_column_matrix[0][3] * state[3][col])
        new_state[1][col] = (mix_column_matrix[1][0] * state[0][col]) ^ (mix_column_matrix[1][1] * state[1][col]) ^ (
                    mix_column_matrix[1][2] * state[2][col]) ^ (mix_column_matrix[1][3] * state[3][col])
        new_state[2][col] = (mix_column_matrix[2][0] * state[0][col]) ^ (mix_column_matrix[2][1] * state[1][col]) ^ (
                    mix_column_matrix[2][2] * state[2][col]) ^ (mix_column_matrix[2][3] * state[3][col])
        new_state[3][col] = (mix_column_matrix[3][0] * state[0][col]) ^ (mix_column_matrix[3][1] * state[1][col]) ^ (
                    mix_column_matrix[3][2] * state[2][col]) ^ (mix_column_matrix[3][3] * state[3][col])

    return new_state


def inv_mix_columns(state):
    inv_mix_column_matrix = [
        [0x0e, 0x0b, 0x0d, 0x09],
        [0x09, 0x0e, 0x0b, 0x0d],
        [0x0d, 0x09, 0x0e, 0x0b],
        [0x0b, 0x0d, 0x09, 0x0e]
    ]
    new_state = [[0 for _ in range(4)] for _ in range(4)]
    for col in range(4):
        new_state[0][col] = (inv_mix_column_matrix[0][0] * state[0][col]) ^ (
                    inv_mix_column_matrix[0][1] * state[1][col]) ^ (inv_mix_column_matrix[0][2] * state[2][col]) ^ (
                                        inv_mix_column_matrix[0][3] * state[3][col])
        new_state[1][col] = (inv_mix_column_matrix[1][0] * state[0][col]) ^ (
                    inv_mix_column_matrix[1][1] * state[1][col]) ^ (inv_mix_column_matrix[1][2] * state[2][col]) ^ (
                                        inv_mix_column_matrix[1][3] * state[3][col])
        new_state[2][col] = (inv_mix_column_matrix[2][0] * state[0][col]) ^ (
                    inv_mix_column_matrix[2][1] * state[1][col]) ^ (inv_mix_column_matrix[2][2] * state[2][col]) ^ (
                                        inv_mix_column_matrix[2][3] * state[3][col])
        new_state[3][col] = (inv_mix_column_matrix[3][0] * state[0][col]) ^ (
                    inv_mix_column_matrix[3][1] * state[1][col]) ^ (inv_mix_column_matrix[3][2] * state[2][col]) ^ (
                                        inv_mix_column_matrix[3][3] * state[3][col])
    return new_state


r_con = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)


def bytes2matrix(text):
    return [list(text[i:i + 4]) for i in range(0, len(text), 4)]


def matrix2bytes(matrix):
    return bytes(sum(matrix, []))


def xor_bytes(a, b):
    return bytes(i ^ j for i, j in zip(a, b))


def pad(plaintext):
    if (len(plaintext) % 16 == 0):
        return plaintext
    else:
        padding_len = 16 - (len(plaintext) % 16)
        padding = bytes([padding_len] * padding_len)
        return plaintext + padding


def unpad(plaintext):
    padding_len = plaintext[-1]
    if padding_len > 0:
        message, padding = plaintext[:-padding_len], plaintext[-padding_len:]
        if all(p == padding_len for p in padding):
            return message
    return plaintext


def split_blocks(message, block_size=16, require_padding=True):
    assert len(message) % block_size == 0 or not require_padding
    return [message[i:i + 16] for i in range(0, len(message), block_size)]


class AES:
    rounds_by_key_size = {16: 10, 24: 12, 32: 14}

    def __init__(self, master_key):

        assert len(master_key) in AES.rounds_by_key_size
        self.n_rounds = AES.rounds_by_key_size[len(master_key)]
        self._key_matrices = self._expand_key(master_key)

    def _expand_key(self, master_key):

        key_columns = bytes2matrix(master_key)
        iteration_size = len(master_key) // 4
        i = 1
        while len(key_columns) < (self.n_rounds + 1) * 4:

            word = list(key_columns[-1])

            if len(key_columns) % iteration_size == 0:
                word.append(word.pop(0))

                word = [s_box[b] for b in word]

                word[0] ^= r_con[i]
                i += 1
            elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:

                word = [s_box[b] for b in word]

            word = xor_bytes(word, key_columns[-iteration_size])
            key_columns.append(word)

        return [key_columns[4 * i: 4 * (i + 1)] for i in range(len(key_columns) // 4)]

    def encrypt_block(self, plaintext):

        assert len(plaintext) == 16

        plain_state = bytes2matrix(plaintext)

        add_round_key(plain_state, self._key_matrices[0])

        for i in range(1, self.n_rounds):
            sub_bytes(plain_state)
            shift_rows(plain_state)
            mix_columns(plain_state)
            add_round_key(plain_state, self._key_matrices[i])

        sub_bytes(plain_state)
        shift_rows(plain_state)
        add_round_key(plain_state, self._key_matrices[-1])

        return matrix2bytes(plain_state)

    def decrypt_block(self, ciphertext):

        assert len(ciphertext) == 16

        cipher_state = bytes2matrix(ciphertext)

        add_round_key(cipher_state, self._key_matrices[-1])
        inv_shift_rows(cipher_state)
        inv_sub_bytes(cipher_state)

        for i in range(self.n_rounds - 1, 0, -1):
            add_round_key(cipher_state, self._key_matrices[i])
            inv_mix_columns(cipher_state)
            inv_shift_rows(cipher_state)
            inv_sub_bytes(cipher_state)

        add_round_key(cipher_state, self._key_matrices[0])

        return matrix2bytes(cipher_state)


def text_encryption_decryption():
    # you can use this msg to test :  my secret msg!!!
    inputMessage = input("enter your message any legnth !! ")
    message = bytes(inputMessage, "cp437")
    # you can use this msg to test(256) : my secret key to encrypt msg!!!!
    # inputkey = input("enter your key  128,192,256 bits  ")
    key = b"\x07\xba\x8d\xb7)J\xc6\x7f;buH\x90\x87\xc4\x08\xb2\xe7\xfa\xdb'E\x10\xfe\x8a?y\xf7k|\x84\x98"
    aes = AES(key)
    padding = pad(message)
    list = split_blocks(padding)
    print("your full message  : ", message.decode("cp437"), "\n")
    cipherlist = []
    plainlist = []
    for i in list:
        ciphertext = aes.encrypt_block(i)
        plaintext = unpad(aes.decrypt_block(ciphertext))
        # added cp437 (IBM encoding) to print readable charctars
        # can remove  the decoding the output will be in hex
        #print("your block         : ", unpad(i).decode("cp437"))
        print("your block         : ", i)
        print("your cipher        : ", ciphertext)
        print("plaint text        : ", plaintext.decode("cp437"), "\n")


def encryption(plain_path , cipher_path , key ):
    with open(plain_path, 'rb') as file:
        pdf_bytes = file.read()
    key = bytes.fromhex(key)
    aes = AES(key)
    padding = pad(pdf_bytes)
    list = split_blocks(padding)
    cipherlist = []
    for i in list:
        ciphertext = aes.encrypt_block(i)
        cipherlist.append(ciphertext)
    concatenated_cipher_bytes = b''.join(cipherlist)

    with open(cipher_path, 'wb') as file:
        file.write(concatenated_cipher_bytes)


def decryption(cipher_path , plain_path , key):
    with open(cipher_path, 'rb') as file:
        pdf_bytes = file.read()
    key =bytes.fromhex(key)
    aes = AES(key)
    padding = pad(pdf_bytes)
    list = split_blocks(padding)
    plainlist = []
    for i in list:
        plaintext = aes.decrypt_block(i)
        plainlist.append(plaintext)
    concatenated_cipher_bytes = unpad(b''.join(plainlist))

    with open(plain_path, 'wb') as file:
        file.write(concatenated_cipher_bytes)



parser = argparse.ArgumentParser(description="AES tool using 128,192,256 key ECB mode")
parser.add_argument("-e" , "--encrypt" , type=str , metavar="" ,help="path to the file you want to encrypt")
parser.add_argument("-d" , "--decrypt" , type=str ,metavar="" , help="path to the file you want to decrypt")
parser.add_argument("-o" , "--output" , type=str ,metavar="" ,help="path to where you want the output to be")
parser.add_argument("-k" , "--key" , type=str ,metavar="" ,help="key 64,48,32 hexadecimal characters")
args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])


if (args is None) :
    parser.print_help()

if not (args.encrypt or args.decrypt  in sys.argv):
    parser.print_usage()
    print("ERROR : one of this arguments is required: -e/--encrypt or -d/--decrypt")
    exit(0)

if  (args.encrypt and args.decrypt  in sys.argv):
    parser.print_usage()
    print("ERROR : just one of this arguments is required: -e/--encrypt or -d/--decrypt")
    exit(0)

if  not (args.key in sys.argv):
    parser.print_usage()
    print("ERROR : is required: -k/--key")
    exit(0)

if  not (args.output in sys.argv):
    parser.print_usage()
    print("ERROR : is required: -o/--output")
    exit(0)

key  = args.key
if not (len(key) == 64 or len(key) == 48 or len(key) == 32 ) :
    parser.print_usage()
    print("ERROR : Enter a valid key size 64,48,32 hexadecimal characters")
    exit(0)



st = time.thread_time()
if args.encrypt :
    encryption(args.encrypt , args.output , key)
elif args.decrypt :
    decryption(args.decrypt , args.output , key )
fi = time.thread_time()
print( "time to finish : ", fi-st)
