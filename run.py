from grade_fast.states.graded import Graded
from grade_fast.states.in_progress import InProgress
from grade_fast.states.initial import Initial
from grade_fast.states.invalid import Invalid
from grade_fast.states.node import Node
from grade_fast.states.returned import Returned
from grade_fast.states.submitted import Submitted


from grade_fast.graphs.assignment import Assignment

import pandas as pd
import numpy as np


# this is an example of aplication of the code
# Althoug the example bellow might not be best usage of the classes created here, 
# I am trying to use a dataframe (as suggested in the README file).
# as in the README file: "Data Frame Creation and Analysis (5 points)"

data = {
    "TeachersId": np.random.randint(1, 100, 1000),
    "Submitted": np.random.randint(0, 11, size=1000),
    "InProgress": np.random.randint(0, 11, size=1000),
    "Graded": np.random.randint(0, 11, size=1000),
}

df = pd.DataFrame(data)


assignments = []

for index, row in df.iterrows():
    assignments.append(Assignment([(Submitted, row['Submitted']), (InProgress, row['InProgress']), (Graded, row['Graded'])]).calculate_total_time())


    # pieces of code where I try implementing the transition
    # assignment.transition(row['Submitted'])
    # assignment.transition(row['InProgress'])
    # assignment.transition(row['Graded'])

df['assignment_time'] = assignments

print("The top 3 grading teachers based on the shortes grading time:")
print(df[['TeachersId', 'assignment_time']].groupby('TeachersId').mean().sort_values('assignment_time', ascending=True).head(3))
