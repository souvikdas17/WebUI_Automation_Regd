Data folder--
Data folder contains Configuration.py file which has all the data such as Web_url, Endpoints and data necessary for registration or logging in.

Locators folder--
Locator folder contains the Web locators of the website which is being automated.

Pageobjects--
Pageobject folder contains the functions which are required to perform actions in the page such as filling, deleting and authenticating fields.

Utilities--
Utilities folder contains the Wait_Util function which is being used explicitly during the execution of test cases.

Conftest.py--
Contains the functions used for filling all the details into the page, removing or skipping details as well as checking details in the page. 
It contains all the actions of the test cases encapsulated in a function for easier use in test files.

test_registration.py--

Test case 1 :- Successful Registration
Steps:
Open the registration page.
Enter a valid username, email, and password.
Click on the Register button.
Verify the success message and redirection to the login page.
Expected Result:
User is registered successfully, and a confirmation message appears.

Test Case 2 :- Register with Existing Email
Steps:
Enter an email that is already registered.
Fill out other fields and click Register.
Expected Result:
Registration fails with an error: "Email already in use"

Test case 3 :- Weak Password Validation
Steps:
Enter a weak password (e.g., 12345 or password).
Click Register.
Expected Result:
Error message: "Password must contain at least 8 characters, including letters and numbers."

Test Case 4 : Missing Required Fields
Steps:
Leave email, password, or username blank.
Click Register.
Expected Result:
Form validation should display: "This field is required."

Test Case 5 :- Invalid Email Format
Steps:
Enter an invalid email (e.g., user@com, test@.com).
Click Register.
Expected Result:
Error message: "Please enter a valid email address."
