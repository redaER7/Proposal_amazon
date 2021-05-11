####################################################################################
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
####################################################################################
df=pd.read_csv("amazon_credentials.txt","r",delimiter=',',header=None)
login=df.values[0][0]
passw=df.values[0][1]
####################################################################################
print('Initializing Profile...\n')
print('-----------------------------------------------------------------')
#SELENIUM ENTRIES
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
cap['acceptInsecureCerts'] = True
binary = FirefoxBinary('/usr/bin/firefox')
##
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--load-images=no')
options.add_argument("window-size=1400,600")
options.add_argument("user-data-dir=/tmp/tarun")
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--proxy-server=%s' % proxy)
##
profile = webdriver.FirefoxProfile()
#profile.set_preference("general.useragent.override", "[user-agent string]")
profile.set_preference("general.useragent.override", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")
####################################################################################
url='https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1'
#
driver = webdriver.Firefox(profile,options = options,capabilities=cap,firefox_binary=binary)
#driver,options,args,df=selenium_request(profile,options,cap,binary,url,df,args)
driver.get(url)
driver.set_page_load_timeout(np.random.randint(5,10))
#
#USERNAME
username_input = driver.find_element_by_css_selector("input[name='email']")
username_input.send_keys(login)
login_button=driver.find_element_by_id('continue')
login_button.click()
time.sleep(np.random.randint(5,10))

pass_input = driver.find_element_by_css_selector("input[name='password']")
pass_input.send_keys(passw)
pass_input.click()
