Requirements:

* [ ] (10) **User Management/Authentication**
    * [x] (1) Password hashing + salting
    * [ ] (6) Settings View
        * [ ] (2) Set up 2-Factor Authentication - similar to Arch Duo, using text, email, or Authy/Google Authenticator
        * [x] (2) Changeable Usernames - if a user wants to change their username, they can do so from a settings option.
        * [x] (2) Change Passwords
    * [x] (3) Login/Registration View
        * [x] Include password reset link - If a user forgets their password, they can request an email with a reset link.
* [x] (10) **General frontend**
    * [x] (3.3) Responsive - the page adapts to display sizes.
    * [x] (3.3) Modern design - CSS, the whole shebang. Pretty, please.
    * [x] (3.3) Templates - the project uses ~~Jinja2~~ Django templates.
* [ ] (20) Implement a **Schedule View** that displays currently planned classes and potential new classes. For student users, this is the main view of the website.
    * [ ] (6) Main interface.
    * [ ] (4) List of available classes, retrieved by AJAX.
    * [ ] (4) Filter classes by credit hours, duration, prerequisites, retrieved by AJAX.
    * [ ] (3) Disallow (or warn) of overlapping classes.
    * [ ] (3) Notifications by text/email - if on a class waitlist, users can be notified of class openings by text or email.
* [ ] (15) **Bulletin View** that displays detailed information about a Class.
    * [x] (6) Main interface
    * [ ] (3) Add class to schedule, if there are no issues with registering for it.
    * [ ] (6) Prerequisite tree view - shows prerequisites required for a class in a dependency tree.
* [x] (10) **Database**
    * [x] Models representing:
        * [x] (3.3) Courses
            * [x] CRN
            * [x] Subject Area
            * [x] Course Name
            * [x] Lab?/Honors?/Graduate?/Online?/Service?
            * [x] Credit Hours
            * [x] Semesters offered
        * [x] (3.3) Course sessions
            * [x] Class one-to-many relationship
            * [x] Meeting times
            * [x] Meeting location
            * [x] Instructor (ID)
            * [x] Max seats
            * [x] Filled seats
        * [x] (3.3) Users
            * [x] One-to-one relationship to Django User model (that handles authentication)
            * [x] ID
            * [x] First Name
            * [x] Last Name
            * [ ] User Groups
                * [ ] Administrator
                * [ ] Instructor
                * [ ] Student
            * [ ] Permissions
            * [x] Courses - many-to-many relationship with associated Courses
* [ ] (5) **Back end API** to list/filter classes
    * [ ] For Ajax on front end
* [ ] (10) **Admin**
    * [ ] (4) View in-demand classes
    * [ ] (4) Add/remove classes and sessions
    * [ ] (2) Manually initiate password reset process
 
