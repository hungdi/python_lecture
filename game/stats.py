from collections import defaultdict

class KillCounter:
    def __init__(self, bus):
        self.total_kills = 0
        self.kills_by_kind = defaultdict(int)
        bus.on('MONSTER_KILLED', self.on_killed)

    def on_killed(self, data):
        is_boss = data.get('is_boss',False)
        kind = data.get('kind','unknown')

        add = 5 if is_boss else 1
        self.total_kills += add
