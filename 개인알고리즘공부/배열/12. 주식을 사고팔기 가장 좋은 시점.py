import sys

prices = list(map(int, input().split())) # [7, 1, 5, 3, 6, 4] -> 출력 : 5

max_price = 0 # 원래는 -sys.maxsize로 초기화해야하지만 빈 리스트가 들어올 수 있으므로 0으로 처리한다.
min_price = sys.maxsize # min_price(최소값)을 최대값으로 세팅
profit = 0 # 이익(최고점 - 최저점)

for price in prices:
    min_price = min(min_price, price) # min price보다 작은 price면 min_price 갱신
    profit = max(profit, price - min_price)
    
print(profit)
