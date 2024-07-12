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