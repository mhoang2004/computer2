//create a sever
//sever will acts as an emitter
//it will automatically emit event called 'request' each time a request hit the server

//event listener is a observer, it keeps waiting the subject will emit the event 

//Steams

/*
when we read a file using memory using stream
we read part of the data, do something with it
then free our memory
repeat until the entire file

or in youtube (instead of load all the video, the processing is done piece by piece (chunks))
=> no need to keep all data in memory and do not have to wait until all the data is available

data comes in when an http server gets a request is actually a readable stream

Streams are instances of the EventEmitter class!
=> streams can emit and listen to named events

http respone that we can send back to the client is a writeable stream

we could implement our own streams and consume them using these same events and functions 
*/