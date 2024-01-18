# Take input as date they want to store thier journal
todays_date = input("Enter the date: ")
# Take input of user mood
mood_of_day = int(input("How do you rate your mood today from 1 to 10? : "))

# Take notes
jounral_notes = input("Let's your thought flow:\n")
#Take that input and create a file under journal folder
with open(f"{todays_date}.txt",'w') as file:
    formatOfContent = f"Mood for the today: {mood_of_day} \nJournal Entries:\n {jounral_notes}"
    file.writelines(formatOfContent)
