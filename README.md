
# TermLine
TermLine is a little tool to generate a personal timeline to outline projects, work, and life events that might be of interest to a potential employer or client. 

## How to use
Fork the project and edit the JSON input file it should be fairly obvious! Client side rendering will read the json file and construct the timeline on the fly!

## IT IS NOT OBVIOUS!!
... Fine. Read on for more details

## How to use (detailed)
The JSON is a list of events. An `event` is represented with a dot in the timeline where `period` is represented as a line. Pretty simple. If you want an event to be represented as a line, add a end-date field OR a period field.

The format of the date is YYYY-MM-DD. If this is not formatted properlly bad things will happen.

Both `event` and `period` will have to have a title. Title is what shows beside the dot for `event` and on the line for `period`.
