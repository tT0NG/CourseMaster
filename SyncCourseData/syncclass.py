import mechanize

def sync_class(class_title, class_code, class_number):
    br = mechanize.Browser()
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1')]

    br.open("http://schedule.psu.edu/act_advanced_search_get_seats.cfm")
    FORM_HTML = '<form method="post"><input name="crseName" id="crseName"><input name="crseNum" id="crseNum"><input name="semester" id="semester"><input name="location" id="location"><input name="CEcrseloc" id="CEcrseloc"></form>'
    res = mechanize._form.ParseString(FORM_HTML, "http://schedule.psu.edu/act_advanced_search_get_seats.cfm")
    br.form = res[1]
    br['crseName'] = class_title
    br['crseNum'] = class_code
    br['semester'] = 'FALL 2015'
    br['location'] = 'UP'
    br['CEcrseloc'] = 'UP'
    br.submit()
    course_list = br.response().read().split('!')[1::2]
    br.close()

    for course in course_list:
        detail = course.split(';')[1]
        if detail[0] == class_number:
            if detail[1] != '0':
                return True
            else:
                return False
