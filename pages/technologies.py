class technologies:
    def __init__(self,page):
        self.page=page

     #Technologies 
        self.technologies = self.page.locator("(//a[text()='Technologies'])[1]")

        self.ecom_dev_loc = self.page.locator("(//strong[text()='eCommerce Development'])[1]")

        self.magento_dev = self.page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')

        self.codeigniter = self.page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')

        self.big_comm= self.page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')

        self.cs_cart = self.page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')

        self.nop_com = self.page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')

        self.laravel_dev = self.page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        
        self.drupal = self.page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')

        self.joomla = self.page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')

        self.express = self.page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')

        self.opencart = self.page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')

        self.wordpress = self.page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')

        self.shopify = self.page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')

        self.nodejs = self.page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')

        self.woo = self.page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')

        self.prestashop = self.page.locator("//ul[@class='cm-flex cm-flex-wrap']//a[normalize-space()='Prestashop Development']")

        self.wix = self.page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')

        self.react_js = self.page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')

        self.technologies_list = [self.ecom_dev_loc,self.ecom_dev_loc,self.magento_dev, self.codeigniter, 
                        self.big_comm, self.cs_cart , self.nop_com, self.laravel_dev, self.drupal ,self.express, self.joomla,self.opencart, 
                        self.wordpress,self.shopify, self.nodejs, self.woo, self.prestashop, self.wix, self.react_js]


            #Mobile App Development 
        self.mobileapp= self.page.locator("//strong[normalize-space()='Mobile App Development']")
        self.react_native = self.page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.xamarin = self.page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.flutter = self.page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.swift = self.page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.enterprise = self.page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.kotlin = self.page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.ionic = self.page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.appartment= self.page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

        self.mobile_app_dev = [self.mobileapp, self.react_native,self.xamarin, self.flutter, self.swift, self.enterprise,self.kotlin, self.ionic,self.appartment]



    def ecom_development_selection(self):  
        for i in self.technologies_list:
            self.technologies.hover()
            self.ecom_dev_loc.hover()
            self.page.wait_for_timeout(2000)
            i.click()
            self.page.go_back()
            self.page.wait_for_load_state("load")

    def mobile_app_selection(self):
        for i in self.mobile_app_dev:
            self.technologies.hover()
            self.mobileapp.hover()
            self.page.wait_for_timeout(2000)
            i.click()
            self.page.go_back()
            self.page.wait_for_load_state("load")
