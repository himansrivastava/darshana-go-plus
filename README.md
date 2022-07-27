# go-plus

The test project for go plus

**Steps:**

1. Clone the repo.
1. Create & activate virtual env and install the dependencies in requirements.txt
1. run makemigrations, migrate and collectstatic.
1. create django superuser.
1. run python manage.py test to check that the tests pass.
1. goto /admin url and login to admin
1. goto /swagger to see the api documentation

**Important Points:**

1. Have made all the endpoints for the Institute api.
1. Added filter of status to the GET endpoint.
1. The fields in the model are not same as the field in the documentation as several fields are foreign keys.
1. If we want the Institute api to accept nested json, we will need the following:
    - Create new models (say for Contact Person)
    - Add institute as FK in those models.
    - Create nested serializers for those models.
    - Override the create and update methods in the serializer.
    - I have skipped these due to pausity of time.
1. Not worked on the logger yet.

**Please share your feedback**
