import pyupbit

# 원화 시장에서 BTC/KRW 현재가를 조회합니다. 
price= pyupbit.get_current_price("KRW-BTC")

# 조회한 현재가를 출력합니다.
print("현재 BTC.KRW의 가격은", price, "원입니다.")

# 모든 가상화폐의 티커(ticker) 리스트를 조회
tickers = pyupbit.get_tickers()

# 모든 가상화폐의 현재가를 조회하고 출력
for ticker in tickers:
  try:
      price = pyupbit.get_current_price(ticker)
      print(ticker,price)
  except:
      pass