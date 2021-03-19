from flask import Blueprint, render_template, url_for
from pyapi.models import Person, Visit_occurrence, Condition_occurrence, Drug_exposure, Concept, Death
from pyapi import db
from datetime import datetime

bp = Blueprint('visit', __name__, url_prefix='/visit')

@bp.route('/')
def index():
    return render_template('visit/index.html')

@bp.route('/visit_concept')
def visit_concept():
    Iperson = len(Visit_occurrence.query.filter_by(visit_concept_id=9201).all())
    Operson = len(Visit_occurrence.query.filter_by(visit_concept_id=9202).all())
    Eperson = len(Visit_occurrence.query.filter_by(visit_concept_id=9203).all())

    return render_template('visit/visit_concept.html', Iperson=Iperson, Operson=Operson, Eperson=Eperson)

@bp.route('/gender')
def gender():
    malecount, femalecount = 0, 0
    male = Person.query.filter_by(gender_concept_id=8507).all()
    female = Person.query.filter_by(gender_concept_id=8532).all()

    for i in male:
        malecount += len(Visit_occurrence.query.filter_by(person_id=i.person_id).all())

    for i in female:
        femalecount += len(Visit_occurrence.query.filter_by(person_id=i.person_id).all())
    
    #personlist = Visit_occurrence.query.filter_by(person_id in Person.query.filter_by(gender_concept_id=Concept.query.filter_by(concept_name='MALE').first().concept_id).all()).all()
    return render_template('visit/gender.html', malecount=malecount, femalecount=femalecount)

@bp.route('/race')
def race():
    raceconcept = Concept.query.filter_by(domain_id='Race').all()
    count = 0
    racecount = []
    for i in raceconcept:
        personlist = Person.query.filter_by(race_concept_id=i.concept_id).all()
        if len(personlist) > 0:
            for a in personlist:
                racecount.append(len(Visit_occurrence.query.filter_by(person_id=a.person_id).all()))
    
    return render_template('visit/race.html', raceconcept=raceconcept, racecount=racecount)

@bp.route('/ethnicity')
def ethnicity():
    ethnicityconcept = Concept.query.filter_by(domain_id='Ethnicity').all()
    count = 0
    ethnicitycount = []
    for i in ethnicityconcept:
        personlist = Person.query.filter_by(ethnicity_concept_id=i.concept_id).all()
        if len(personlist) > 0:
            for a in personlist:
                ethnicitycount.append(len(Visit_occurrence.query.filter_by(person_id=a.person_id).all()))
    
    return render_template('visit/ethnicity.html', ethnicityconcept=ethnicityconcept, ethnicitycount=ethnicitycount)

@bp.route('/age')
def age():
    count0, count1, count2, count3, count4, count5, count6, count7, count8, count9, count10 = 0,0,0,0,0,0,0,0,0,0,0
    agelist = []
    yearlist = []
    visitlist = Visit_occurrence.query.all()
    personlist = Person.query.all()
    persondict = {}
    for i in personlist:
        persondict[i.person_id] = i.birth_datetime
    for i in visitlist:
        agelist.append(i.visit_start_datetime - persondict.get(i.person_id))
    
    for i in agelist:
        age = int(((i.days / 365) + 1) / 10)
        if age < 1:
            count0 += 1
        elif age < 2:
            count1 += 1
        elif age < 3:
            count2 += 1
        elif age < 4:
            count3 += 1
        elif age < 5:
            count4 += 1
        elif age < 6:
            count5 += 1
        elif age < 7:
            count6 += 1
        elif age < 8:
            count7 += 1
        elif age < 9:
            count8 += 1
        elif age < 10:
            count9 += 1
        else:
            count10 += 1
    
    yearlist.append(count0)
    yearlist.append(count1)
    yearlist.append(count2)
    yearlist.append(count3)
    yearlist.append(count4)
    yearlist.append(count5)
    yearlist.append(count6)
    yearlist.append(count7)
    yearlist.append(count8)
    yearlist.append(count9)
    yearlist.append(count10)
    return render_template('visit/age.html', yearlist=yearlist)