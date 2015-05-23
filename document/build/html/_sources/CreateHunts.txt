Create Hunts
************

The application that handles all of the create hunts related tasks is named **cr_hunt** app in our system. The tasks it handles are

	1. Rendering main page

		- The view that handles this task is **cr_hunt.views.render_main**. It handles the create hunt process, rendering template with appropriate forms and content.

	2. Rendering add title and starting location page
	   
		- **cr_hunt.views.render_ats** handles this task. It renders a page that prompts the user to add a title for their hunt and a starting location.

	3. Rendering add item page
		
		- **cr_hunt.views.render_aitem** function handles rendering the page that allows the user to choose an item from our items collection.

.. include:: ./cr_hunt/doc_cr_hunt.rst
