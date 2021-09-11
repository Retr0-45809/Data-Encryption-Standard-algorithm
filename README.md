# Data-Encryption-Standard-algorithm
Python code for encryption and decryption of text using DES algorithm
The Data Encryption Standard is a symmetric-key algorithm for the encryption of digital data.
In the first step, the 64 bit plain text block is handed over to an initial Permutation(IP) function.
The initial permutation is performed on plain text.
Then initial permutation(IP) produces two block halves;Left Plaintext(LPT) & Right Plaintext(RPT).
Now each LPT and RPT to go through 16 rounds of encryption process.
In the end, LPT and RPT are rejoined and a Final Permutation(FP) is performed on the combined block
The result of this process produces 64 bit cipher text.
