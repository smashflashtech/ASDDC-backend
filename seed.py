from models import db, Group, Participant, Trial_Type, Set, Feedback

db.create_all()

groups = [Group(
  name = 'MET'
)]
groups.append(Group(
  name = 'EVOT'
))
groups.append(Group(
  name = 'PSVOT'
))

# db.session.add_all(groups) # passes the array in to "add all"
# db.session.commit() # commits the changes to the database

participants = [Participant( 
  dyad_L = 'A',
  dyad_N = 1,
  remedial = 'nope',
  date_of_participation = '2020-12-15; 10:33',
  notes = 'Test'
)]
participants.append(Participant(
  dyad_L = 'A',
  dyad_N = 2,
  date_of_participation = '2020-12-15; 10:33',
  notes = 'Test'
))
participants.append(Participant(
  dyad_L = 'I',
  dyad_N = 1,
  remedial = 'yep',
  date_of_participation = '2020-12-15; 10:33'
))
participants.append(Participant(
  dyad_L = 'I',
  dyad_N = 2,
  date_of_participation = '2020-12-15; 10:33',
))
participants.append(Participant(
  dyad_L = 'Q',
  dyad_N = 1,
  date_of_participation = '2020-12-15; 10:33'
))
participants.append(Participant(
  dyad_L = 'Q',
  dyad_N = 2,
  date_of_participation = '2020-12-15; 10:33'
))
# db.session.add_all(participants) 
# db.session.commit() # commits the changes to the database

#TRIAL TYPES
trial_types = []
##### ~~~ ~~~~ ~~~ ~~~ ~~~ AMTS
trial_types.append(Trial_Type(
  trial_code = 'aMTS01-S-bG'
))
trial_types.append(Trial_Type(
  trial_code = 'aMTS02-S-rG'
))
trial_types.append(Trial_Type(
  trial_code = 'aMTS03-S-pG'
))
trial_types.append(Trial_Type(
  trial_code = 'aMTS04-S-Gb'
))
trial_types.append(Trial_Type(
  trial_code = 'aMTS05-S-Gp'
))
trial_types.append(Trial_Type(
  trial_code = 'aMTS06-S-Gr'
))
trial_types.append(Trial_Type(
  trial_code = 'aMTS07-S-Pg'
))
trial_types.append(Trial_Type(
  trial_code = 'aMTS08-S-bP'
))
trial_types.append(Trial_Type(
  trial_code = 'aMTS09-S-Pr'
))
trial_types.append(Trial_Type(
  trial_code = 'aMTS10-S-rP'
))
trial_types.append(Trial_Type(
  trial_code = 'aMTS11-S-Br'
))
trial_types.append(Trial_Type(
  trial_code = 'aMTS12-S-rB'
))

##### ~~~ ~~~~ ~~~ ~~~ ~~~ DCT
trial_types.append(Trial_Type(
  trial_code = 'dct01-S-rbG'
))
trial_types.append(Trial_Type(
  trial_code = 'dct02-S-rGp'
))
trial_types.append(Trial_Type(
  trial_code = 'dct03-S-Gbp'
))
trial_types.append(Trial_Type(
  trial_code = 'dct04-S-rbP'
))
trial_types.append(Trial_Type(
  trial_code = 'dct05-S-Pbr'
))
trial_types.append(Trial_Type(
  trial_code = 'dct06-S-bPr'
))
trial_types.append(Trial_Type(
  trial_code = 'dct07-M-gbP'
))
trial_types.append(Trial_Type(
  trial_code = 'dct08-M-rPg'
))
trial_types.append(Trial_Type(
  trial_code = 'dct09-M-Pgb'
))
trial_types.append(Trial_Type(
  trial_code = 'dct10-M-brP'
))
trial_types.append(Trial_Type(
  trial_code = 'dct11-M-gBr'
))
trial_types.append(Trial_Type(
  trial_code = 'dct12-M-rpB'
))
trial_types.append(Trial_Type(
  trial_code = 'dct13-L-Bpg'
))
trial_types.append(Trial_Type(
  trial_code = 'dct14-L-gBp'
))
trial_types.append(Trial_Type(
  trial_code = 'dct15-L-pgB'
))
trial_types.append(Trial_Type(
  trial_code = 'dct16-L-gRb'
))
trial_types.append(Trial_Type(
  trial_code = 'dct17-L-bpR'
))
trial_types.append(Trial_Type(
  trial_code = 'dct18-L-Rgp'
))

