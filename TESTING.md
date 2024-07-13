# Luga|Talk Testing
This is an overview of the tests conducted on Luga|Talk website to access performance evaluations, browser compatibility, accessibility assessments, cross-device testing, code validation and user story testing. Each section describes the tools used, the issues found (if any), and the corresponding test results.

## Table of Content

1. [Code Validation](#html-validation)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Python Validation](#python-validation)
2. [Accessibility](#accessibility)
3. [Performance](#performance)
    1. [Desktop Performance](#desktop-performance)
    2. [Mobile Performance](#mobile-performance)
4. [Performing tests on various devices](#performing-tests-on-various-devices)
5. [Browser compability](#browser-compability)
6. [Manual Testing](#manual-testing)
    1. [Testing user stories](#testing-user-stories)
    2. [User Experience and Improvements](#user-experience-and-improvements)
    3. [Full testing](#full-testing)
8. [Summary](#summary)

## Code Validation

### HTML Validation
[W3C Markup Validation](https://validator.w3.org/) is a tool provided by the World Wide Web Consortium (W3C) to help web developers check the validity of their HTML, XHTML, and other markup languages. It ensures that web pages conform to the standards set by the W3C, promoting best practices and improving cross-browser compatibility. Using the validator helps identify and correct errors in code, leading to more robust and accessible web content.

- On checking the whole page for HTML validation, the following errors were registered as seeen in the image below. These errors were, bad image value attribute which was rectified by moving the styles of the image to the css file, section had been used instead of a div and then defer attibute had been applied in the link element.  
<details><summary>BEFORE: HTML validation</summary><img src="/docs/validation/html/validation_before.png"></details>
<details><summary>BEFORE: HTML validation</summary><img src="/docs/validation/html/validation_after.png"></details>

All pages were validated, and the code was pasted in. I applied a filter to remove issues related to the Django templating system. 

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|base| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/base.png)</details>| :white_check_mark:
|index| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/index.png)</details>| :white_check_mark:
|about| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/about.png)</details>| :white_check_mark:
|register| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/register.png)</details>| :white_check_mark:
|login| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/login.png)</details>| :white_check_mark:
|profile| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/profile.png)</details>| :white_check_mark:
|logout| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/logout.png)</details>| :white_check_mark:

|create_blogpost| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/create_blogpost.png)</details>| :white_check_mark:
|user_blogposts| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/user_blogposts.png)</details>| :white_check_mark:
|blogpost_detail| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/blogpost_detail.png)</details>| :white_check_mark:
|blogpost_detail| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/blogpost_edit.png)</details>| :white_check_mark:
|blogpost_delete| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/blogpost_delete.png)</details>| :white_check_mark:
|remove_favorite| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/remove_favorite.png)</details>| :white_check_mark:
|delete_account| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/delete_account.png)</details>| :white_check_mark:
|400_page| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/400.png)</details>| :white_check_mark:
|500_page| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/505.png)</details>| :white_check_mark:

### CSS Validation
To validate the css code for Luga|Talk, [W3C Jigsaw](https://jigsaw.w3.org/css-validator/) was used. A tool developed by the World Wide Web Consortium (W3C), a modular web server platform designed to explore and implement web technologies. It serves as a reference implementation of the HTTP protocol, offering a customizable framework for experimenting with new standards and functionalities. As a tool that supports validation and checks for HTML and CSS code correctness. It ensures web pages adhere to W3C standards, fostering interoperability and accessibility across different web environments.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|styles.css | No errors |<details><summary>Screenshot of result</summary>![Result](/docs/validation/styles.png)</details>| :white_check_mark:
|Whole webpage | When validating the website as a whole, the validator shows warnings linked to Bootstrap v5.0. |[Result](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Flugatalk-ab90580d7f17.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)| :white_check_mark:

### Python Validation 
[PEP 8](https://pep8ci.herokuapp.com/) was used to validate the python code for the LuGa|Talk is the official style guide for Python code, maintained by the Python Software Foundation. It outlines best practices for writing clean, readable Python code, covering topics such as naming conventions, indentation, and code structure. Adhering to PEP 8 helps maintain consistency across Python projects and enhances code maintainability and collaboration.


Note: Under 'View Result' expand the image by clicking onto it to properly view detailed information and validation results.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
| settings | One URL was too long, while the other lines that exceeded the recommended length were automatically generated by Django. | ![Result](/docs/validation/pep8/settings.png) | :white_check_mark:
|luga/admin | All clear, no errors found |![Result](/docs/validation/pep8/luga-admin.png)| :white_check_mark:
|luga/app | All clear, no errors found |![Result](/docs/validation/pep8/luga-app.png)| :white_check_mark:
|luga/forms | All clear, no errors found |![Result](/docs/validation/pep8/luga-forms.png)| :white_check_mark:
|luga/models | All clear, no errors found |![Result](/docs/validation/pep8/luga-models.png)| :white_check_mark:
|luga/urls | All clear, no errors found |![Result](/docs/validation/pep8/luga-urls.png)| :white_check_mark:
|luga/views | All clear, no errors found |![Result](/docs/validation/pep8/luga-views.png)| :white_check_mark:
|users/forms | All clear, no errors found |![Result](/docs/validation/pep8/users-forms.png) | :white_check_mark:
|users/models | One line too long because of URL |![Result](/docs/validation/pep8/users-models.png)| :white_check_mark:
|users/signals | All clear, no errors found | ![Result](/docs/validation/pep8/users-signals.png)| :white_check_mark:
|users/views | All clear, no errors found |![Result](/docs/validation/pep8/users-views.png)| :white_check_mark:

[Back to the top](#table-of-content)

## Accessibility
To access the accessibility of the website, [The WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) was used to identify potential accessibility issues and provides guidance on how to improve the accessibility of web content.

The website generated no errors, not even contast errors. However there was need for accessibility improvements related to aria-labels and adjacent to each other.
(<details><summary>See screenshort</summary><img src="docs/validation/wave-testing.png"></details>)

- Removed aria-label from Blog Post Link: To improve accessibility, I removed the aria-label attribute from the blog post links. The aria-label was deemed unnecessary as it duplicated the information already present in the link text, which could confuse screen reader users. This change ensures that content is more straightforward and accessible for those using screen readers.

- Simplified Logo: Simplified the logo by removing the link from it. The logo originally linked to the same URL as the "Home" link immediately next to it, making the link redundant. By removing the link from the logo and maintaining its styling, I streamlined the navigation and reduced repetitive links, thus enhancing overall accessibility.

These changes were made to ensure a better and more accessible user experience for all visitors, including those who rely on assistive technologies.

By utilizing the WAVE tool, I obtained crucial insights into my website's accessibility. Although I have opted not to address certain issues currently, I am dedicated to ensuring an inclusive user experience. I will persist in seeking opportunities to enhance accessibility moving forward.

[Back to the top](#table-of-content)
