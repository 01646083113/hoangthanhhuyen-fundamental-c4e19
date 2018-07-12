bacterias = int(input("=====> How many B bacterias are there? "))
time = int(input("=====> How much time in minutes will we wait? "))
phase = int(input(" =====>> How many phase? "))

for i in range(phase):
    bacterias = bacterias*time
time = time*phase
print(" After {0} minutes, we would have {1} bacterias, through {2} phase !! ".format(time, bacterias, phase))