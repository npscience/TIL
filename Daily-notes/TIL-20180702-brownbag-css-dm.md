# CSS grid layout

Brown Bag (lunchtime) talk on css grid layout, by the wonderful @davidcmoulton :tada: thank you David!
Date: 2018-07-02
Note: this is second talk on using CSS for layout, first talk was about flexbox (retrieve notes from that, also by DM)

## Background
* what is a grid? structure of invisible intersecting lines so you can see alignment (horizontal and vertical)
* Having a grid makes it easier for designers and for collaboration (clarity and order, efficiency)
* having a grid gives you consistency (for your one brand), but if many places use it and look the same it gets boring (i.e. bootstrap) - you should use a grid intentionally to solve a problem, not fit your problem to an existing grid
* BUT it's not easy to use a grid on the web. Here's the story in brief:
  * before css, it's html using `<table>` as a hack, not semantically correct (because it's not a table!) but no alternative
  * then css --> display:table and margin, padding, etc - semantically correct as display instructions. Maintenance burden --> hence the frameworks people have made to help (but the web looks homogenous because of this)
  * last year, 20 years after css, flex box arrives! baked into css, allows you to define layout on a webpage.
  * BUT it can only deal with 1D layout, it doesn't wrap with consistent styling, so not good for 2D layout
  * NOW (Feb 2018) we have CSS Grid Layout Module Level 1 - https://www.w3.org/TR/css-grid-1 Browsers are now natively aware of the concept of a grid!!
   * we use it for layout of labs homepage, on eLife monthly archive pages, in individual patterns - experimenting as it's new and we don't want to break anything.
   * https://labs.jensimmons.com/index.html - great Moz dev who is doing funky things

## Let's try it
* Apply ```display: grid``` to an element, use feature queries to isolate from older browsers
* Talk to DM re nested grids - some options, but also caveats
simple non-responsive grid
* use `grid-gap: XX px;` to add padding (gutter) - can also specify row or column
* use `grid-template-columns: XX px XX px;` <-- two columns at XX pixels each, just extend the list to add more columns
* use `grid-template-rows: 200px 100px`<-- first row is 200px tall, second row 100px, etc - any more rows are as high as needed to fit the content (and row height will match across all items in that row, so one large item in that row will affect the other items in that row)
* use `grid-auto-rows: 200px`<-- set any implicit rows to 200px, so all remaining rows will be this. But this would not accommodate varying content sizes, so may not be good design decision

*DM: "the explicit grid is the grid explicitly defined by the CSS, the implicit grid is the rest of the grid structure that the browser creates despite not being told to, in order to accommodate any remaining grid items"*
At this point, the browser has an implicit grid and is acting based on the browser window width, i.e. it auto wraps when there are more elements than will fit the current explicit grid (column number and widths; item numbers). But it is not responsive: it won't change the number of columns as the window width is changed. Instead, if there are three columns of X width and your window is too narrow, then you need to scroll left and right to see the whole width.

For responsive CSS:
```
display: grid;
grid-gap: 20px;
grid-template-column: 1fr 1fr 1fr
```
This new fr unit represents a fraction of the available space. It subtracts the gap widths from the total width of the element that's specified in the grid (could be the browser window width, or the container within which it sits) then divides remaining space between the number of fraction units, and assigns those widths to the columns. Here all are 1 fr, so equal widths. You can specify one columns width and leave the rest to scale (you can mix fr and px).

You can also use `minmax(200px, 1fr)` to specify a minimum and maximum width, and this can be quite complex: `grid-template-columns: minmax(200px, 1fr) 2fr 300px;`

For many columns, you can simplify using `repeat(x, 1fr 2fr)` <-- repeat x times the 1fr 2fr pattern

You can use autofill within repeat function, so that the number of columns changes according to browser window space: `grid-template-columns: repeat(autofill, minmix(150px, 1fr));`
* columns will be minimum 150px will be equal fractions of remaining space. Once another column can be included in a row, it will be and will fill with the items.
* autofit will stick to same number of columns and just expand to fill the width (so contact column number); autofill will create new column spaces as more space becomes available (so variable column number).

Qs:
* can you set the order of priority for the items? so some stay at top if the narrow window with many rows? can with flexbox, DM unsure if with this, but take care easy to break accessibility (readers, etc) when you start messing with rules like this.
