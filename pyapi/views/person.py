from flask import Blueprint, render_template, url_for
from pyapi.models import Person, Visit_occurrence, Condition_occurrence, Drug_exposure, Concept, Death
from pyapi import db

bp = Blueprint('person', __name__, url_prefix='/person')

@bp.route('/')
def index():
    return render_template('person/index.html')

@bp.route('/total')
def total():
    person = len(Person.query.all())
    return render_template('person/total.html', person = person)

@bp.route('/gender')
def gender():
    man_concept = Concept.query.filter_by(concept_name = "MALE").first()
    female_concept = Concept.query.filter_by(concept_name = "FEMALE").first()
    male = len(Person.query.filter_by(gender_concept_id=man_concept.concept_id).all())
    female = len(Person.query.filter_by(gender_concept_id=female_concept.concept_id).all())
    return render_template('person/gender.html', male=male, female=female)

@bp.route('/race')
def race():
    racedict = {}
    personrace = []
    racecount = []
    raceconcept = Concept.query.filter_by(domain_id='Race').all()
    for i in range(len(raceconcept)):
        racedict[raceconcept[i].concept_id] = raceconcept[i].concept_name
    
    for i in racedict.keys():
        race = Person.query.filter_by(race_concept_id=i).all()
        if len(race) == 0 :
            continue
        personrace.append(racedict.get(i))
        racecount.append(len(race))
    
    return render_template('person/race.html', personrace=personrace, racecount=racecount)

@bp.route('/ethnicity')
def ethnicity():
    ethnicitydict = {}
    personethnicity = []
    ethnicitycount = []
    ethnicityconcept = Concept.query.filter_by(domain_id='Ethnicity').all()
    for i in range(len(ethnicityconcept)):
        ethnicitydict[ethnicityconcept[i].concept_id] = ethnicityconcept[i].concept_name
    
    for i in ethnicitydict.keys():
        ethnicity = Person.query.filter_by(ethnicity_concept_id=i).all()
        if len(ethnicity) == 0 :
            continue
        personethnicity.append(ethnicitydict.get(i))
        ethnicitycount.append(len(ethnicity))
    
    return render_template('person/ethnicity.html', personethnicity=personethnicity, ethnicitycount=ethnicitycount)

@bp.route('/death')
def death():
    death = len(Death.query.all())
    return render_template('person/death.html', death = death)