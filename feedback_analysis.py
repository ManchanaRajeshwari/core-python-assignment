def feedback_analysis(ratings):
    if not ratings:
        return "No ratings available to calculate feedback"
    total=len(ratings)
    sum=0
    for rating in ratings:
        if rating>=4:
            sum+=rating
        percentage=(sum/total)*100
        return percentage
ratings = list(map(int, input("Enter ratings (space-separated, values 1-5): ").split()))
print(f"Positive Feedback : {feedback_analysis(ratings)}%")