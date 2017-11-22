#m5t2 - bug collector
#cti 110
#robert crawford
#10/9

def main():
    totalBugs = 0;
    week = range (1,8)
    for day in week:
        #ask user for today's bugs
        print("Enter the bugs collected day", day)
        todayBugs = int(input())
        #add today's to the total
        totalBugs = totalBugs + todayBugs
    print("Total bugs:", totalBugs)


main()
