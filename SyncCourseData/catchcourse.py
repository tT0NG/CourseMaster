# coding=utf-8
import mechanize
import cookielib

from .models import Course
from .syncclass import sync_class

def add_class():
    activated_class_list = Course.objects.filter(is_active=True)
    print activated_class_list
    for course in activated_class_list:
        if sync_class(course.class_title, course.class_code, course.class_number):
            user = course.get_first_user()
            try:
                if submitClass(user.psu_account, user.psu_password, course.class_number):
                    # success
                    user.courses_caught += 1
                    course.remove_user(user.username)
                    user.save()

                else:
                    # unsuccessful
                    user.courses_pack += 1
                    user.save()
            except:
                pass


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
                print 'Add class ' + sectionNubmer + ' successfully'
                return True
            else:

                print 'Section fulled, failed to add class' + sectionNubmer + "\n"
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
                print 'Add class ' + sectionNubmer + ' successfully'
                return True
            else:
                print 'Section fulled, failed to add class' + sectionNubmer + "\n"
                return False

        elif br.response().read().find('wish to schedule any of the other available sections') != -1:
            print 'Section fulled, failed to add class' + sectionNubmer + "\n"
            return False

        else:
            if br.response().read().find('success') != -1:
                print 'Add class ' + sectionNubmer + ' successfully'
                return True
            else:
                print 'Section fulled, failed to add class' + sectionNubmer + "\n"
                return False

    except:
        print 'An unexpected error occured, please connect psuclassgotcha@gmail.com\n'
        print br.response().read()
        return False