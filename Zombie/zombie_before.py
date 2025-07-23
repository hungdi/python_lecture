## 제출된 과제 버전 ##


import csv
import random

# 1. Start_member 불러오기 / Class 설정하기

# Start_member
def load_report(filepath):
    start_member = []
    with open(filepath, newline = '' , encoding = 'utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            fieldname = {'이름':row['name'],
                         '직업':row['class'],
                         '체력':int(row['health']),
                         '식량':int(row['food']),
                         '해독제':int(row['antidote']),
                         '감염':row['infected'].strip(),
                         '연속감염':0
                         }
            start_member.append(fieldname)
       
        #Class 설정하기
        random_sample = random.sample(range(1,len(start_member)+1),len(start_member))
        for idx, member in enumerate(start_member):
            role = random_sample[idx]

            if role <= 15:
                member['직업'] = '군인'
            elif role <= 18:
                member['직업'] = '의사'
            elif role <= 20:
                member['직업'] = '경찰'
            elif role <= 24:
                member['직업'] = '요리사'
            elif role == 25:
                member['직업'] = '강도'
            else:
                member['직업'] = '시민'

        #Class 별 체력 변경
        for member in start_member:
            if member['직업'] == '군인':
                member['체력'] = 120
            elif member['직업'] == '의사':
                member['체력'] = 80
            elif member['직업'] == '강도':
                member['체력'] = 60
                
    return start_member


# 2. 데일리 루틴 내용
def daily_routine(member_status):
    for status in member_status:
        
        # 2-1. 시민, 경찰, 요리사
        # 기본 체력 : 100
        # 일과 소모 체력 : 10
        # 식량 획득 확률 : 30%
        # 식량 획득 체력 : 15
        # 해독제 획득 확률 : 10%
        if status['직업'] in ['시민','경찰','요리사']:
            status['체력'] -= 10
            
            if random.random() <= 0.3:
                status['식량'] += 1
            
            if status['식량'] >= 1:
                if status['체력'] <= 85:
                    status['식량'] -= 1
                    status['체력'] += 15

            if random.random() <= 0.1:
                status['해독제'] += 1
            

        # 2-2. 군인
        # 기본 체력 : 120
        # 일과 소모 체력 : 15
        # 식량 획득 확률 : 50%
        # 식량 획득 체력 : 20
        # 해독제 획득 확률 : 10%
        if status['직업'] == '군인':
            status['체력'] -= 15

            if random.random() <= 0.5:
                status['식량'] += 1

            if status['식량'] >= 1:
                if status['체력'] <= 85:
                    status['식량'] -= 1
                    status['체력'] += 20
            
            if random.random() <= 0.1:
                status['해독제'] += 1

        # 2-3. 의사
        # 기본 체력 : 80
        # 일과 소모 체력 : 10
        # 식량 획득 확률 : 30%
        # 식량 획득 체력 : 15
        # 해독제 획득 확률 : 30%
        if status['직업'] == '의사':
            status['체력'] -= 10

            if random.random() <= 0.3:
                status['식량'] += 1

            if status['식량'] >= 1:
                if status['체력'] <= 65:
                    status['식량'] -= 1
                    status['체력'] += 15
            
            if random.random() <= 0.3:
                status['해독제'] += 1

        # 2-4. 강도
        # 기본 체력 : 60
        # 일과 소모 체력 : 20
        # 식량 획득 확률 : 10%
        # 식량 획득 체력 : 15
        # 해독제 획득 확률 : 5%
        if status['직업'] == '강도':
            status['체력'] -= 20

            if random.random() <= 0.1:
                status['식량'] += 1

            if status['식량'] >= 1:
                if status['체력'] <= 45:
                    status['식량'] -= 1
                    status['체력'] += 15
            elif status['식량'] >= 2:
                if status['체력'] <= 30:
                    status['식량'] -= 2
                    status['식량'] += 30
            
            if random.random() <= 0.05:
                status['해독제'] += 1
    return member_status


