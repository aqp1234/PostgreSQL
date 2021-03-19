import pandas as pd
tuninglist = ['concept.csv', 'condition_occurrence.csv', 'death.csv', 'drug_exposure.csv', 'person.csv', 'visit_occurrence.csv']
aftertuningname = ['concept2.csv', 'condition_occurrence2.csv', 'death2.csv', 'drug_exposure2.csv', 'person2.csv', 'visit_occurrence2.csv']
tuningcols = [
    ['concept_id', 'concept_name', 'domain_id'],
    ['person_id', 'condition_concept_id', 'condition_start_datetime', 'condition_end_datetime', 'visit_occurrence_id'],
    ['person_id', 'death_date'],
    ['person_id', 'drug_concept_id', 'drug_exposure_start_datetime', 'drug_exposure_end_datetime', 'visit_occurrence_id'],
    ['person_id', 'gender_concept_id', 'birth_datetime', 'race_concept_id', 'ethnicity_concept_id'],
    ['visit_occurrence_id', 'person_id', 'visit_concept_id', 'visit_start_datetime', 'visit_end_datetime']
    ]
for i in range(len(tuninglist)):
    df = pd.read_csv(tuninglist[i], usecols=tuningcols[i])
    df.to_csv(aftertuningname[i], sep=',')

