class vertical:
    def __init__(self,page):

        self.page = page
        self.verticals = page.locator('(//a[text()="Verticals"])[1]')
        self.trad = page.locator('//li[@data-id="trading"]')
        self.RE = page.locator('//li[@data-id="retailEcommerce"]')
        self.HC = page.locator('//strong[text()="Healthcare"]')
        self.Finntech = page.locator('//li[@data-id="fintech"]')
        self.CA = page.locator('//strong[text()="Custom App"]')

        #trading options
        self.trade1 = page.locator('(//a[text()="Stock Trading"])[1]')
        self.trade2 = page.locator('(//a[text()="Paper Trading"])[1]')
        self.trade3 = page.locator('(//a[text()="CFD Trading"])[1]')
        self.trade4 = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.trade5 = page.locator('//a[text()="Algo Trading"]')
        self.trade6 = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.trade7 = page.locator('(//a[text()="Web Portal Trading"])[1]')

        self.trade_list = [self.trade1,self.trade2,self.trade3,self.trade4,self.trade5,self.trade6,self.trade7]


        #retailEcommerce options
        self.re_1=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.re_2=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        self.re_list = [self.re_1,self.re_2]

        #Healthcare options
        self.hc_1=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.hc_2=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.hc_list=[self.hc_1,self.hc_2]

        #fintech options
        self.fin_1=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.fin_2=page.locator('(//a[text()="Crypto"])[1]')

        self.fin_list=[self.fin_1,self.fin_2]


        #Custom App options
        self.cust_1=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.cust_2=page.locator('(//a[text()="HRM Development"])[1]')
        self.cust_3=page.locator('(//a[text()="Travel"])[1]')
        self.cust_4=page.locator('(//a[text()="Dating App Development"])[1]')
        self.cust_5=page.locator('(//a[text()="CRM Development USA"])[1]')
        self.cust_6=page.locator('(//a[text()="CRM Development"])[1]')
        self.cust_7=page.locator('(//a[text()="ERP App Development"])[1]')
        self.cust_8=page.locator('(//a[text()="E-Learning"])[1]')
        self.cust_9=page.locator('(//a[text()="Real Estate"])[1]')

        self.cust_list=[self.cust_1,self.cust_2,self.cust_3,self.cust_4,self.cust_5,self.cust_6,self.cust_7,self.cust_8,self.cust_9]

    def click_trading_options(self):
        for i in self.trade_list:
            self.verticals.hover()
            self.trad.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_retailEcommerce(self):
        for i in self.re_list:
            self.verticals.hover()
            self.RE.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_Healthcare(self):
        for i in self.hc_list:
            self.verticals.hover()
            self.HC.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_fintech(self):
        for i in self.fin_list:
            self.verticals.hover()
            self.Finntech.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_Custom_App(self):
        for i in self.cust_list:
            self.verticals.hover()
            self.CA.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

