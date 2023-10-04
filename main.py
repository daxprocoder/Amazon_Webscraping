from selenium import webdriver
from Levenshtein import distance
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json
import math
import re
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains


options = webdriver.ChromeOptions()
# setBinary to brave browser
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
# options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# disable js
driver = webdriver.Chrome(options=options)


def group_similar_links(links, threshold):
    groups = []
    for link in links:
        added = False
        for group in groups:
            if distance(link, group[0]) < threshold:
                group.append(link)
                added = True
                break
        if not added:
            groups.append([link])
    return groups


data_amount = 0
num_pages = 5  # set the number of pages to scrape here
num_pages = math.floor(num_pages)


for num in range(1, num_pages):
    url = 'https://www.amazon.in/s?k=cosmetic&ref=nb_sb_noss'

    # gets links of products on the page and returns a list of links
    def get_product_links(url):
        driver.get(url)
        links = []
        data_span_xpath = '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]'
        data_span = driver.find_element(By.XPATH, data_span_xpath)
        data_divs = data_span.find_elements(
            By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div')
        for divs in data_divs:
            data_index = int(divs.get_attribute('data-index'))
            if not (data_index >= 2 and data_index <= 55):
                continue
            c = data_index + 1
            try:
                # get the anchor tag
                anchor = divs.find_element(
                    By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[' + str(c) + ']/div/div/div/div/div[1]/span/a')
                links.append(anchor.get_attribute('href'))
            except NoSuchElementException:
                print("No such element on index: " + str(c) + " skipping...")
                continue
        return links

    my_links = get_product_links(url)
    print(my_links)  # print the links for testing purposes

    def get_details(url):
        wait = WebDriverWait(driver, 0.5)
        action = ActionChains(driver)
        driver.get(url)
        # time.sleep(1)
        data_dict = {}

        print('getting title...')
        try:
            title = wait.until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="productTitle"]'))).text
        except TimeoutException:
            title = 'N/A'
        print('getting image...')
        try:
            main_img = wait.until(ec.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div[2]/div[5]/div[4]/div[3]/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/ul/li[1]/span/span/div/img'))).get_attribute('src')
        except TimeoutException:
            main_img = 'N/A'
        print('getting description...')

        #images for amazon

        images = []
        try:
            alt_images = wait.until(ec.presence_of_all_elements_located(
                (By.CLASS_NAME, "imageThumbnail")))
        except:
            alt_images = wait.until(ec.presence_of_all_elements_located(
                (By.CLASS_NAME, "thumbTypeimage")))

        for image in alt_images:
            image.click()
            image.click()
            dynamic_image = wait.until(ec.presence_of_all_elements_located(
                (By.CLASS_NAME, "a-dynamic-image")))
            for img in dynamic_image:
                images.append(img.get_attribute('src'))

        final_imgs = []

        for image in images:
            image = re.sub(r',', '', image)
            #only take images that have m.media-amazon.com/images/I
            if 'm.media-amazon.com/images/I' in image:
                final_imgs.append(image)

        print(len(final_imgs))

        disticnt_imgs = list(set(final_imgs))
        print(len(disticnt_imgs))

        # images for amazon

        try:
            ##feature-bullets > ul css selector
            description = wait.until(ec.presence_of_element_located(
                (By.XPATH, "//div[@id='feature-bullets']//ul"))).text
        except TimeoutException:
            description = 'N/A'
        print('getting list price...')
        try:
            list_price = wait.until(ec.presence_of_element_located(
                (By.CLASS_NAME, 'a-price'))).text
        except TimeoutException:
            list_price = 'N/A'
        print('getting price...')
        #class="a-price"
        try:
            price = wait.until(ec.presence_of_element_located(
                (By.CLASS_NAME, 'a-price-whole'))).text
        except TimeoutException:
            price = 'N/A'
        print('getting discount...')
        try:
            discount = wait.until(ec.presence_of_element_located(
                (By.CLASS_NAME, 'savingsPercentage'))).text
        except TimeoutException:
            discount = 'N/A'
        print('getting product details...')
        #id="detailBullets_feature_div"
        try:
            prod_det = wait.until(ec.presence_of_element_located(
                (By.XPATH, "//div[@id='detailBulletsWrapper_feature_div']//ul"))).text
        except TimeoutException:
            prod_det = 'N/A'

        data_dict = {
            'url': url,
            'title': title,
            'main_img': main_img,
            'images': group_similar_links(disticnt_imgs, 10)[0],
            'description': description,
            'list_price': list_price,
            'price': price,
            'discount': discount,
            'details': prod_det
        }

        return data_dict

    for link in my_links:
        data = get_details(link)
        with open('cosmetic.json', 'a') as f:
            json.dump(data, f, indent=4)
            f.write(',')

driver.quit()
