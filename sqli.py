from urllib.request import urlopen
import mechanicalsoup


def checkForm(browser, login_page, login_html):
    forms = login_html.select("form")

    if len(forms) == 0:
        return False

    # 2
    form = forms[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "ThunderDude"

    # 3
    profiles_page = browser.submit(form, login_page.url)
    
    return True




def sqlicheck(url):

    # 1
    browser = mechanicalsoup.Browser()
    login_page = browser.get(url)
    login_html = login_page.soup

    checkForm(browser, login_page,login_html)






    
