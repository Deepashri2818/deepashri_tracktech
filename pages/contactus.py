class contactus:
    def __init__(self,page):
        self.page=page
        #Contact Us 
        self.contactus = page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')

        self.name= page.locator('(//input[@placeholder="Your Name"])[2]')
        self.mail= page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.otp= page.locator('(//button[text()="Send OTP"])[2]')
        self.company= page.locator('(//input[@placeholder="Your Company"])[2]')

        self.service= page.locator('(//select[@name="service"])[2]')
        self.phone= page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message= page.locator('(//textarea[@placeholder="Message"])[2]')

        self.submit= page.locator('(//input[@type="submit"])[2]')

    def fill_contact_us_form(self, name, email, company_name, phone ):
        self.contactus.click()

        self.name.fill(name)
        self.mail.fill(email)
        self.company.fill(company_name)
        self.service.select_option("Web Development")
        self.phone.fill(phone)

        self.message.fill("Hello")

        self.submit.click()







