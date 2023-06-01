print((int(int(input())**0.5)))

'''
소인수 분해 : a^x * b^y * ... * c^z -> (x + 1) * (y + 1) * ... * (z + 1) - 1
x, y, ..., z 중 어느 하나라도 홀수면 창문은 닫힌다.
x, y, ..., z 모두가 짝수일 때에만 창문이 열린다. -> 루트를 씌웠을 때 정수면 x, y, z가 모두 짝수임.
-> N보다 작은 수들 중 제곱 수를 찾는 문제
'''