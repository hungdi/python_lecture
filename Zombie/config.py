"""게임 설정 상수"""

# 직업별 기본 스탯
JobStats = {
    "BASIC": {  # 시민/경찰/요리사 공통
        "hp": 100,
        "consume": 10,
        "food_prob": 0.3,
        "food_heal": 15,
        "antidote_prob": 0.1
    },
    "SOLDIER": {  # 군인
        "hp": 120,
        "consume": 15,
        "food_prob": 0.5,
        "food_heal": 20,
        "antidote_prob": 0.1
    },
    "DOCTOR": {  # 의사
        "hp": 80,
        "consume": 10,
        "food_prob": 0.3,
        "food_heal": 15,
        "antidote_prob": 0.3
    },
    "THIEF": {  # 강도
        "hp": 60,
        "consume": 20,
        "food_prob": 0.1,
        "food_heal": 15,
        "antidote_prob": 0.05
    }
}

# 감염 관련 설정
INFECTION_PROB = 0.5  # 감염 확률
InfectionDays = {
    "DEFAULT": 4,  # 일반 직업 최대 감염 일수
    "DOCTOR": 6    # 의사 최대 감염 일수
}

# 요리사 특수 능력
CHEF_CURE_PROB = 0.3  # 요리사의 식량으로 감염 치료 확률

# 강도/경찰 시스템
ROBBERY_FOOD_PROB = 0.2  # 식량 강탈 확률 (나머지는 해독제)
POLICE_ARREST_PROB = 0.3  # 경찰의 강도 체포 확률