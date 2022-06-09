# Ur-Gram

An Instagram-like image gallery app, generated with [Python](https://www.python.org/) version 3.8.13 for [Django](https://www.djangoproject.com/) version 4.0.5 

# Ur-Gram
#### This repo creates an Instagram-ui-inspired app with user functionalities to sign in, upload photos, see user/other profiles, follow other users & see their photos, like photos & drop comments.
## Author
[Benson Langat](https://github.com/benie254)

## Description

If you have used Instagram, you will find Ur-Gram quite similar in appearance and in most functionalities. The Ur-Gram app displays photos posted by different users at different times. Users can click on images to expand its view in an image details page. Users can also views the images they have posted, in the user account profile. On top of these, is a functionality to copy an image's link and share in across social platforms, a search functionality, and options to comment and/or like photos.
>The app supports `CRUD` functionalities to Create, Read, Update, and Delete images and their content/details. 


## Screenshot--Home Page

<img src="https://user-images.githubusercontent.com/99865051/172786953-de327a20-46b2-4da7-b754-1dcfcd1a0bb8.png" >

## Screenshot--User's Account

<img src="https://user-images.githubusercontent.com/99865051/172787060-f28a81e7-78c6-4831-bad3-c4e580d4690c.png">


## Behavior Driven Development--BDD

**1. Home Page**
   - OUTPUT: 'Navbar', 'Home page content'
   
**2. User Action:** 
   - INPUT:  Click : Navbar : 'Ur-Gram', Home-icon
   - OUTPUT: Home page
   - OUTPUT: All Images

**3. User Action:**
   - INPUT:  Click : Image object
   - OUTPUT: Redirect: Single image details page
   - INPUT:  Click : Navbar: 'Ur-Gram', Home icon
   - OUTPUT: Home Page

**4. User Action:**
   - INPUT:  Input : Navbar : 'Enter a search term',
   - OUTPUT: Image results--image results page

**5. User Action:**
   - INPUT:  Click : Navbar : Icon: Icon-rep-profile
   - OUTPUT: User profile page: Profile photo, user details, bio, user photos
   - INPUT:  Click : 'Update p-pic'
   - OUTPUT: Profile image upload form
   - INPUT:  Click: 'Add bio'
   - OUTPUT: Bio update form

**6. User Action:**
   - INPUT:  Click : Browser Page : Close
   - Exits


## Setup/Installation Requirements

* To use this open-source repo, clone it; to contribute, fork it. 
* Open your Terminal (CTRL + ALT + T on Ubuntu/Linux). 
* Make a destination directory in your preferred path (where you would like to clone the repo into.)
* Run the command ``` cd yourDestinationDirectory ```
* Run the command ``` git clone https://github.com/benie254/Ur-Gram.git ``` to clone the repo into your destination directory. 
* Run the command ``` cd Ur-Gram ``` to move you into this repo's directory.
* Run the command ``` atom . ``` for Atom or ``` code . ``` for VSCode --opens the directory in your preferred code editor. (it is okay if you use something different.)
* Happy coding!

## Known Bugs

No known bugs. Please report any issues or encountered bugs! 

## Technologies Used

* [Python](https://www.python.org/) 
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)

## Other Resources 

* [Bootstrap](https://getbootstrap.com/) 
* [Adobe Color Wheel](https://color.adobe.com/) 
* [Coolors](https://coolors.co/) 
* [Google Fonts](https://fonts.google.com)


## Support and contact details

Reach out with any issues, concerns, or contributions to [Benie-throughMail](davinci.monalissa@gmail.com)

### License

*Copyright (c) 2022* ***Benson Langat***

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*

###
Copyright (c) 2022 **Benson Langat**

[Python](https://www.python.org/) version 3.8.13
