# coding=utf-8
import mechanize
import cookielib
import time

from sendemail import email_sender, email_sender_fail

from .models import Course, ClassLog, RunningCount



def add_class():
    course_number_list = []
    activated_class_list = Course.objects.filter(is_active=True)
    for course in activated_class_list:
        course_number_list.append(course.class_number)

    A = course_number_list[:len(course_number_list)/2]
    print A
    sync_class(A)

def add_class2():
    course_number_list = []
    activated_class_list = Course.objects.filter(is_active=True)
    for course in activated_class_list:
        course_number_list.append(course.class_number)

    B = course_number_list[len(course_number_list)/2:]
    print B
    sync_class(B)

def sync_class(activating_class_number_list):
    # init the browser
    br = mechanize.Browser()
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36')]
    # when activating courses list has at least one element
    while activating_class_number_list and ClassLog.objects.get(id=1).running:
        # let the first element in list be the current course
        current_course = Course.objects.get(class_number=activating_class_number_list[0])
        # open schedule website
        br.open("http://schedule.psu.edu/act_advanced_search_get_seats.cfm")
        # create form
        FORM_HTML = '<form method="post"><input name="crseName" id="crseName"><input name="crseNum" id="crseNum"><input name="semester" id="semester"><input name="location" id="location"><input name="CEcrseloc" id="CEcrseloc"></form>'
        res = mechanize._form.ParseString(FORM_HTML, "http://schedule.psu.edu/act_advanced_search_get_seats.cfm")
        #select form & put in necessary values
        br.form = res[1]
        br['crseName'] = current_course.class_title
        br['crseNum'] = current_course.class_code
        br['semester'] = 'SPRING 2016'
        br['location'] = 'UP'
        br['CEcrseloc'] = 'UP'
        # submit
        br.submit()
        c = RunningCount.objects.get(id=1)
        c.count += 1
        c.save()
        time.sleep(5)
        # get returned course list
        course_list = br.response().read().split('!')[1::2]
        # for every course in returned course list
        for course in course_list:
            # split to class number and remaining seats
            class_number_and_seats = course.split(';')
            print class_number_and_seats
            # if the class number is in activating courses list
            if class_number_and_seats[0] in activating_class_number_list:
                # remove it
                activating_class_number_list.remove(class_number_and_seats[0])
                # if it has opening seats
                if class_number_and_seats[1] != '0':
                    # catch it
                    cathing_course = Course.objects.get(class_number=class_number_and_seats[0])
                    user = cathing_course.get_first_user()
                    if submitClass(user.psu_account, user.psu_password, class_number_and_seats[0]):
                        user.add_course_caught(class_number_and_seats[0])
                        cathing_course.remove_user(user.username)
                        # send email
                        try:
                            email_sender(user, cathing_course)
                        except:
                            pass
                    else:
                        user.add_course_failed(class_number_and_seats[0])
                        if user.courses_failed > 5 and user.is_correct:
                            user.is_correct = False
                            user.save()
                            for course_num in user.get_courses_list('running'):
                                user.remove_course(course_num)
                                course = Course.objects.get(class_number=course_num)
                                course.remove_user(user.username)
                                course.save()
                            user.save()
                            try:
                                email_sender_fail(user)
                            except:
                                pass

    # close browser
    br.close()


def submitClass(usrname, password, sectionNubmer):
    try:
        # cookie jar
        cj = cookielib.LWPCookieJar()
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_cookiejar(cj)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        br.addheaders = [('User-agent',
                          'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1')]

        # 打开登录界面
        br.open(
            "https://webaccess.psu.edu/?cosign-elionvw.ais.psu.edu&https://elionvw.ais.psu.edu/cgi-bin/elion-student.exe/submit/goRegistration")

        br.select_form(nr=0)

        # 输入用户名密码，跳转
        br['login'] = usrname
        br['password'] = password
        br.submit()

        # 页面有语法错误，更正
        response = br.response()  # this is a copy of response
        response.set_data(response.get_data().replace("<!!--", "<!--"))
        br.set_response(response)

        # 选择Spring 2015
        br.select_form(nr=0)
        list = []
        for f in br.form.controls:
            list.append(f.name)
        radioID = list[1]
        br[radioID] = ['1 @ 2']
        br.submit()

        # 页面有语法错误，更正
        response = br.response()  # this is a copy of response
        response.set_data(response.get_data().replace("<!!--", "<!--"))
        br.set_response(response)
        # 选择密码输入框
        br.select_form(nr=0)
        list = []
        for f in br.form.controls:
            list.append(f.name)
        passwordId = list[0]
        # 输入密码， 跳转
        br[passwordId] = password
        br.submit()
        # 页面有语法错误，更正
        response = br.response()  # this is a copy of response
        response.set_data(response.get_data().replace("<!!--", "<!--"))
        br.set_response(response)
        # 选择课程输入框
        br.select_form(nr=0)
        list = []
        for f in br.form.controls:
            list.append(f.name)

        courseId = list[5]
        submitId = list[6]

        # 输入课程代码
        br[courseId] = sectionNubmer
        br.submit(submitId)

        # 页面有语法错误，更正
        response = br.response()  # this is a copy of response
        response.set_data(response.get_data().replace("<!!--", "<!--"))
        br.set_response(response)
        if br.response().read().find('conflict') != -1:
            br.select_form(nr=0)
            list = []
            for f in br.form.controls:
                list.append(f.name)
            radioID = list[1]
            br[radioID] = ['N']
            br.submit()
            # 页面有语法错误，更正
            response = br.response()  # this is a copy of response
            response.set_data(response.get_data().replace("<!!--", "<!--"))
            br.set_response(response)

            if br.response().read().find('success') != -1:
                ClassLog.objects.get(id=1).add_catched_course(sectionNubmer)
                return True
            else:
                ClassLog.objects.get(id=1).add_failed_course(sectionNubmer)
                return False

        elif br.response().read().find('You have a duplicate course request') != -1:
            br.select_form(nr=0)
            list = []
            for f in br.form.controls:
                list.append(f.name)
            radioID = list[1]
            br[radioID] = ['N']
            br.submit()
            if br.response().read().find('success') != -1:
                ClassLog.objects.get(id=1).add_catched_course(sectionNubmer)
                return True
            else:
                ClassLog.objects.get(id=1).add_failed_course(sectionNubmer)
                return False

        elif br.response().read().find('other available sections') != -1:
            ClassLog.objects.get(id=1).add_failed_course(sectionNubmer)
            return False

        else:
            if br.response().read().find('success') != -1:
                ClassLog.objects.get(id=1).add_catched_course(sectionNubmer)
                return True
            else:
                ClassLog.objects.get(id=1).add_failed_course(sectionNubmer)
                return False

    except:
        ClassLog.objects.get(id=1).add_failed_course(sectionNubmer)
        print br.response().read()
        return False
