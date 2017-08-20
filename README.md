# bloodbank2
A django sample application which show how to create a simple CRUD application with master-detail style. In this application, there is a master (bloodgroup) and detail (patient).

When clicking bloodgroup link it move to the detail page and  in that page list of patient related to the particular group shows. editing and deleting will move back to the same page

For retrunig page we have to use a special success_url function in the PatientDelete class.

