// pipe()

//* allow to pipe `the output of readable steam` into `the input of writeable steam`
// => fix backpressure (readable streams faster than writeable stream)

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

/*
Certainly! A web server consists of three main components: HTTPS server, application logic, and files. Let's explore each of these components in more detail:

1. **HTTPS Server:**
   The HTTPS server is responsible for handling incoming HTTP requests from clients (usually web browsers) and sending back corresponding responses. 
   HTTPS stands for Hypertext Transfer Protocol Secure and ensures encrypted communication between the client and the server to protect sensitive data. 
   The server manages incoming requests, processes them, and sends back appropriate responses.

2. **Application Logic:**
   Application logic refers to the set of instructions, code, and processes that determine how the server responds to various types of requests. 
   It's the "brain" of the web server and governs the behavior of the server. Application logic is responsible for tasks such as authentication, 
   authorization, handling database queries, generating dynamic content, and more. This logic is typically written using programming languages like Python, 
   JavaScript (Node.js), Ruby, Java, or PHP.

   Application logic often includes the use of frameworks or libraries that help developers build web applications more efficiently. These frameworks provide 
   tools for routing, handling data, rendering views, and managing sessions. Some popular frameworks include Flask and Django for Python, Express.js for Node.js, 
   Ruby on Rails for Ruby, and Spring Boot for Java.

3. **Files:**   
   Files in the context of a web server refer to static assets such as HTML, CSS, JavaScript, images, videos, and other resources that are served to the client's 
   web browser. These files contribute to building the user interface and user experience of the web application. When a client requests a particular resource, the 
   web server retrieves the corresponding file and sends it back in the response. This enables the client's browser to render the content properly.

   To manage the organization and delivery of static files, web servers often use routing mechanisms to determine which files to serve for different URL paths.
   Additionally, web servers may apply caching strategies to improve performance by storing copies of frequently requested files in memory.

In summary, a web server combines an HTTPS server for handling client requests, application logic to process those requests, and files to serve as the building 
blocks of the web application's user interface. These components work together to create a seamless and secure experience for users accessing web applications 
through their browsers.

*/

















