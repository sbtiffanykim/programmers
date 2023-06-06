def solution(bin1, bin2):
    squared = [2 ** i for i in range(0, 11)]
    bin1_to_decimal = sum([int(n) * squared[i] for i, n in enumerate(bin1[::-1])])
    bin2_to_decimal = sum([int(n) * squared[i] for i, n in enumerate(bin2[::-1])])
    
    return bin(bin1_to_decimal+bin2_to_decimal)[2:]