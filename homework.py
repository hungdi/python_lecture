def main():
    # 영화 목록: {영화명: [평점1, 평점2, ...]}
    movies = {}

    def show_menu():
        print("\n==== 영화 평점 관리 ====")
        print("1. 영화 등록")
        print("2. 평점 추가")
        print("3. 전체 목록 조회")
        print("4. 영화별 평균 평점 조회")
        print("5. 종료")

    def add_movie():
        name = input("영화 이름 입력 >>> ")
        if name in movies:
            print("이미 등록된 영화입니다.")
        else:
            movies[name] = []
            print(f"영화 '{name}' 등록 완료")

    def add_rating():
        name = input("평점 추가할 영화 이름 >>> ")
        if name not in movies:
            print("영화가 등록되어 있지 않습니다.")
            return
        try:
            score = float(input("평점 (0~10) 입력 >>> "))
            if 0 <= score <= 10:
                movies[name].append(score)
                print(f"{name}에 평점 {score} 추가 완료")
            else:
                print("0~10 범위로 입력하세요.")
        except ValueError:
            print("숫자만 입력하세요.")

    def show_movies():
        if not movies:
            print("등록된 영화가 없습니다.")
            return
        print("\n=== 영화 목록 ===")
        for name, ratings in movies.items():
            print(f"{name}: {ratings}")

    def show_average():
        name = input("평균 평점을 조회할 영화 이름 >>> ")
        if name not in movies:
            print("영화가 등록되어 있지 않습니다.")
            return
        if not movies[name]:
            print("평점이 없습니다.")
            return
        avg = sum(movies[name]) / len(movies[name])
        print(f"{name} 평균 평점: {avg:.2f}")

    while True:
        show_menu()
        choice = input("선택 >>> ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            add_rating()
        elif choice == '3':
            show_movies()
        elif choice == '4':
            show_average()
        elif choice == '5':
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()