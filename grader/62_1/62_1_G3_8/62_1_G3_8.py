n_party = int(input().strip())

parties = [input().strip() for _ in range(n_party)]

n_politicians = int(input().strip())

party_politicians = {party: [] for party in parties}
politician_votes = {}
politician_parties = {}
party_votes = {party: {"Y": 0, "N": 0, "X": 0} for party in parties}

for _ in range(n_politicians):
    politician, party = input().strip().split()
    party_politicians[party].append(politician)
    politician_votes[politician] = None
    politician_parties[politician] = party

n_vote = int(input().strip())

for _ in range(n_vote):
    politician, vote = input().strip().split()
    politician_votes[politician] = vote
    party_votes[politician_parties[politician]][vote] += 1

for party in parties:
    print(party)
    party_vote = party_votes[party]
    major_vote = {count: vote for vote, count in party_vote.items()}[
        max(party_vote.values())]

    if len([count for count in party_vote.values() if count != 0]) == 1:
        print("No cobra")
        continue

    if len([count for count in party_vote.values() if count == max(party_vote.values())]) > 1:
        print("Inconclusive")
        continue

    print(", ".join(sorted(politician for politician in party_politicians[party]
          if politician_votes[politician] != None and politician_votes[politician] != major_vote)))
