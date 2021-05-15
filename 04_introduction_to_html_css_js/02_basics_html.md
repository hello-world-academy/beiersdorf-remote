# Basics HTML

[Hypertext Markup Language (HTML)](https://en.wikipedia.org/wiki/Hypertext_Markup_Language)  is not a programming language in the strict sense. It is rather a markup language that describes the structure of a web page. The basic building block of HTML is the so-called _element_. It allows content to be structured and provided with attributes.   

## Elemente

An element can contain text, data, images, etc.. Typically an element starts with an opening tag `<...>`, contains attributes, encloses text and ends with a closing tag `</...>`.

Here is an example of a `p` (_paragraph_) element: 

`<p>class="abcd">Hello world!</p>`, 

- `<p>` opening _day_,
- `class="abcd"` an attribute and its value,
- `'Hello world!'` Text and the
- `</p>` closing _day_

There are also elements that have no content (_empty elements_):

`<img src="mypath/image.png">`

This element contains an attribute but no closing tag (`</img>`) and no content.

### Texts

#### Headings
Heading elements make it possible to display individual text passages as headings of different sizes. HTML contains 6 predefined sizes (`<h1>`–`<h6>`).

```
<h1>Heading 1st order</h1>
<h2>Heading 2nd order</h2>
<h3>Heading 3rd order</h3>
<h4>Heading 4th order</h4>
<h5>Heading 5th order</h5>
<h6>Heading 6th order</h6>
```

#### Paragraphs 
The `<p>` element identifies a paragraph.

```
<p>I'm a paragraph</p>
```

### Images

The `<img>` element inserts image files into the document. The `src` (_source_) attribute refers to the path to the image file (a local file or a _url_).

`<img src="images/my_image.png">`


## The anatomy of a HMTL document

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Coding Workshop</title>
  </head>
  <body>
    <img src="image/Beiersdorf.png">
  </body>
</html>
```

* `<!DOCTYPE html>` The document type. A historical artifact that corresponded to a (best-practice) standard in the early 90s. 
* `<html></html>` The `<html>` element. The element includes the entire content (_root element_).
* `<head></head>` The `<head>` element. This element corresponds to a container in which everything relevant can be found that is not part of the content displayed on the web page.
* `<meta charset="utf-8">` The element describes the character encoding used.
* `<title></title>`  The `<title>` element. It describes the title of the web page that is displayed by the browser in the tab and is also used as the name of the page when it bookmarked.
* `<body></body>` The `<body>` element. This element contains all the contents of the website that are displayed to the user (text, images, videos, games, etc).

***
## Exercise 1

> __Create an HTML document with the following contents:__
> * Define the title of the browser tab as `Coding Workshop`.
> * Create a document heading `Coding for non-coders`.
> * Create a paragraph and document today's date `Date 2019-09-25` 
> * Add an image. This can be found under the path `images/BDF_Logo.png` or the url `https://hello-world.academy/wp-content/uploads/2019/09/BDF_Logo.png`
> *  Please use the template `04_introduction_to_html_css_js/html//01-html-exercise.html`. Open this file with a text editor of your choice and fill the empty lines. At the same time you may open this file with a browser of your choice to see your progress. 


***

## Exercise 2
> __Open the HTML document `04_introduction_to_html_css_js/html/02-html-exercise.html` with a text editor of your choice look at the changes to the previous version and try to imagine what the difference may look like.__
> * The element `<ul></ul>` indicates an unordered list (_unordered list_)
> * The element `<li></li>` indicates a list entry (_list_)
> * The element `<a></a>` represents a link (_anchor_)
> * Only after you have an idea about the appearance of the website, open the file with your web browser (usually by double-clicking).