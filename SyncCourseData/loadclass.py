from SyncCourseData.models import Course
import json
import re

def load_class():
    json_data = open('course3.json').read()
    data = json.loads(json_data)

    for token in data:
        try:
            name = token['class_name'][0]
            num_pos = re.search('\d', name)
            new_course = Course()
            new_course.class_campus = 'UP'
            #121
            new_course.class_code = str(name[num_pos.start():len(name)])
            #CMPSC
            new_course.class_title = str(name[0:num_pos.start()-1])
            #469646
            new_course.class_number = int(token['class_number'][0])

            new_course.class_time = str(token['class_time'][0])

            new_course.save()
        except:
            print token['class_number'][0]


