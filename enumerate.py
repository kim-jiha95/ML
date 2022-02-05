# 1. open()을 이용해 stockcode.txt 텍스트 파일을 읽기모드로 열고, 파일 객체를 f에 저장하세요.
f = open('stockcode.txt', 'r')

# 2. readlines()을 이용해 stockcode.txt 파일의 내용을 원소로 갖고 있는 리스트를 lines에 저장하세요. 
lines = f.readlines()

# 3. 실행 버튼을 누르고 주석과 함께 코드를 이해해보세요.
# lines의 인덱스와 요소를 각각 line_num과 line에 순서대로 저장합니다.
for line_num, line in enumerate(lines):
    # 첫번째 반복문에서는 인덱스 0과 000020 동화약품 \n이 line에 저장됩니다.
    print('%d %s' %(line_num+1, line), end='')
# 파일을 닫습니다.
f.close()
