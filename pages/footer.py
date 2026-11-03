

class footer:
    def __init__(self,page):
        self.page=page

        #Footer
        self.web_development = page.locator('//a[@href="https://www.tranktechnologies.com/web-development-company"]')  
        self.cms_website= page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]') 
        self.ecom_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]') 
        self.custom_web = page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')

        self.uiux= page.locator('//a[@href="https://www.tranktechnologies.com/ui-ux-design-company"]')
        self.mob_app_dev = page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.responsive_web = page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.brand_identity = page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')

        self.app_dev =page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[1]')
        self.ios_app = page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.android_app = page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        self.hybrid_mob = page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.cross_platform = page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.progressive_web = page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')

        self.graphic_design = page.locator('//a[@href="https://www.tranktechnologies.com/graphic-design-company"]')
        self.logo_design = page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.banner_design = page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packing_design = page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.businesscard_design = page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')

        self.footer_list =[ self.web_development,self.cms_website, self.ecom_dev, self.custom_web, self.uiux, self.mob_app_dev,self.responsive_web,self.brand_identity,self.app_dev,
                    self.app_dev,self.ios_app, self.android_app,self.hybrid_mob, self.cross_platform, self.progressive_web, self.graphic_design, self.logo_design, self.banner_design, 
                    self.packing_design, 
                        self.businesscard_design ]


        self.facebook= page.locator('//img[@alt="Facebook"]')
        self.linkedin = page.locator('//img[@alt="LinkedIn"]')
        self.instagram = page.locator('(//img[@alt="Instagram"])[1]')
        self.pinterest = page.locator('(//img[@alt="Instagram"])[2]')
        self.twitter = page.locator('(//img[@alt="Twitter"])[1]')
        self.youtube = page.locator('(//img[@alt="Youtube"])[1]')
        self.quora = page.locator('(//img[@alt="Quora"])[1]')

        self.follow_list = [ self.facebook, self.linkedin, self.instagram, self.pinterest, self.twitter, self.youtube, self.quora]


    def footer_selection(self):
        for i in self.footer_list:
            i.click()
            self.page.go_back()

    def social_media_selection(self):
        for i in self.follow_list:
            with self.page.context.expect_page() as new_page_info:
                i.click()
                new_tab = new_page_info.value
                new_tab.wait_for_load_state("load")
                new_tab.close()

        