# 3. 경찰과 강도
def special_routine(member_status):
      
    # 3-1. 경찰 / 강도
    # 강도 출현
    robbers = [r for r in member_status if r['직업'] == '강도']
    if robbers:
        robber = robbers[0]
        print('강도가 나타났습니다.')
        victim_lst = [v for v in member_status if v['직업'] != '강도']
        victim = random.choice(victim_lst)
        i = random.randint(1,10)
        
        # 일반 피해자
        if victim['직업'] != '경찰':
            if i <= 2:
                if victim['식량'] >= 1:
                    robber['식량'] += 1
                    victim['식량'] -= 1
                    print(f"{robber['직업']}이 {victim['직업']} {victim['이름']}의 식량을 강탈했습니다.")
                else:
                    print(f"{robber['직업']}이 {victim['직업']} {victim['이름']}의 식량을 강탈하려 했으나 허탕입니다.")
            else:
                if victim['해독제'] >= 1:
                    robber['해독제'] += 1
                    victim['해독제'] -= 1
                    print(f"{robber['직업']}이 {victim['직업']} {victim['이름']}의 해독제를 강탈했습니다.")
                else:
                    print(f"{robber['직업']}이 {victim['직업']} {victim['이름']}의 해독제를 강탈하려 했으나 허탕입니다.")
    
            # 강도 검거
            for police in [p for p in member_status if p['직업'] == '경찰']:
                candidates = [c for c in member_status if c['직업'] != '경찰']
            
                if not candidates:
                    continue

                arrest = random.choice(candidates)

                if arrest['직업'] == '강도':
                    police['식량'] += arrest['식량']
                    police['해독제'] += arrest['해독제']
                    print(f"경찰 {police['이름']}님이 강도를 검거하고 사살하였습니다.")
                    member_status.remove(arrest)

                else:
                    print('오늘은 경찰이 강도를 발견하지 못하였습니다.')
        
        # 피해자가 경찰일 경우
        else:
            victim['식량'] += robber['식량']
            victim['해독제'] += robber['해독제']
            print(f"경찰 {victim['이름']}님이 강도를 검거하고 사살하였습니다.")
            member_status.remove(robber)
    
    return member_status


# 3. 감염 판단하기
def check_infected(member_status):

    for status in member_status:
        if status['직업'] == '요리사':
            if status['감염'] == 'False':
                status['연속감염'] = 0
                status['감염'] = str(bool(random.randint(0,1)))
                print(f"{status['이름']}이 감염되었습니다.")
            elif status['감염'] == 'True':
                if status['해독제'] >= 1:
                    status['해독제'] -= 1
                    status['감염'] = 'False'
                    status['연속감염'] = 0
                elif status['식량'] >= 1:
                    while status['감염'] == 'True' or status['식량'] > 0:
                        status['식량'] -= 1
                        status['감염'] = str(bool(random.randint(0,1)))
                        if status['감염'] == 'False':
                            status['연속감염'] = 0
                            print(f"{status['직업']} {status['이름']}님이 요리로 감염을 이겨냈습니다.")
                            break
                        elif status['식량'] == 0:
                            status['연속감염'] += 1
                            print(f"{status['직업']} {status['이름']}님이 감염을 이겨내려다 식량을 탕진하였습니다.")
            else:
                status['연속감염'] += 1

        else:
            if status['감염'] == 'False':
                status['연속감염'] = 0
                status['감염'] = str(bool(random.randint(0,1)))
                if status['감염'] == 'True':
                    print(f"{status['이름']}이 감염되었습니다.")

            elif status['감염'] == 'True':
                if status['해독제'] >= 1:
                    status['해독제'] -= 1
                    status['감염'] = 'False'
                    status['연속감염'] = 0
                else:
                    print(f"{status['이름']}이 감염되었습니다.")
                    status['연속감염'] += 1

    return member_status


# 4. 상태 확인 후 사망 판정하기
def check_death(member_status):
    dead_list = []
    print('아침이 되었습니다.')
    
    for status in member_status:
        if status['체력'] <= 0:
            print(f"{status['직업']} {status['이름']}님이 굶어 죽었습니다......")
            dead_list.append(status)

        elif status['직업'] == '의사':
            if status['연속감염'] == 6:
                print(f"{status['직업']} {status['이름']}님이 감염되어 죽었습니다......")
                dead_list.append(status)
        else:
            if status['연속감염'] == 4:
                print(f"{status['직업']} {status['이름']}님이 감염되어 죽었습니다......")
                dead_list.append(status)

    for dead in dead_list:
        member_status.remove(dead)

    return member_status


# 5. 리포트 저장하기
def save_report(savepath, status):
    save_field = ['name','class','health','food','antidote','infected']
    save_file = []
    for row in status:
         row = {'name':row['이름'],
                'class':row['직업'],
                 'health':int(row['체력']),
                 'food':int(row['식량']),
                 'antidote':int(row['해독제']),
                 'infected':row['감염'],
                 } 
         save_file.append(row)
        
    with open(savepath, 'w', newline = '' , encoding = 'utf-8') as f:
        writer = csv.DictWriter(f, fieldnames = save_field)
        writer.writeheader()
        writer.writerows(save_file)



# 6. main으로 연결
def main():
    day = int(input('시작 일을 입력하세요.(처음은 0): '))
    during_day = int(input('기간을 입력하세요(일): '))
    input_day = during_day
    if day == 0:
        filepath = 'D:\\git_desktop\\day_start_report.csv'
    else:  
        filepath = f'D:\\git_desktop\\day_{day}_report.csv'

    start = load_report(filepath)
    
    while during_day:
        during_day -= 1
        status = start
        status1 = daily_routine(status)
        status2 = special_routine(status1)
        status3 = check_infected(status2)
        end = check_death(status3)
        start = end           

    savepath = f'D:\\git_desktop\\day_{day+input_day}_report.csv'
    save_report(savepath, status)

if __name__ == '__main__':
    main()