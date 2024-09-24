from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

# Open URL
driver.get("https://www.examtopics.com/exams/microsoft/az-300/view/")

# Wait for the container that holds the questions to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "question-choices-container")))

# Find all question choices containers
choices_containers = driver.find_elements(By.CLASS_NAME, "question-choices-container")

# Iterate through each question choices container
for container in choices_containers:
    # Extract choice items
    choice_items = container.find_elements(By.CLASS_NAME, "multi-choice-item")
    
    # Iterate through each choice item
    for item in choice_items:
        # Extract choice letter and text
        choice_letter = item.find_element(By.CLASS_NAME, "multi-choice-letter").text.strip()
        choice_text = item.text.replace(choice_letter, "").strip()
        
        # Concatenate choice letter with choice text
        full_choice = choice_letter + "" + choice_text
        
        # Print full choice
        print("Full Choice:", full_choice)
        print("-" * 50)

# Close the browser
driver.quit()
