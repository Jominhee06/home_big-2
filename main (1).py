import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from collections import Counter
from konlpy.tag import Komoran

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def preprocess(text):
  text = text.lower() # 소문자로 변환
  words = word_tokenize(text) # 단어 단위로 분리
  words = [word for word in words if word.isalpha()] # 알파벳으로 이루어진 단어만 추출
  stop_words = set(stopwords.words('english')) # 영어 불용어 목록 로드
  words = [word for word in words if not word in stop_words] # 불용어 제거
  return words
def count_words(words):
  word_counts = Counter(words)
  top_words = word_counts.most_common(10)
  return top_words
def tag_parts_of_speech(words):
  tagged_words = pos_tag(words)
  return tagged_words
# 사용자 입력 받기
text = input("Enter some text: ")
# 텍스트 전처리
words = preprocess(text)
# 단어 빈도수 계산
top_words = count_words(words)
print("Top 10 words:", top_words)
# 단어의 품사 태깅
tagged_words = tag_parts_of_speech(words)
print("Part of speech tagging:", tagged_words)
# Komoran 형태소 분석기 객체 생성
komoran = Komoran()
# 입력된 텍스트를 형태소 단위로 분석하고, 품사 태깅 수행
text = "오늘은 날씨가 좋아서 산책을 하고 싶습니다."
words = komoran.pos(text)
# 분석된 결과 출력
for word, pos in words:
print(word, "(", pos, ")")