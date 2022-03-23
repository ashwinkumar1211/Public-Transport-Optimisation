Workflow of our system: 

If the appropriate buses that the people need arrive faster to them then there will be a flawless transport system and also reduces crowd for waiting for a single bus.

Thus we have decided to design a system for it.

The system includes the following steps:

step-1:

Count the passengers waiting for bus using and face counting camera in the step.

Step-2:

Bus arrives, check the bus id using plate detection and the count the persons boarding inside the bus.

Step-3:

Check the remaining count . Now we can figure out that how many people travel to the place that the above bus goes.

step-4:

If many people boarded in the bus then the buses with same id should pass through this route frequently.

Else if less people boarded in the bus then buses with random other ids are passed through this route. 


The above steps are repeated until the algorithm finds the best bus ids to pass through this route.

Every bus ids , their frquencies are registered and stored in a data base.

These data are then analysed using any supervised learning method:

Classification:

The buses or bus ids are classified based on their routes and their frequencies over the routes are classified based on day , month and season.

Clustering:

The classification results are passed to clustering where the all the 3 classifications are clustered to provide efficient result of frequencies of buses over their routes.

Finally according to the clustering reults of each day the routes of buses are designed.

Thus this will be a flawless transport system and also reduces crowds and waiting time for buses.
