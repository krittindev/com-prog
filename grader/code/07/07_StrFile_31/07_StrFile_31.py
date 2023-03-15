def reverseComplement(nucleotide):
    reversedNucleotide = ''
    for c in nucleotide:
        if c == 'A':
            reversedNucleotide += 'T'
        elif c == 'T':
            reversedNucleotide += 'A'
        elif c == 'G':
            reversedNucleotide += 'C'
        elif c == 'C':
            reversedNucleotide += 'G'
    reversedNucleotide = reversedNucleotide[::-1]
    return reversedNucleotide


def frequency(nucleotide):
    countA = sum(1 for c in nucleotide if c == 'A')
    countT = sum(1 for c in nucleotide if c == 'T')
    countG = sum(1 for c in nucleotide if c == 'G')
    countC = sum(1 for c in nucleotide if c == 'C')
    return 'A={}, T={}, G={}, C={}'.format(
        countA,
        countT,
        countG,
        countC
    )


def doublet(nucleotide, dualNucleotide):
    countDoublet = 0
    countDoublet = sum(
        1
        for i in range(len(nucleotide) - 1)
        if nucleotide[i] + nucleotide[i + 1] == dualNucleotide
    )
    return countDoublet


def isValidDNA(nucleotide):
    for c in nucleotide:
        if c not in 'ATGC':
            return False
    return True


nucleotide = input().strip().upper()
operator = input().strip().upper()
dualNucleotide = ''

if not isValidDNA(nucleotide):
    print('Invalid DNA')
elif operator == 'R':
    print(reverseComplement(nucleotide))
elif operator == 'F':
    print(frequency(nucleotide))
elif operator == 'D':
    dualNucleotide = input().strip().upper()
    print(doublet(nucleotide, dualNucleotide))
