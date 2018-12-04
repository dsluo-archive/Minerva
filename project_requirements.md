Requirements:

* (10) **User Management/Authentication**
    * (1) Password hashing + salting
    * (6) Settings View
        * (2) Set up 2-Factor Authentication - similar to Arch Duo, using text, email, or Authy/Google Authenticator
        * (2) Changeable Usernames - if a user wants to change their username, they can do so from a settings option.
        * (2) Change Passwords
    * (3) Login/Registration View
        * Include password reset link - If a user forgets their password, they can request an email with a reset link.
* (10) **General frontend**
    * (3.3) Responsive - the page adapts to display sizes.
    * (3.3) Modern design - CSS, the whole shebang. Pretty, please.
    * (3.3) Templates - the project uses Jinja2 templates.
* (20) Implement a **Schedule View** that displays currently planned classes and potential new classes. For student users, this is the main view of the website.
    * (6) Main interface.
    * (4) List of available classes, retrieved by AJAX.
    * (4) Filter classes by credit hours, duration, prerequisites, retrieved by AJAX.
    * (3) Disallow (or warn) of overlapping classes.
    * (3) Notifications by text/email - if on a class waitlist, users can be notified of class openings by text or email.
* (15) **Bulletin View** that displays detailed information about a Class.
    * (6) Main interface
    * (3) Add class to schedule, if there are no issues with registering for it.
    * (6) Prerequisite tree view - shows prerequisites required for a class in a dependency tree.
* (10) **Database**
        * Models representing:
        * (3.3) Courses
            * CRN
            * Subject Area
            * Course Name
            * Lab?/Honors?/Graduate?/Online?/Service?
            * Credit Hours
            * Semesters offered
        * (3.3) Course sessions
            * Class one-to-many relationship
            * Meeting times
            * Meeting location
            * Instructor (ID)
            * Max seats
            * Filled seats
        * (3.3) Users
            * One-to-one relationship to Django User model (that handles authentication)
            * ID
            * First Name
            * Last Name
            * User Groups
                * Administrator
                * Instructor
                * Student
            * Permissions
            * Courses - many-to-many relationship with associated Courses
* (5) **Back end API** to list/filter classes
    * For Ajax on front end
* (10) **Admin**
    * (4) View in-demand classes
    * (4) Add/remove classes and sessions
    * (2) Manually initiate password reset process