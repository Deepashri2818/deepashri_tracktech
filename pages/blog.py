class blog:
    def __init__(self,page):
        self.page=page

        self.blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

        self.app_development= page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')

        self.artificial_int= page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"])[1]')
        self.content_making = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"])[1]')

        self.crm_development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"])[1]')

        self.digital_marketing = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"])[1]')

        self.ecom_development= page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')

        self.email_marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')

        self.graphic_design = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')

        self.software_it_comp= page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')

        self.software_dev = page.locator ('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')

        self.ui_ux = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')

        self.web_devlopment = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')

        self.categories_list = [self.app_development, self.artificial_int, self.content_making, self.crm_development,self.digital_marketing,self.ecom_development,self.email_marketing, 
                                  self.graphic_design, self.software_it_comp,  self.software_dev,self.ui_ux,self.web_devlopment  ]


    def categories_selection(self):
        self.blog.click()
        for i in self.categories_list:
            i.click()
            self.page.go_back()

            


