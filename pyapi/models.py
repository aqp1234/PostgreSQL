from pyapi import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, unique=True)
    gender_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'), nullable=False)
    birth_datetime = db.Column(db.DateTime(), nullable=False)
    race_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'), nullable=False)
    ethnicity_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'), nullable=False)

class Visit_occurrence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visit_occurrence_id = db.Column(db.Integer, unique=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id', ondelete='CASCADE'))
    visit_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'))
    visit_start_datetime = db.Column(db.DateTime(), nullable=False)
    visit_end_datetime = db.Column(db.DateTime(), nullable=False)

class Condition_occurrence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id', ondelete='CASCADE'), nullable=False)
    condition_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'), nullable=False)
    condition_start_datetime = db.Column(db.DateTime(), nullable=False)
    condition_end_datetime = db.Column(db.DateTime())
    visit_occurrence_id = db.Column(db.Integer, db.ForeignKey('visit_occurrence.visit_occurrence_id', ondelete='CASCADE'))

class Drug_exposure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id', ondelete='CASCADE'), nullable=False)
    drug_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id', ondelete='CASCADE'))
    drug_exposure_start_datetime = db.Column(db.DateTime(), nullable=False)
    drug_exposure_end_datetime = db.Column(db.DateTime(), nullable=False)
    visit_occurrence_id = db.Column(db.Integer, db.ForeignKey('visit_occurrence.visit_occurrence_id', ondelete='CASCADE'))

class Concept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    concept_id = db.Column(db.Integer, unique=True)
    concept_name = db.Column(db.String(1000))
    domain_id = db.Column(db.String(1000))

class Death(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id', ondelete='CASCADE'))
    death_date = db.Column(db.Date())