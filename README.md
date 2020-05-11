Dataset:
My project is the MET archive analysis report. I used the API (RESTful web service in JSON format) that provides access to all of The Met’s Open Access data. It has all of the artworks at the MET so I chose to focus on just one medium of art to help focus on a select group of data first, I chose "Paintings." From here I looked at a few different variables, to start out with, ‘Artist’, ‘Accession Year’, and ‘Gender.'

Interest:
I was curious to see what kind of data the MET has recorded about their collection, and specifically their paintings. I was also interested how many paintings the MET had with repeat artists, and how many of those had actual corresponding data entires. 


Method:
I initially grabbed all of the paintings from the online API and from there created dictionaries for the data variables that I wanted to record. This had quite a bit of trial and error, as I had to look at each object and its information separately and from here chose different variables that I wanted to compare for the entire 6,174 painting objects. I found that a lot of objects were missing common variables such as period or artist nationality. I chose to not include those entires in my final python code, as most of it was blank. For other variables like, ‘Gender,’ I found that the MET only listed a gender if the artist was female, so none of the results say ‘male.’ I had to include a try/except line to keep the code from breaking or stopping once it encountered an object with no data.  

Conclusion:
There was a learning curve to try and apply the python actions to this API, as it was very large and online only. I was able to grab quite a bit of data from its repository and also discover something unique about its data entries.  I was even able to include a statement of the percentage of the gender data the is recorded in the API data. I have a lot to learn, especially regarding charts and tables, as I could not get one to work properly. It was very interesting to see that while the api data is very sophisticated and easy to look at, especially with the Github guide, there are a lot of missing data entries- including entire works only having an object-ID. 
