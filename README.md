# Data-Encryption-Standard-algorithm

The Data Encryption Standard is a symmetric-key algorithm for the encryption of digital data.<br />
1) In the first step, the 64 bit plain text block is handed over to an initial Permutation(IP) function.<br />
2) The initial permutation is performed on plain text.<br />
3) Then initial permutation(IP) produces two block halves;Left Plaintext(LPT) & Right Plaintext(RPT).<br />
4) Now each LPT and RPT to go through 16 rounds of encryption process.<br />
5) In the end, LPT and RPT are rejoined and a Final Permutation(FP) is performed on the combined block<br />
6) The result of this process produces 64 bit cipher text.<br />
