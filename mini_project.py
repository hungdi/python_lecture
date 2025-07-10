def main():
    # 하드코딩된 지출 데이터
    data = [    
        {'날짜': '2025-07-01', '지출금액': 12000, '카테고리': '식비', '상세내역': '점심'},
        {'날짜': '2025-07-02', '지출금액': 8000, '카테고리': '교통', '상세내역': '버스'},
        {'날짜': '2025-07-03', '지출금액': 15000, '카테고리': '식비', '상세내역': '저녁'},
    ]
    
    # print(data[0]['날짜'])

    # TODO: 카테고리 목록 표시
    def show_categories():
        categories = {entry['카테고리'] for entry in data}
        for category in categories:
            print(category)
        pass

    # TODO: 특정 카테고리의 총 지출 계산
    def sum_by_category(category):
        def filter_data():
            # 입력받은 카테고리만 추출해서
            # 총 지출을 계산
            return [entry['지출금액'] for entry in data if entry['카테고리']==category]
        
        amounts = filter_data()
        return sum(amounts)

    # 메뉴 루프
    while True:
        print("\n=== 지출 관리 ===")
        print("1. 카테고리 목록 보기")
        print("2. 카테고리별 지출 조회")
        print("3. 종료")
        choice = input("선택 >>> ")

        if choice == '1':
            show_categories()
        elif choice == '2':
            category = input("조회할 카테고리 입력 >>> ")
            total = sum_by_category(category)
            print(f"{category} 총 지출: {total:,}원")
        elif choice == '3':
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()