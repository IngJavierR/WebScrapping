from selenium import webdriver
driver = webdriver.Chrome()

def get_page(url):
    driver.get(url)

def get_movies():
    driver.find_elements_by_xpath("//input[@type='submit' and @value='VER CARTELERA']")[0].click()

def get_movies_divs():
    movies_divs = driver.find_elements_by_xpath("//article[@data-oculto='0' and @class='row tituloPelicula ng-scope']")
    for element in movies_divs:
        print(element.find_elements_by_xpath("//figure/a/img").get_attribute('src'))

def path_get_movies():
    get_page('http://www.cinepolis.com/')
    driver.implicitly_wait(2)
    get_movies()
    driver.implicitly_wait(8)
    get_movies_divs()
    #driver.implicitly_wait(3)
    #driver.close()

if __name__ == '__main__':
    print('Inicio')
    path_get_movies()