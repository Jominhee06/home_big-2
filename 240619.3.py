import pandas as pd
import requests

#################################
## 함수 정의
#################################
def get_stock_code():
    # 종목코드 다운로드 (encoding 설정 추가)
    stock_code = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0, encoding='euc-kr')[0]
    # 필요없는 column들은 제외
    stock_code = stock_code[['회사명', '종목코드']]
    
    # 한글 컬럼명을 영어로 변경
    stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'})
    
    # 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해줌
    stock_code.code = stock_code.code.map('{:06d}'.format)
    
    return stock_code

def get_stock(code):
    df_list = []
    for page in range(1, 21):
        # 일별 시세 url
        url = f'http://finance.naver.com/item/sise_day.nhn?code={code}&page={page}'
        print(url)
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        res = requests.get(url, headers=header)
        current_df = pd.read_html(res.text, header=0)[0]
        df_list.append(current_df)
    
    df = pd.concat(df_list, ignore_index=True)
    return df

def clean_data(df):
    # 결측값 있는 행 제거
    df = df.dropna()
    
    # 한글로 된 컬럼명을 영어로 바꿔줌
    df = df.rename(columns={'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})  
    
    # '보합' 문자열 처리 및 숫자 형식의 데이터에서 쉼표 제거
    df['close'] = df['close'].astype(str).str.replace(',', '').astype(float).astype(int)
    df['diff'] = df['diff'].astype(str).str.replace(',', '').str.replace('상승', '').str.replace('하락', '').str.replace('보합', '').astype(float).astype(int)
    df['open'] = df['open'].astype(str).str.replace(',', '').astype(float).astype(int)
    df['high'] = df['high'].astype(str).str.replace(',', '').astype(float).astype(int)
    df['low'] = df['low'].astype(str).str.replace(',', '').astype(float).astype(int)
    df['volume'] = df['volume'].astype(str).str.replace(',', '').astype(float).astype(int)
    
    # 컬럼명 'date'의 타입을 date로 바꿔줌
    df['date'] = pd.to_datetime(df['date'])
    
    # 일자(date)를 기준으로 오름차순 정렬
    df = df.sort_values(by=['date'], ascending=True)
    
    return df

#################################
## 함수 호출 및 CSV 저장
#################################
# 종목코드 가져오기
company = '삼성전자'
stock_code = get_stock_code()

# 일별 시세 가져오기
code = stock_code[stock_code.company == company].code.values[0].strip() # strip() : 공백제거
df = get_stock(code)

# 일별 시세 클린징
df = clean_data(df)

# 데이터 CSV 파일로 저장
df.to_csv('data.csv', index=False, encoding='utf-8-sig')
print("데이터가 data.csv 파일로 저장되었습니다.")

