# prototype-ChoreoGrapher
First prototype of a choreography-making application. Functionality based on OOP in Python for this version.

  The idea is to provide dancers with a program allowing easy, efficient, and collaborative creation of dance formations for choreography sets. Each dancer is represented with a customizable circle on the screen that keeps track of its own canvas location at each given Formation. 

  At the moment, each Dancer object holds a collection of different Points, indexed by the given "state" of the Choreo. My next steps are to keep refactoring all the classes to have a simpler and more efficient hierarchy among them in terms of inheritance. Something like: Choreo > Formation > Dancer > Point. 


Once I am satisfied with how each object is behaving and have integrated audio input from song files to control animation timesteps, I plan to move on to a different framework to allow for better server integration and synchronous editing. Other long-term features are:

- Being able to have a 3D view of dancers, implemented with Unity (similar to how Google Streetview puts you into a 3D, navigatable world)
- Being able to add dancers, create crews, save formations, and share them in a specific file type (similar to .PSD in photoshop)
- Being able to collab in making formations on a hosted server(google docs style)
- Being able to add notes to each formation
- Being able to adjust the time for each formation and the time for the transitions of each Dancer
- Being able to customize a pathway for each dancer, not only calculating the shortest line
- Song synchronization (similar to Audio tracks in most video editors)
