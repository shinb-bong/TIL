n ,m = map(int,input().split())

def gcd(a,b):
    if a % b == 0 :
        return b
    return gcd(b,a%b)

print(m-gcd(n,m))

# 유클리드 호제법
# 최대 공약수를 구하고
# 두 수의 최대공약수의 N의 배수라는 것을 알고 있는 것에 착안

