import random

def generate_lotto():
    # 1부터 45까지의 숫자 중 6개를 중복 없이 무작위로 선택합니다.
    lotto_numbers = random.sample(range(1, 46), 6)
    
    # 번호를 보기 좋게 정렬합니다.
    lotto_numbers.sort()
    
    print("=== 오늘의 행운 번호 ===")
    print(f"번호: {lotto_numbers}")
    print("==========================")

if __name__ == "__main__":
    generate_lotto()