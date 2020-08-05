# Associations

## Intro to Associations

Associations allow us to have multiple pieces of data/collections in our DB to be related to one another. A single datapoint or collection might be useful in its own way, but to leverage and maximize it's use requires interactions with other collections of data. In the context of web applications, we might have a list of registered users for a certain blog for example. These users might leave comments on certain posts on the blog. These are all datapoints that are all related to each other. But within the database, they might be seperated (A user record might be recorded in a _user_ collection, while comments are recorded in a _comment_ collection). 



Continuing with this example of _users_ and _comments_, we can elaborate on the 3 basic types of data associations that exist. Suppose the blog was now a forum of racecar enthusiasts. Each user has one and only one homepage where they could post photos of their favorite petrol-guzzlers, and other users could leave comments like _"Oh my days, what a marvel of human engineering"_. In this context,  a _user_ record within the forum's database relates to a single homepage. Because this homepage belongs to the user and the user only (no other users can change what information is contained in the homepage), this is a _one-to-one_ association. A _one-to-one_ association, as the name suggests, is when a single datapoint in a collection is related to only one other datapoint in another collection. This association goes both ways as well, i.e. datapoints on the other collection is also related only one datapoint each on the initial collection.



Now, a single user might visit the homepages of other users within the community and leave comments on how stunning or beautiful the pictures. 




