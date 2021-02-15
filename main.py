nominee_1 = input("enter the nominee 1 name: ")
nominee_2 = input("enter the nominee 2 name: ")

nom_1_votes = 0
nom_2_votes = 0

voters_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_of_voter = len(voters_id)

while True:
    if voters_id == []:
        print("voting session over")
        if nom_1_votes>nom_2_votes:
            percent = (nom_1_votes/num_of_voter) * 100
            print(f"{nominee_1} has won the vote by {percent}% vote")
            break

        elif nom_1_votes<nom_2_votes:
            percent = (nom_2_votes/num_of_voter) * 100
            print(f"{nominee_2} has won the vote by {percent}% vote")
            break

        else:
            print(f"Its a tie between {nominee_1} and {nominee_2}")

    else:
        voter = int(input("enter your voter id no : "))
        if voter in voters_id:
            print("you are a voter")
            voters_id.remove(voter)
            vote = int(input("enter your vote 1 0r 2: "))
            if vote == 1:
                nom_1_votes += 1
                print("thankyou for casting your vote")
            elif vote == 2:
                nom_2_votes += 1
                print("thankyou for casting your vote")
            else:
                print("Vote between candidate 1 or 2")
        else:
            print("you are not a voter or you have already voted")
