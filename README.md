# Graphic Design Services

Milestone four project: Full Stack Frameworks with Django - Code Institute

This is a full stack site that allows users to manage and order a dataset about particular domain. This project highlights convinient access to the set of graphic designs, it also suppors all CRUD operations, a dashboard page that gives all graphic designs available with the site.

## Menu Page

Must have:
As a user I would like to register quickly and easily check what are the designs available in this site, also check whether this site provides the information of a design based on category that I like.

As a user I want to order a design according to my requirements/ needs.

Should have:
As a user I'd like to read about designs which look efficient and attractive.

# UX

## Strategy

My goal in the design was to make it as easy as possible to access information on the site while striving for a minimalist and user-friendly design.

## Scope

For users, I wanted to provide a brief overview of all designs within my site, also create new orders if have any, which will be later uploaded by admin. This way, many other members of the community get a glimpse about designs that they can order for and enjoy their time, with average price in the market so they can plan for order.

## Structure

I wanted users to be able to quickly access the data that is available, providing a short description, user details which provide much more information about seller. A link to dashboard, home pages for quick navigation and a overview of all designs in a single dashboard page for quick access and efficient performance.

## Surface

The bootstrap color schema was chosen to create a modern feel.

## Technologies

1. HTML
2. CSS
3. Bootstrap
4. JS
5. Python + Django
6. MySQL database

## Features

This site uses the bootstrap grid layout for better organising the content of a page. The navbar also stays regardless of the screen size to achieve quick access to pages.

# USER Perspective

# 1. Create

This site allows users to register and order designs

# 2. Access

Every user will be provided with complete information about all designs available that was shared by an admin

# 3. Order

Every registered User will be able to order a design based on their needs

# 4. Search

Users will be able to filter the designs based on the design categories for quick and efficient access

# 5. Making Payments

After ordering users will be taken to the payment page on which if purchased admin will be able to check all the list of orders I used stripe payment gateway to achieve this functionality

# Admin Perspective

# 1. Create

Site Owner will be able to add a user, add a design based on orders

# 2. Edit

Site owner will be able to modify any information which is either related to user, orders or designs

# 3. Delete

Site Owner will be able to delete any user information

# 4. Access

Site Owner will be provided with the complete information and super access

## Testing

The user and site owner achieved the intended outcome of providing them with a showcase of data. In the dashboard section, they can quickly check usefull information of a designs like image, category, seller and price, link which takes to that single design page for more information. They are able to see all list of designs via cards in dashboard section. They are also able to check appropriate error or success messages as an acknowledgement. They are also able to order data specific to a category. The application is also made responsive for a modern feel.

## Deployment

To run locally you can clone this repository directly into the editor of your choice by pasting git clone https://github.com/vinod2rahul/MS4-GraphicDesignServices.git into your terminal.

Rename the .env.example to .env and configure the keys

switch to graphic-design folder and Use command python manage.py runserver to run app locally a port 8000.

You can check it run at localhost:8000 if followed above procedure correctly.

## Credits

All content and code in this project site was writen by me.
