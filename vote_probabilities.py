from scipy.special import comb

def critical_vote_probability(n):
    if (n > 1000) or (n < 2):
        print("Please input a number between 2 and 1,000")

    return comb(n, n/2) / (2 ** n)
