from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from pyapi.models import Person
from pyapi import db

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def getperson():
    person_list = Person.query.all()
    print(person_list[0].gender_concept_id)
    return 'hello'