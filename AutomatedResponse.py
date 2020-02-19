from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class ChatBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def openDiscord(self):
        #search webdriver on pc and open chrome
        self.driver = webdriver.Chrome('C:\\Users\\User\\Desktop\\chromedriver.exe')
        #browser asks me to accept certificate from the website, so i ignore
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        #maximize window
        self.driver.maximize_window()
        #open page
        self.driver.get('https://discordapp.com/login')
        print('Page opened succesfully')

    def login(self):

        sleep(3) #for avoiding ban lol

        #enter email
        email = self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/div[1]/div/input')
        email.send_keys(self.username)
        print('email sent succesfully')

        sleep(2) #for avoiding ban lol

        #enter password
        password = self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/div[2]/div/input')
        password.send_keys(self.password)
        print('Password sent succesfully')
        sleep(1)
        password.send_keys(Keys.ENTER)

    def closePopup(self):

        sleep(8) #for avoiding ban lol (and waiting for the page to load)

        #close popup window asking for server creation
        skip = self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div[2]/div[2]/div[3]/form/div/button[1]')
        skip.click()

    def searchPerson(self):

        sleep(3)

        #locate first chat
        #note to self: MUST change function for working by user input
        friend = self.driver.find_elements_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/div/div/div/div[1]/div[1]/div[2]/div/span/a[2]/div/div[2]/div[1]/div')
        friend[0].click()

    def sendMessage(self, message):

        #switch focus to original tab
        self.driver.switch_to.window(self.driver.window_handles[0])

        sleep(2)

        #select chatbox
        chatbox = self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/form/div/div/div/div[3]/div[2]/div')
        chatbox.click()

        sleep(3) #for avoiding ban lol

        chatbox.send_keys(message)

        sleep(2) #for avoiding ban lol

        chatbox.send_keys(Keys.ENTER)

    def openCleverBot(self, message):
        
        sleep(2) #for avoiding ban lol

        #open new tab (javascript function)
        self.driver.execute_script("window.open('');")
        sleep(2)

        #switch focus to new tab
        self.driver.switch_to.window(self.driver.window_handles[1])
        #open cleverbot page
        self.driver.get("https://www.cleverbot.com/")

        sleep(2) #for avoiding ban lol

        #find chat bar
        chatbar = self.driver.find_element_by_name('stimulus')
        chatbar.clear()
        chatbar.send_keys(message)
        chatbar.send_keys(Keys.ENTER)
        print('Mensaje enviado a cleverbot')
        sleep(8)

        #copy answer
        answer = self.driver.find_element_by_id('line1')
        response = answer.text
        print('Mensaje de respuesta: ' + response)

        self.sendMessage(response)

    def copyAnswer(self):

        sleep(3) #for avoiding ban lol

        #all messages share the same class, so i get last item in the list (by using -1)
        allmessages = self.driver.find_elements_by_xpath("//div[@class='markup-2BOw-j containerCozy-336-Cz markupRtl-3M0hmN']")
        lastmessage = allmessages[-1].text
        print('Mensaje recibido: ' + lastmessage)

        self.openCleverBot(lastmessage)

    def wait(self):
        sleep(30)

    def closeWindow(self):

        #close current focused tab
        self.driver.close()


email = input('Ingrese un email: ')
password = input('Ingrese una contraseña: ')

bot = ChatBot(email,password)
bot.openDiscord()
bot.login()
bot.closePopup()
bot.searchPerson()
#to do: put both methods below in a loop that checks for friend response
bot.copyAnswer()
bot.wait()