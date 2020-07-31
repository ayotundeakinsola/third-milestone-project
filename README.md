<div align ="center">
    <img src="static/img/logo2.png" width="200" height="200" target="_blank" rel="noopener" alt="AR Agency Logo" aria-label="AR Agency Logo"/>
</div>

## Introduction

<div>
    <img src="static/img/tagline.png" target="_blank" rel="noopener" alt="AR Recruitment Agency" aria-label="AR Recruitment Agency"/>
</div>

<hr>

[AR Agency](https://ar-recriutment-agency.herokuapp.com/) was created by both Ayo Akinsola and Ruth Dara-Akinsola to help organizations grow by finding the right talents. 
Talents that really match the corporate culture. We believe that this is the basis for a long-term relationship. 
If talents believe in what you believe, it is possible to build a strong brand and achieve structural growth.

## Table of Contents
1. [UX](#ux)
    - [Objectives](#objectives)
        - [Visitor Objectives](#visitor-objectives)
        - [Business Objectives](#business-objectives)
        - [AR Agency Objectives](#ar-agency-objectives)
    - [User Stories](#user-stories)
        - [Visitor Stories](#visitor-stories)
        - [Business Stories](#business-stories)
    - [Wireframes](#wireframes)
    - [PDF](#pdf)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Elements on every Page](#elements-on-every-page)
        - [Home Page](#home-page)
        - [Activities Page](#activities-page)
        - [Listing Page](#listing-page)
        - [Create Account Page](#create-account-page)
        - [Log In Page](#log-in-page)
        - [Account Settings Page](#account-settings-page)
        - [Account Page](#account-page)
        - [Add new Listing Page](#add-new-listing-page)
        - [Preview Listing Page](#preview-listing-page)
        - [Edit Listing Page](#edit-listing-page)
        - [Contact Page](#contact-page)
        - [404 Page](#404-page)
        - [Permission Denied Page](#permission-denied-page)
    - [Features Left to Implement](#features-left-to-implement)

3. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Storage Types](#data-storage-types)
    - [Collections Data Structure](#collections-data-structure)
        - [Users Collection](#users-collection)
        - [Activities Collection](#activities-collection)

4. [Technologies Used](#technologies-used)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)

7. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

8. [Contact](#contact)

9. [Disclaimer](#disclaimer)

----

# UX

## Objectives

### Visitor Objectives

The central target audience for AR Agency are:
- Stdents looking for a student jobs.
- Dutch/English speaking candidates.
- High Skilled Migrants.
- Graduates.

User Objectives are:

- Job seekers have a place to search for jobs in the Netherlands, that offers its listings in both Dutch & English.

- Employers can have access to best candidates. 

- Saves time of both Employers and prospective candidates.

- Job seekers would be helped through the application process. 

- Candidates can be sure they have access to more opportunities.

- Users can have their data stored so they can be contacted for jobs at anytime. 

AR Agency is a great way to meet user needs because:

- AR recruitment agency has access to the best talent available.

- AR recruitment agency saves time because they take care of the initial steps in the hiring process. 

- AR Recruitment agency conducts background checks on candidates, which is essential when considering potential employees.

### Business Objectives 

- Searching for specialised & executive roles.

- Fulfil both short & long term needs.

- Provide a pipeline full of talent to make business decisions.

- Recruiting agencies are partners, not foes.

Business User objectives are:

- A well thought-out, well designed, user-friendly platform that will benefit sell the core function of AR Agency.

- A user interface that is user friendly manage data easily, efficiently & effectively.

- Value creation. Having an online presence to market AR Agency properly.


### AR Agency Objectives

- Provide access to key strategic skills

- AR recruitment agency can speed up the time it takes to find a new employee

- Offer specialist knowledge by telling you what the job market currently looks like and also also let you know how to best achieve your recruitment needs.

- The data management structure has been put in place to manage data and make sure what is provided fits the needs of the database structure.

- The listing page can only be edited by logged in users who post a job. 

- The listing page for the business user shows all their existing listings and gives them the option to view, edit or delete them from this location. 

- THe site offers the business user links and buttons to make navigation easy. 



## User Stories

### Visitor Stories

As a visitor to AR Agency I expect/want/need:

1.  I would like the app to be easy to use.

2.  I would like to easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it. 

3.  Be able to register to have my own profile.

4.  I would like to be able to delete my job posting and all content added by me at any point.

5.  I would like to be able to edit my job posting and all content added by me at any point.

6.  As a user of AR Agency, I expect to be able to easily get in contact via a contact form.

7.  I would like to post the books that I own and want to buy on a online database

8.  As a user accessing this site from a mobile phone or tablet, I want the site to have been designed responsively so that it is still easy to navigate and use on my smaller devices. 

9.  As a user, I would like to view the books that I have added.

10. Be able to browse and navigate information easily.

### Business Stories

1. To be able to log in to access my existing vacancies, and for my data to only be editable with my account.

2. To create, edit and delete vacancies in my account.

3. Forms for inputting my data to make the process easy, that there is no wasting my time or making the process difficult or slow. 


## Wireframes

The wireframe was created using [Figma](https://www.figma.com/) during the conceptul phase and project proposal to my mentor. 

You can find the wireframe [here](https://1drv.ms/b/s!AqARRU4jO5elunG2T1AiA9FteWuU?e=YpZqiG).

### PDF
- [AR Agency Database Schema]()

This document was created during the planning phase of this project. The final website has some slight differences from what was planned. 
But I included this document in the project to provide insight into the original planning and direction of the site during the planning stages.  


# Features
 
## Existing Features

### Elements on every page
- Navbar
    - The navigation bar features the AR Receuitment logo in the top left corner.

    - For visitors to the site, list items links are available for them to use.
        1. Home
        2. About
        3. Employers
        4. Contact
        5. User icon(this is a dropdown menu)
            - Log in
            - Sign up

    - For users who are logged in, the list items are as follows: 
        1. Home
        2. About
        3. Employers
        4. Contact
        5. User icon(this is a dropdown menu)
            - Log out

    - Python determines if the user is logged in or not by checking `if 'user' in session` and passes this data to Jinja to display the correct navbar for the user.

    - The navbar is collapsed into a hamburger icon on mobile view.

- Footer
    - The footer features:
        - Links to social media locations (which are facebook, twitter, linkedin and youtube ).
