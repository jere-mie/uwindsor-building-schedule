# UWindsor Room Schedule

Shows when UWindsor rooms are in use by classes.

There are two main components to this project, the parser and the website.

## The Parser

The parser works by extracting useful information from the text of the official UWindsor Timetable PDFs, and generating a javascript file which has the data prepopulated into a handy object.

The parser should work for any term as long as the PDF format remains the same.

To run the parser for a new term, simply:

1. Grab the timetable PDF from [here](https://www.uwindsor.ca/registrar/541/timetable-information)
2. Copy and paste the contents of the PDF file into a new text file in the `data/` directory. For example, if the term is Winter 2024, create the file `data/W24.txt`
3. Edit the `term` variable in the `parse.py` file to the new term (in our above example, we would set it to `W24`)
4. Run the `parse.py` script
     - You should notice a new file, `data/W24.js` is created
5. Profit

If the format of the PDF changes, you may not get accurate results from the parser. This means you'll need to make some adjustments to `parse.py` to get it working.

## The Website

The website works by importing the appropriate JS file and searching through it to find suitable matches. To update this website for new terms, simply change which `term.js` file is being loaded. Of course, make sure you've already parsed the input for your desired term (see above).