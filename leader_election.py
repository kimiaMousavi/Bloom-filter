class leader_election():

  def __init__(self, list):

    self.l = list

  def select_leader(self):
    leader = sorted(self.l , key=lambda tup:tup[1],reverse=True )
    return leader[:3]