##### ~~~ ~~~~ ~~~ ~~~ ~~~ SDisc
trial_types.append(Trial_Type(
  trial_code = 'sDiscT01-oP'
))
trial_types.append(Trial_Type(
  trial_code = 'sDiscT02-Po'
))
trial_types.append(Trial_Type(
  trial_code = 'sDiscT03-oP'
))
trial_types.append(Trial_Type(
  trial_code = 'sDiscT04-Po'
))
trial_types.append(Trial_Type(
  trial_code = 'sDiscT05-oP'
))
trial_types.append(Trial_Type(
  trial_code = 'sDiscT06-Po'
))
trial_types.append(Trial_Type(
  trial_code = 'sDiscT07-oP'
))
trial_types.append(Trial_Type(
  trial_code = 'sDiscT08-Po'
))
trial_types.append(Trial_Type(
  trial_code = 'sDiscT09-oP'
))
trial_types.append(Trial_Type(
  trial_code = 'sDiscT10-Po'
))
##### ~~~ ~~~~ ~~~ ~~~ ~~~ sPair
trial_types.append(Trial_Type(
  trial_code = 'sPairT01-p'
))
trial_types.append(Trial_Type(
  trial_code = 'sPairT02-p'
))
trial_types.append(Trial_Type(
  trial_code = 'sPairT03-o'
))
trial_types.append(Trial_Type(
  trial_code = 'sPairT04-p'
))
trial_types.append(Trial_Type(
  trial_code = 'sPairT05-p'
))
trial_types.append(Trial_Type(
  trial_code = 'sPairT06-o'
))
trial_types.append(Trial_Type(
  trial_code = 'sPairT07-p'
))
trial_types.append(Trial_Type(
  trial_code = 'sPairT08-p'
))
trial_types.append(Trial_Type(
  trial_code = 'sPairT09-o'
))
trial_types.append(Trial_Type(
  trial_code = 'sPairT10-p'
))
##### ~~~ ~~~~ ~~~ ~~~ ~~~ sPair
trial_types.append(Trial_Type(
  trial_code = 'tat-A'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-B'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-C'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-D'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-E'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-F'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-G'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-H'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-I'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-J'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-K'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-L'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-M'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-N'
))
trial_types.append(Trial_Type(
  trial_code = 'tat-O'
))
##### ~~~ ~~~~ ~~~ ~~~ ~~~ TSF
trial_types.append(Trial_Type(
  trial_code = 'tsft01-gB'
))
trial_types.append(Trial_Type(
  trial_code = 'tsft02-Bg'
))
trial_types.append(Trial_Type(
  trial_code = 'tsft03-Pg'
))
trial_types.append(Trial_Type(
  trial_code = 'tsft04-gP'
))
trial_types.append(Trial_Type(
  trial_code = 'tsft05-Rg'
))
trial_types.append(Trial_Type(
  trial_code = 'tsft06-gR'
))
trial_types.append(Trial_Type(
  trial_code = 'tsft07-pB'
))
trial_types.append(Trial_Type(
  trial_code = 'tsft08-Bp'
))
trial_types.append(Trial_Type(
  trial_code = 'tsft09-Rp'
))
trial_types.append(Trial_Type(
  trial_code = 'tsft10-pR'
))
trial_types.append(Trial_Type(
  trial_code = 'tsft11-Rb'
))
trial_types.append(Trial_Type(
  trial_code = 'tsft12-bR'
))

# SETS
sets = []
sets.append(Set(
  letter = '101'
))
sets.append(Set(
  letter = '102'
))
sets.append(Set(
  letter = '103'
))
sets.append(Set(
  letter = '104'
))
sets.append(Set(
  letter = '105'
))
sets.append(Set(
  letter = '106'
))
sets.append(Set(
  letter = '107'
))
sets.append(Set(
  letter = '108'
))
sets.append(Set(
  letter = '109'
))
sets.append(Set(
  letter = '110'
))
sets.append(Set(
  letter = '111'
))
sets.append(Set(
  letter = '112'
))
sets.append(Set(
  letter = '113'
))
sets.append(Set(
  letter = '114'
))
sets.append(Set(
  letter = '115'
))

#feedbacks
feedback=[]
feedback.append(Feedback(
  code = 'Yes'
))
feedback.append(Feedback(
  code = 'None'
))

# #MEGA SEED MENU
# db.session.add_all(groups)
# db.session.add_all(participants) 
# db.session.add_all(trial_types) 
# db.session.add_all(sets) 
# db.session.add_all(feedback) 

# db.session.commit() # commits the changes to the database