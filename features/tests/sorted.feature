# Created by HP at 8/12/2021
Feature:  User can work on Gettop website
  # Enter feature description here


  Scenario: User can sort products by average rating
     Given Open Gettop Website
     When Verify User can sort products by average rating
     When Verify 1st product has rating starts displayed after sorting
     When Verify User can click through product pages after sorting is done (1, 2, > buttons under product catalog)
     Then Verify Url https://gettop.us/shop/?orderby=rating opens page with results sorted by Rating




