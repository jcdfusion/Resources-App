# ResourcesApp

This application is intended to bring a solution to the problem of resource distribution throughout affected areas after a disaster, but more importantly to give the distributor a more clearer insight of what is really needed and where, so that the affected people can receive the help they really need.

This first phase of the project includes the basic structure and code of a flask application written in python. The application connects to a database and displays the same dummy data from such database regardless of the URL route specified.

Valid application routes include /ResourcesApp/resources, /ResourcesApp/resources/<int:rid>, /ResourcesApp/resources/<int:rname>
