# Basics JS

[JavaScript (JS)](https://en.wikipedia.org/wiki/JavaScript) is a programming language that adds dynamics, interactivity, and responsiveness to web pages.

JavaScript is very versatile. Developers can fall back on a multitude of tools and extensions and thus significantly extend the core functionality of JS.

It is basically possible to write JS code directly into the HTML document. But, similar to inserting CSS, it is recommended to simply add a reference to a JS file in the HTML (shortly before the _tag_ `</body>`). 

`<script src="the-path-to-the-file/name-js-script.js"></script>`

***

## Exercise 6

> __Change the document title to `'Hello World Academy'` using JS code__
> * Open the HTML document `04_introduction_to_html_css_js/html/04-js-exercise.html` with a text editor of your choice.
> * Open the HTML document `04_introduction_to_html_css_js/html/04-js-exercise.html` with a browser of your choice.
> * Open the JS script `04_introduction_to_html_css_js/html//scripts/header_changer.js` with a text editor of your choice.
> Add the following two lines of JS code to the `header_changer.js` file and save it.
>```
>var myHeading = document.querySelector('h1');
>myHeading.textContent = 'Hello World Academy';
>```
> * Add `<script src="scripts/header_changer.js"></script>` to the HTML document `04_introduction_to_html_css_js/html/04-js-exercise.html` and save the changes.
> * Update the browser.

### What happened?

* The heading has been changed to 'Hello World Academy' using JS.
* The `querySelector()` function referenced the heading and stored it in a variable (`myHeading`).
* Then this variable (a JS object) was overwritten with the new title (`textContent` property).
* Go to the browser and display the _source code_ (right mouse button). You will see that the HTML document is unchanged and the JS code made the change dynamically.   

***

## Exercise 7

> __Open JS file `04_introduction_to_html_css_js/html/scripts/image_switcher.js` and try to understand what the JS script does__
> * Open the HTML document `04_introduction_to_html_css_js/html/05-js-exercise.html` with a text editor of your choice.
> * Open the HTML document `04_introduction_to_html_css_js/html/05-js-exercise.html` with a browser of your choice.
> Click on the _Beiersdorf_ logo. 
> What happened?

***