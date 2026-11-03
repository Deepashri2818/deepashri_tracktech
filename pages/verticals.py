class vertical:
    def __init__(self, page):
        self.page=page   
        #verticals locators
        
        self.verticals = page.locator("(//a[text()='Verticals'])[1]")
        
        #Select Trading in Verticals
        self.trading = page.locator('(//a[text()="Verticals"])[1]')
 
        self.stock_trading= page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
    
        self.paper_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        
        self.cfd_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
 
        self.trading_app = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
    
        self.algo_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')

        self.custom_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        
        self.trading_option = [self.stock_trading,self.paper_trading,  self.cfd_trading,self.trading_app, self.algo_trading, self.custom_trading]

        #Retail and Ecommerce locators
        self.retail_ecom = page.locator("//strong[text()='Retail and Ecommerce']")
           
        self.ecom_web_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')

        self.ecom_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        self.retail_ecom_list = [self.ecom_web_dev,self.ecom_app_dev ]

        #Locators of healthcare
        self.heathc = page.locator("//strong[text()='Healthcare']")

        self.dietnt = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')

        self.heathapp = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.healthcare = [self.dietnt,self.heathapp ]

        #Locator for Fintech 
        self.fintech_loc = page.locator("//strong[text()='Fintech']")

        self.pos_loc = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')

        self.crypto = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        self.fintech = [self.pos_loc, self.crypto]




    def trading_options_clicking(self):
        for i in self.trading_option:
            self.verticals.hover()
            self.trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def retail_options_selection(self):
        for i in self.retail_ecom_list:
            self.verticals.hover()
            self.retail_ecom.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def healthcare_options_selection(self):
          for i in self.healthcare:
            self.verticals.hover()
            self.heathc.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def fintech_options_selection(self):
         for i in self.fintech:
            self.verticals.hover()
            self.fintech_loc.hover()
            
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()



