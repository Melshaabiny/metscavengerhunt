Forum
*****

The application that handles all of the forum and community related tasks is named **forum** app in our system. The tasks it handles are

	1. Rendering layout

		- The view that handles this task is **forum.views.thread_layout**. It handles all types of threads with their description and total number of posts in each thread.

	2. Submiting posts to thread page
	   
		- **forum.views.submit** handles this task. It takes the title and description of the post that a user creates, sent by angularjs with $http.post method. This function should handle data saving into thread model.

	3. Rendering posts
		
		- **forum.views.post** function handles rendering the page with the requested post information.

.. include:: ./forum/doc_forum.rst
