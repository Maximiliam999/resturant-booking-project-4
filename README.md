# Mutatio

Mutatio is a website designed for the restaurant Mutatio. It incorporates a booking system where the users booking information is saved to a database so that reservations can be made, and also cancelled. It also includes a starter page with navigation, a javascript carousel, and a brief history of the restaurant. Menu page is also available for users to see what the resturant offers, making the choice if they should come eat easier. In the footer there is an address to the location of the restaurant and contact information if the users have any questions. 

![Screenshot of am i responsive](/static/images/am_i_responsive_mutatio.png "check responsiveness on diffrent screen sizes")

## Features

- Navbar 
    - At the top of the page for the user to redirect between all pages and see opening times for the restaurant

![screenshot of title at the top of the screen and nav](/static/images/nav_screenshot.png "Navbar")

- Carousel 
    - Shows the user the quality promises made by the restaurant by having a button to click through to next or previous promise

![Screenshot of the carousel that lets you click through quality promises made](/static/images/java_carousel.png "promises carousel")


- History 
    - The area displays information about the origin of the restaurant so customers can see how long the restaurant has perfected it's food.

![Screenshot of the history of the restaurant](/static/images/history_mutatio.png "history of the restaurant")

- Menu

    - This area is what allows the user to see what they can order if they come to the restaurant.
    - There is three sections. Starters, main-course and dessert.  

![Screenshot of the menu starters](/static/images/starters_mutatio.png "menu starters")
![Screenshot of the menu main-courses](/static/images/main_course_mutatio.png "menu main-courses")
![Screenshot of the menu dessert](/static/images/dessert_mutatio.png "menu dessert")



- Booking
    - For the user to create a booking instance by selecting a time, date, number of guests, name, phone and email. The information is then saved in the database

![Screenshot of form used to create a booking instance](/static/images/booking_mutatio.png "booking form")

-  Cancel Booking
    - For the user to cancel a booking instance by entering the name and phone used to make the reservation. The information is then deleted from the database.

![Screenshot of form used to cancel a booking instance](/static/images/cancel_reservation.png "cancel reservation form")

- Footer 
    - Contains the address to the Restaurant.
    - Contains ways to get in touch via phone or email. 

![Screenshot of the footer](/static/images/footer_mutatio.png "Footer with address and get in touch section ")

## Features left to implement
- Add google maps API with restaurant location for users to more quickly get help finding it
- Add list of drinks to menu 

## Running Tests
- Mutatio Site
    - The site tested on and works on both Google Chrome,  Microsoft Edge  And safari 
    - Works on all screen sizes tablet, cellphones and laptops.

![Screenshot of choices on phone](/static/images/small_phone.png "choices as seen on or phone")

- Booking
    - Booking has python testing on the views and forms. Done with unit testing and TestCase import from django.test. 
    - Tested on diffrent screen sizes, making the form wider or thiner depending on size. 
    - Manual testing done on the logic making sure a booking instance, if valid is sent and saved on the database. If not it states what the issue is, for example forgot to check box or date already booked full. 

- Cancel Booking
    - Cancel Booking has python testing on the views and forms. Done with unit testing and TestCase import from django.test.
    - Tested on diffrent screen sizes, making the form wider or thiner depending on size. 
    - Manual testing done on the logic testing if information put in the form matches one in the database, it's removed. If not it pops up a message for the user saying there is no match in the database.

- Home
    - Home views has been tested with unit testing and TestCase import from django.test checking respond code and that it contains the expected information.
    - It has been tested and works on diffrent screen sizes such as desktop, laptop, tablet and phones using am I responsive website and manual checking on diffrent devices.

- Menu
    - Menu views has been tested with unit testing and TestCase import from django.test checking respond code and that it contains the expected information.
    - It has been tested and works on diffrent screen sizes such as desktop, laptop, tablet and phones using am I responsive website and manual checking on diffrent devices.

- Carousel
    - JavaScript Carousel has been tested using jshint testing and manual testing. 
    - It has been tested and works on diffrent screen sizes such as desktop, laptop, tablet and phones using am I responsive website and manual checking on diffrent devices 

## Lighthouse testing
![Screenshot of lighthouse test](/static/images/lighthouse_testing.png "Result of lighthouse testing")

## Validator Testing 

- HTML 
    - No errors were found when passing through the official W3C Validator. https://validator.w3.org/
![Screenshot of w3 validator test](/static/images/html_testing.png "Result of w3 validator testing")

- CSS
    - One error found when passing through the official W3C Validator , Deprecated media feature max-device-width. For guidance, see the Deprecated Media Features section in the current Media Queries specification. I have manually tested this and it was the only work around for fixing a media query issue on my own device.
    https://jigsaw.w3.org/css-validator/
![Screenshot of w3 validator test](/static/images/css_testing.png "Result of w3 validator testing")


- JavaScript
    - No errors were found when passing through the official Jshint Validator. https://jshint.com/
        - The following metrics were returned.
        - There are 3 functions in this file
        - Function with the largest signature take 0 arguments, while the median is 0
        - Largest function has 4 statements in it, while the median is 4.
        - The most complex function has a cyclomatic complexity value of 2 while the median is 2.
![Screenshotof jshint testing](/static/images/jshint_testing.png " Result of Jshint testing")

## Deployment

- This site was deployed to Heroku by following these steps.
    - Install gunicorn in your terminal with the pip3 install command
    - Create a Procfile and declere a web process by putting in web: gunicorn my_project.wsgi
    - Set DEBUG to False 
    - Add herokuapp.com to ALLOWED_HOSTS in settings file
    - Log in click new and  select a name and your region then press create app,
    - click on settings tab and in cofig vars add a key DISABLE_COLLECTSTATIC with value 1
    - Add a SECRET_KEY to config vars in settings tab
    - Add a DATABASE_URL to config vars with your database URL
    - Connect to GitHub
    - Connect your repo project
    - Click deploy Branch
    - Wait for a bit press the open app on the top of the page.
    - The link can be found here: https://restaurant-bookings-80e27fc9edb0.herokuapp.com/
## Credits

- Content 
    - Time-choices table taken from https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78

- Media 
    - The icons were taken from https://fontawesome.com/icons
    - And the font was taken from https://fonts.google.com/
    - The Images Were Taken From https://pixabay.com/sv/ and google images with the CCL option added
    - Carousel inspired by https://www.w3schools.com/howto/howto_js_slideshow.asp
    - Recipes taken from https://www.delish.com/cooking/recipe-ideas/