# 21st Century Piracy Phenomenon. Exploring Contemporary Sea Piracy

## Summary

In this study the main goal is to evaluate the concentrations of the modern piracy incidents around the world.
Modern-day pirates around the world share the legal designation of their historic brethren as “enemies of all mankind” because they disrupt and hinder the safe navigation of maritime vessels containing goods and people. 

Piracy is a global crime which impedes the free movement of ships containing people and goods, with its attendant economic ramifications. The perpetrators are usually heavily armed, with sophisticated weapons to enable them to hijack a vessel or vessels and redirect them to their desired location for the payment of an expected ransom.

I am using Beautiful Soup for this Python app. Beautiful Soup is a Python library for parsing data out of HTML and XML files (aka webpages). It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. 

The major concept with Beautiful Soup is that it allows you to access elements of your page by following the CSS structures, such as grabbing all links, all headers, specific classes, or more. It is a powerful library. Once we grab elements, Python makes it easy to write the elements or relevant components of the elements into other files, such as a CSV, that can be stored in a database or opened in other software.

The data I used came from Live Piracy & Armed Robbery Report 2020. Reference: https://www.icc-ccs.org/index.php/piracy-reporting-centre/live-piracy-report

## Main goal

+ To access all of the content from the source code of the webpage with Python
+ Parse and extract data. 
+ Save the info in CSV file for further analysis.

## Methodology

1. Import Modules
2. Get the URL link
3. Navigate the URL Data Structure
4. Testing out data requests
5. Write data to a file in pseudo-code:
    + Open up a file to write in and append data. 
    + Write headers
    + Clear HTML tag and insert text in array
    + Clear \r \n \t to prepare string variable to clear Narrations: and insert text in array
    + Prepare string variables Date, Time, Position, Area and Country, replace characters to insert character | and insert text in array
    + Split to elements to array results for character | and Write to file items Date, Time, Position, Area and Country
    + When complete, close the file
6. The output file in CSV format.

## Data info extracted:

Date, Time, Position, Area and Country of Live Piracy & Armed Robbery Report 2020

