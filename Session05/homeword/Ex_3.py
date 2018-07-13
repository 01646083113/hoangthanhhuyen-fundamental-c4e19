bacterias = int(input("=====> How many B bacterias are there? "))
time = int(input("=====> How much time in minutes will we wait? "))
phase = int(input("=====> Enter the number phase : "))
phase = time // 2
total = bacterias * 2 ** (phase)
print ("After {0} minutes(s) we would have {1} B Bacterias".format(time, total))