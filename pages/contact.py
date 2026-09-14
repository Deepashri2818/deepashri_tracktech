from config import BASE_URL


class contacts:
    def __init__(self,page):
        self.page = page

        #contact details
        self.Contact_Us = page.locator('//ul[@class="cm-flex-type-2"]//a[normalize-space()="Contact us"]')
        self.name = page.locator('(//input[@placeholder="Your Name"])[2]')
        self.mail = page.locator('(//input[@placeholder="Your Mail"])[2]')
        # self.button=page.locator('//button[@class="send-otp-btn"]')
        # self.otp= page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.company = page.locator('(//input[@placeholder="Your Company"])[2]')
        self.service = page.locator('(//select[@name="service"])[2]')
        self.phone = page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message = page.locator('(//textarea[@placeholder="Message"])[2]')

        #Web Devlopment
        self.cms = page.locator('//a[normalize-space()="CMS Website Development"]')
        self.arrow1 = page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]')
        self.web = page.locator('(//a[@href="https://www.tranktechnologies.com/website-development-company"])[1]')
        self.custom = page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')

        #arrow1.click()

        self.web_list = [self.cms,self.custom]


        #App devlopment
        self.ios = page.locator('//a[normalize-space()="iOS App Development"]')
        # self.arrow2 = page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]')
        # self.android = page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        # self.app = page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
        self.hyb = page.locator('//a[normalize-space()="Hybrid Mobile App Development"]')
        self.cross =  page.locator('//a[normalize-space()="Cross-Platform App Development"]')
        self.prog = page.locator('//a[normalize-space()="Progressive Web App Development"]')

        self.app_list = [self.ios,self.hyb,self.cross,self.prog]


        #graphic design
        self.logo = page.locator('//a[normalize-space()="Logo Design"]')
        self.banner = page.locator('//a[normalize-space()="Banner Design"]')
        self.pack = page.locator('//a[normalize-space()="Packaging Design"]')
        self.cards = page.locator('//a[normalize-space()="Business cards Design"]')

        self.graphic_list = [self.logo,self.banner,self.pack,self.cards]

    
        #UI-UX
        self.mob = page.locator('//a[normalize-space()="Mobile App Design"]')
        self.resp = page.locator('//a[normalize-space()="Responsive Web Design"]')
        self.brand = page.locator('//a[normalize-space()="Brand Identity Design"]')

        self.UI_List = [self.mob,self.resp,self.brand]


        self.portfolio = page.locator('//a[normalize-space()="Portfolio"]')

        #follow us - social media
        self.facebook = page.locator('//img[@alt="Facebook"]')
        self.linkedin = page.locator('//img[@alt="LinkedIn"]')
        self.insta = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/Insta.png"]')
        self.pinterest = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/pinterest.png"]')
        self.twitt = page.locator('//img[@alt="Twitter"]')
        self.ytube = page.locator('//img[@alt="Youtube"]')
        self.quora = page.locator('//img[@alt="Quora"]')

        self.follow_list = [self.facebook,self.linkedin,self.insta,self.pinterest,self.twitt,self.ytube,self.quora]



    def fill_contact_details(self):
        self.Contact_Us.click()
        self.name.fill("Apurva")
        self.mail.fill("apu5@gmail.com")
        self.company.fill("Umcodemy")
        self.service.select_option("App Development")
        self.phone.fill("5847126978")
        self.message.fill("Please share me the detail information")
        self.page.wait_for_load_state("load")

    def click_Web_Devlopment(self):
        self.Contact_Us.click()
        for i in self.web_list:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_App_devlopment(self):
        self.Contact_Us.click()
        for i in self.app_list:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_graphic_design(self):
        self.Contact_Us.click()
        for i in self.graphic_list:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_UI_UX(self):
        self.Contact_Us.click()
        for i in self.UI_List:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def socialmediapageclick(self):
        self.portfolio.click()
        self.page.wait_for_load_state(state="load")
        for i in self.follow_list:
            i.scroll_into_view_if_needed()
            # prefer clicking the parent anchor if present
            try:
                parent_anchor = i.locator('xpath=ancestor::a[1]')
                if parent_anchor.count():
                    parent_anchor.wait_for(state="visible", timeout=5000)
                    with self.page.context.expect_page() as new_page_info:
                        parent_anchor.click()
                    new_tab = new_page_info.value
                    new_tab.wait_for_load_state("load")
                    new_tab.close()
                    continue
            except Exception:
                pass

            # fallback: wait for the image to be visible then click
            try:
                i.wait_for(state="visible", timeout=5000)
                with self.page.context.expect_page() as new_page_info:
                    i.click()
                new_tab = new_page_info.value
                new_tab.wait_for_load_state("load")
                new_tab.close()
            except Exception:
                # if clicking still fails, ignore to continue with other links
                continue

    # def socialmediapageclick(self):
    #     self.portfolio.click()
    #     self.page.wait_for_load_state(state="load")
    #     self.socialmediaList=[self.facebook,self.linkedin,self.insta,self.pinterest,self.twitt,self.ytube,self.quora]
    #     for social_media_link in self.socialmediaList:
    #         social_media_link.scroll_into_view_if_needed()
    #         with self.page.context.expect_page() as new_page_info:
    #             social_media_link.click()
    #         new_tab = new_page_info.value
    #         new_tab.wait_for_load_state("load")
    #         new_tab.close()


    