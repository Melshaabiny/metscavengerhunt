Hunts
*****

The application that handles all of the hunts related tasks is named **hunts** app in our system. The tasks it handles are

	1. Rendering Hunt

		- The view that handles this task is **hunts.views.render_hunt**. It handles the hunt process, rendering template with appropriate forms and content.

	2. Rendering Clue
	   
		- **hunts.views.render_clue** handles this task. It renders the proper clue for the items.

	3. Rendering Result
		
		- **hunts.views.render_result** function handles rendering the result of the item verification process.

.. include:: ./hunts/doc_hunts.rst
