from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Modified from https://github.com/aryanc55/T-RexDinoRunner-GAME-AI-BOT/blob/master/model.py
class DinoGame:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--mute-audio")
        self.driver = webdriver.Chrome(executable_path="/Users/nikhilkulkarni/downloads/chromedriver", chrome_options=chrome_options)
        self.driver.get("chrome://dino")
        self.driver.execute_script("Runner.config.ACCELERATION=0")
    def press_up(self):
        self.driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_UP)
    def pause(self):
        self.driver.execute_script("return Runner.instance_.stop()")
    def resume(self):
        self.driver.execute_script("return Runner.instance_.play()")
    def restart(self):
        self.driver.execute_script("Runner.instance_.restart()")
    def get_score(self):
        score_arr = self.driver.execute_script("return Runner.instance_.distanceMeter.digits")
        score = ''.join(score_arr)
        return int(score)
    def is_playing(self):
        return self.driver.execute_script("return Runner.instance_.playing")
    def is_crashed(self):
        return self.driver.execute_script("return Runner.instance_.crashed")
    def close(self):
        self.driver.close()

# Simple test of selenium automator
if __name__ == '__main__':
    game = DinoGame()
    while True:
        game.press_up()
        print("score:",game.get_score(), "crashed:", game.is_crashed())
