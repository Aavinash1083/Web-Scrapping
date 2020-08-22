from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

# Load the page on the browser
browser.get('https://www.linkedin.com/')

# Execute Javascript code on webpage
browser.execute_script(
    "(function(){try{for(i in document.getElementsByTagName('a')){let el = document.getElementsByTagName('a')[i]; "
    "if(el.innerHTML.includes('Contact info')){el.click();}}}catch(e){}})()")

# Wait 5 seconds for the page to load
time = time.sleep(5)

# Scrape the email address from the 'Contact info' popup
email = browser.execute_script(
    "return (function(){try{for (i in document.getElementsByClassName('pv-contact-info__contact-type')){ let el = "
    "document.getElementsByClassName('pv-contact-info__contact-type')[i]; if(el.className.includes('ci-email')){ "
    "return el.children[2].children[0].innerText; } }} catch(e){return '';}})()")
    
# Rendering of the page
soup = BeautifulSoup(browser.page_source, 'lxml')

# Scraping of the Name (profile_name)
name_div = soup.find('div', {'class': 'flex-1 mr5'})
name_loc = name_div.find_all('ul')
profile_name = name_loc[0].find('li').get_text().strip()


