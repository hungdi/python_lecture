class SimulationController:
    def __init__(self, simulator, interaction_manager, spawner):
        self.simulator = simulator
        self.inter = interaction_manager
        self.spawner = spawner

    def run_day(self, users, day):
        print(f"\n===== Day {day} =====")
        for user in users:
            if user.status.alive:
                self.simulator.run_day(user)

        for user in users:
            if user.status.alive and user.job.job_name == "강도":
                self.inter.perform_robbery(user)

        self.spawner.spawn_if_needed(users)

        self.print_summary(users)

    def print_summary(self, users):
        print("\n[상태 요약]")
        for u in users:
            print(f"{u.user_name} | {u.job.job_name} | {u.summary()} | 감염: {u.status.infected} | 생존: {u.status.alive}")
