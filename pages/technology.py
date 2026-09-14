class technologies:
    def __init__(self,page):

        self.page=page
        self.Tech = page.locator('(//a[text()="Technologies"])[1]')
        self.ed = page.locator('//strong[text()="eCommerce Development"]')
        self.md = page.locator('//strong[text()="Mobile App Development"]')
        self.AI = page.locator('//strong[text()="Artificial Intelligence"]')


        #eCommerce Development options
        self.ed_1 = page.locator('(//a[text()="Magento Development"])')
        self.ed_2 = page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.ed_3 = page.locator('(//a[text()="Big Commerce"])[1]')
        self.ed_4 = page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.ed_5 = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.ed_6 = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.ed_7 = page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.ed_8 = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.ed_9 = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.ed_10 = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.ed_11 = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.ed_12 = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.ed_13 = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.ed_14 = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.ed_15 = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.ed_16 = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.ed_17 = page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')

        #Mobile App Development options
        self.md_1 = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.md_2 = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.md_3 = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.md_4 = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.md_5 = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.md_6 = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.md_7 = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.md_8 = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
    
        self.ed_list = [self.ed_1, self.ed_2, self.ed_3, self.ed_4, self.ed_5, self.ed_6, self.ed_7, self.ed_8, self.ed_9, self.ed_10, self.ed_11, self.ed_12, self.ed_13, self.ed_14, self.ed_15, self.ed_16]
        self.md_list=[self.md_1,self.md_2,self.md_3,self.md_4,self.md_5,self.md_6,self.md_7,self.md_8]

    def click_eCommerce_Development(self):
        for i in self.ed_list:
            self.Tech.hover()
            self.ed.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_Mobile_App_Development(self):
        for i in self.md_list:
            self.Tech.hover()
            self.md.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_AI(self):
        self.Tech.hover()
        self.AI.click()
        self.page.wait_for_load_state("load")
        self.page.go_back()


    
