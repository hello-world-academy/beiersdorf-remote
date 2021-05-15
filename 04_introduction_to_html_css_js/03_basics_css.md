# Basics of CSS

Like HTML, [Cascading Stylesheets (CSS)](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) is not a programming language but a _Stylesheet_ language. This can be used to format individual elements of a HTML document. To display all paragraph elements (`<p>`) in a HTML document in red text color, write the following in CSS:

```
p {
  color: red;
}
```

Usually you create a CSS file and reference it within the `<head>` _tags_ in the HTML document.

`<link href="styles/style.css" rel="stylesheet" type="text/css">`


## Anatomy of CSS 

CSS formatting is based on rules. The name of the HTML element to be formatted (_selector_) is always at the beginning of the rule. (e.g. `p`).
A rule like `color: red;` represents the selected element in the color red. The correct syntax is very important here:

* Each rule is enclosed by the curly brackets `{}`.
* The colon `:` separates the property (e.g. `color`) from the value (e.g. `red`).
* The semicolon (`;`) separates the declarations from each other.

```
p {
  color: red;
  width: 500px;
  border: 1px solid black;
}
```

There are various ways to address individual elements or groups of elements:

```
p, li, h1 {
  color: red;
}
```

You can also address individual elements in different ways:

* _Name_ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `p`
* _ID_ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `#my-id`
* Class &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.my-class`
* Attributes &nbsp;&nbsp;&nbsp; `img[src]`
* Status &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `a:hover`

Furthermore there are many more possibilities to address single elements with CSS ([see here](https://www.w3schools.com/cssref/css_selectors.asp)). 

### _Thinking in blocks_

When defining CSS rules, it can help you to think of elements of an HTML document as boxes that can exist side by side and on top of each other (_box model_). With this model in mind, properties like `padding`, `border` and `margin` are easier to understand.

<img src='_img/box-model.png' width='100%'>

****
## Exercise 3

> __Open the CSS file `04_introduction_to_html_css_js/html/styles/style.css` with a text editor of your choice and try to understand the formatting rules.__

***
## Exercise 4

> __Open the HTML document `04_introduction_to_html_css_js/html/03-css-exercise.html` with a text editor of your choice.__
> There are two small changes in the file between the _tags_ `<head>`.  
> 1. `<link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">`. Here we refer to an internet source which provides us with the font _Open Sans_.
> 2. `<link href="styles/style.css" rel="stylesheet" type="text/css">` Here we refer to the local `.css` file which contains our specific formating rules.
> * Finally, please open the file `04_introduction_to_html_css_js/html/03-css-exercise.html` with your web browser (usually by double-clicking) and try to assign the visual changes to the respective rules.
 
***