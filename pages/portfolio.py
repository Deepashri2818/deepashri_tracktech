class portfolio:
    def __init__(self,page):
        self.page=page
        self.portfolio= page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')
        
        self.ics_homework_viewmore= page.locator('//a[@href="https://www.icshomework.in/"]')

        self.wings_pharma_viewmore= page.locator('//a[@href="https://www.wingspharma.com/"]')

        self.arena_animation_viewmore= page.locator('//a[@href="https://arenasonipat.com/"]')

        self.home360_viewmore= page.locator('//a[@href="https://home360stores.com/"]')

        self.club_meeting_viewmore= page.locator('//a[@href]')

        self.cords_cables_viewmore= page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')

        self.portfoli_list = [self.ics_homework_viewmore, self.wings_pharma_viewmore, self.arena_animation_viewmore,self.home360_viewmore, self.cords_cables_viewmore ]

    def portfolio_selection(self):
        for i in self.portfoli_list:
            self.portfolio.click()
            with self.page.context.expect_page() as new_page_info:
                i.click()
                new_tab = new_page_info.value
                new_tab.wait_for_load_state("load")
                new_tab.close()
            
            
            

        














