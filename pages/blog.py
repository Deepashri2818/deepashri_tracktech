class blogs:
    def __init__(self,page):
        self.page = page
        self.Blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        self.AD = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
        self.AI = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.CM = page.locator('//a[normalize-space()="Content Marketing"]')
        self.CRM = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.DM = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.EDEV = page.locator('//li[@class="cat-item cat-item-373"]//a[normalize-space()="ECommerce Development"]')
        self.EM = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.GD = page.locator('//li[@class="cat-item cat-item-341"]//a[normalize-space()="Graphic Design"]')
        self.IT = page.locator('//a[normalize-space()="Software & IT Company"]')
        self.SD = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.UI = page.locator('//li[@class="cat-item cat-item-342"]//a[normalize-space()="UI UX Design"]')
        self.WD = page.locator('//li[@class="cat-item cat-item-339"]//a[normalize-space()="Web Development"]')

        self.Categories_list = [self.AD,self.AI,self.CM,self.CRM,self.DM,self.EDEV,self.EM,self.GD,self.IT,self.SD,self.UI,self.WD]

    # def click_blog(self):
    #     self.Blog.click()

    def click_Categories(self):
        self.Blog.click()
        for i in self.Categories_list:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()


    
