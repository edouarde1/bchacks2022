## Inspiration

There is too much negativity in the world and we wanted to make it a better place.

## What it does

Our app performs positivity metrics on live conversations and copied text. Users are able to access the web app, begin a recording, have a conversation, then view the its positivity metric.

## How we built it

This app was constructed on Node.js. Inside the Node.js project folder includes all of the html, styling, and backend python code for the Voice-to-Speech collection.

The conversation recording function was developed using the AssemblyAI API for python. This script file sends and retrieves voice data from a microphone. For the purposes of this project, we used one of our computers to do this. During the recording process, we added preprocessing code onto the voice data that was being collected. The preprocessing code removed recording repetitions and unwanted whitespace data from the voice collection console.

In another python file we built our positivity score. We did this by creating a state of the art algorithm which calculates the positivity of a specified text. The algorithm is P = (numPosWords - numNegWords)/sqrt(totalWords). We found this algorithm to not only be extremely effective, but beautifully simple. The voice to speech python file is run directly from Node.js using express.

## Challenges we ran into

We ran into many challenges during this project. Our first challenge was trying to figure out how to use APIs that we had little experience using. In our original project idea we wanted to make a project that would make social media apps such as Instagram more accessible to seniors. Although we quickly ran into issues with permission issues with the social media APIs. In another project idea we wanted to monitor ski lift traffic using live location data from users. We spent a long time researching how to do this and tried testing location code in lots of environments. At one point we can to the census that cross-platform geocoordinates are not each to deal with when trying to run them in the background. Finally, the last challenge was finding an idea that was feasible and interesting for our group to accomplish. This last challenge was one we overcame when we came up with posimeter.

## Accomplishments that we're proud of

We are very proud of Stu for brining his all into this project. He carried the team with his Node.Js knowledge which stitched the entire project together. As first time hackers, we are proud to have accomplished a project as a group.

## What we learned

- Learning how to use unknown development platforms is a lot of work 
- Changing your idea helps 
- Social Media APIs suck

## What's next for Posimeter

We would like to have Posimeter hosted on the Web!
