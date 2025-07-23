import random
from config import ROBBERY_FOOD_PROB, POLICE_ARREST_PROB

class InteractionManager:
    def __init__(self, users, test_mode=False):
        self.users = users
        self.test_mode = test_mode
    
    def perform_robbery(self, robber):
        """강도 행동 수행"""
        if not self._can_rob(robber):
            return
            
        # 테스트 모드가 아닐 때만 경찰과의 조우를 처리
        if not self.test_mode:
            police = self._find_police()
            if police:
                # 경찰과 조우
                print(f"{robber.user_name}이(가) 경찰과 마주쳤습니다!")
                if random.random() < POLICE_ARREST_PROB:
                    self._arrest_robber(robber, police)
                    return
                print(f"{robber.user_name}이(가) 경찰의 체포를 피해 도주했습니다.")
        
        # 일반인 대상 강탈 시도
        victim = self._get_civilian_victim(robber)
        if not victim:
            return
            
        print(f"{robber.user_name}이(가) {victim.user_name}에게 강탈 시도!")
        
        # 식량 또는 해독제 강탈 시도
        if random.random() < ROBBERY_FOOD_PROB:
            # 식량 강탈 시도
            if victim.food.has():
                victim.food.take()
                robber.food.give()
                print(f"{robber.user_name}이(가) {victim.user_name}에게서 식량을 강탈했습니다.")
            else:
                print(f"{victim.user_name}에게서 뺏을 식량이 없습니다.")
                return
        else:
            # 해독제 강탈 시도
            if victim.antidote.has():
                victim.antidote.take()
                robber.antidote.give()
                print(f"{robber.user_name}이(가) {victim.user_name}에게서 해독제를 강탈했습니다.")
            else:
                print(f"{victim.user_name}에게서 뺏을 해독제가 없습니다.")
                return
    
    def _find_police(self):
        """경찰 찾기"""
        police_list = [u for u in self.users if u.alive and self._is_police(u)]
        return police_list[0] if police_list else None
    
    def _get_civilian_victim(self, robber):
        """일반인 피해자 선택"""
        candidates = [u for u in self.users 
                     if u.alive and u != robber and not self._is_police(u)]
        return random.choice(candidates) if candidates else None
    
    def _rob_civilian(self, robber, victim):
        """일반인 강탈"""
        if random.random() < ROBBERY_FOOD_PROB:
            if victim.food.has():
                victim.food.take()
                robber.food.give()
                print(f"{robber.user_name}이(가) {victim.user_name}에게서 식량을 강탈했습니다.")
            else:
                print(f"{victim.user_name}에게서 뺏을 식량이 없습니다.")
        else:
            if victim.antidote.has():
                victim.antidote.take()
                robber.antidote.give()
                print(f"{robber.user_name}이(가) {victim.user_name}에게서 해독제를 강탈했습니다.")
            else:
                print(f"{victim.user_name}에게서 뺏을 해독제가 없습니다.")
    
    def _arrest_robber(self, robber, police):
        """강도 체포 처리"""
        # 강도의 모든 자원을 경찰에게 이전
        self._transfer_all_resources(robber, police)
        # 강도 사망 처리
        robber.health = 0
        robber.alive = False
        print(f"경찰 {police.user_name}이(가) 강도를 검거하고 사살했습니다.")
    
    def _transfer_all_resources(self, from_user, to_user):
        """모든 자원 이전"""
        if from_user.food.has():
            to_user.food.give(from_user.food.amount)
            from_user.food.take(from_user.food.amount)
        if from_user.antidote.has():
            to_user.antidote.give(from_user.antidote.amount)
            from_user.antidote.take(from_user.antidote.amount)

    def _can_rob(self, user):
        """강도 행동 가능 여부 확인"""
        return user.alive and user.job.job_name == "강도"
    
    def _is_police(self, user):
        """경찰 여부 확인"""
        return user.job.job_name == "경찰"
