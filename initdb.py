import json
import os
import re

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minerva.settings')

django.setup()

from base.models import SubjectArea, Course


def create_subject_areas():
    with open('subject_areas.json', 'r') as f:
        subject_areas = json.load(f)

    subject_area_models = [SubjectArea(short=short, long=long) for short, long in subject_areas.items()]
    for models in subject_area_models:
        models.save()


def create_courses():
    with open('courses.json', 'r') as f:
        courses = json.load(f)

    subject_area = re.compile(r'[A-Z]{4}')
    course_number = re.compile(r'\d{4}')
    credit_hours = re.compile(r'(\d+)-?(\d+)?')

    for course in courses:
        for course_num in re.findall(course_number, course['course_id']):
            hours = re.search(credit_hours, course['credit_hours'])

            min, max = int(hours[1]), hours[2]

            subject_areas = re.findall(subject_area, course['course_id'])
            parsed = {
                'course_number':    course_num,
                'name':             course['course_title'],
                'description':      course['course_description'],
                'lab':              course['course_id'].endswith('L'),
                'honors':           course['course_id'].endswith('H'),
                'writing':          course['course_id'].endswith('W'),
                'service':          course['course_id'].endswith('S'),
                'online':           course['course_id'].endswith('E'),
                'graduate':         int(course_num) >= 6000,
                'min_credit_hours': min,
                'max_credit_hours': max
            }

            course_model = Course(**parsed)
            course_model.save()

            for sa in subject_areas:
                sa = SubjectArea.objects.get(short=sa)
                sa.course_set.add(course_model)
                print(repr(course_model))


if __name__ == '__main__':
    create_subject_areas()
    create_courses()
