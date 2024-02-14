def min_time(stages, floor, simple_goal):






def my_answer():
    N = int(input())
    goal_patterns = []
    goal_flag = False
    simple_goal_time = 0

    floor = 1
    stages = []
    for i in range(N-1):
        stage = []
        stage = list(map(int, input().split()))
        simple_goal_time += stage[0]
        stages.append(stage)


    while goal_flag != True:
        stage_now = stages[floor]
        op1_time = stage_now[0]
        op2_time = stage_now[1]
        op1_next = floor + 1
        op2_next = stage_now[2]
        time = 0
        for op in [op1_time, op2_time]:
            time



    print(stages)
    print(simple_goal_time)


if __name__ == "__main__":
    my_answer()
