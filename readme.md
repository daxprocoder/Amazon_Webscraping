# footer

Webscarping Amazon!

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium ,Levenshtein.
    
    ```bash
    pip install selenium
    pip install python-Levenshtein
    ```


## Usage
    
    ```python
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
    ```


## Disclaimer 
This code is for educational purposes only. It demonstrates how web scraping works and should not be used to scrape any website without proper permission. Unauthorized scraping of websites can violate terms of service and may result in legal action or being banned from the targeted site. Always ensure you have explicit consent or follow the website's terms and policies before attempting any web scraping.


## Description

The project I'm undertaking involves web scraping on the Amazon platform, and I'm employing the Python programming language alongside Selenium and Chrome WebDriver to accomplish this task efficiently. This project revolves around automating the process of extracting valuable data from Amazon's vast e-commerce platform.

Selenium is a powerful tool for web automation, enabling the program to interact with web pages just as a human user would. In combination with Chrome WebDriver, it provides a reliable and efficient way to navigate Amazon's web pages, search for products, and extract various data points such as product names, prices, customer ratings, and descriptions.

Python, a versatile and widely used programming language, serves as the backbone of this project. Its rich ecosystem of libraries and tools, including Selenium, facilitates web scraping and data manipulation. Python also allows for seamless integration with data structuring and storage processes.

One of the key objectives of this project is automation. Manually collecting data from Amazon is time-consuming and error-prone. Automation ensures that the scraping process can be performed regularly and consistently, keeping the dataset up-to-date with the latest information.

The collected data is structured and organized in JSON (JavaScript Object Notation) format. JSON is chosen due to its simplicity and ease of use, making it suitable for storing structured data. JSON files are lightweight, easy to read, and easy to parse, making them an ideal choice for data storage.

Data quality is a paramount concern in this project. Special attention is given to error handling mechanisms to address potential issues that may arise during web scraping. Ethical considerations are also taken into account, with the project adhering to Amazon's terms of service, including rate limiting to avoid overloading Amazon's servers and respecting robots.txt files.

As the project progresses, the collected data can be analyzed and used for various purposes, such as market research, price tracking, and trend analysis. Data visualization tools can be employed to provide insights and trends in a user-friendly format.

To ensure the project's replicability and usability, comprehensive documentation will be provided. This documentation will guide users on setting up the environment, running the web scraper, and interpreting the collected data.

I have developed a website where I push data from various sources and display it to the users in a user-friendly manner. This platform allows for seamless data integration and presentation, offering an efficient way to access and interact with valuable information

## instructions

Change the path of the chrome driver in the code to the path of the chrome driver in your system.

and im using the brave browser so if you are using chrome browser then change the browser name and location in the code in main.py file.

chagne the link of the search itmes which u want to search by deafult its cosmatics.

also i uploaded some example of the data which i scraped from the amazon website.

even i create a site where i push these data you required you can check .

also there is file aslo you can change the jason file to csv using pandas.


## images

![image](https://cdn.discordapp.com/attachments/777919148985810945/1159020727253618739/image.png?ex=651e5daa&is=651d0c2a&hm=d0d46a5c69ab4a55eb3cafa081b088c48e77ab93ebb7e346e3e6e1c2d1cfcc64&)




## License

[MIT](https://choosealicense.com/licenses/mit/)
