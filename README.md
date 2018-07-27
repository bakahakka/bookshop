# Test task

To bootstrap the application, `cd` into the root  folder and run
```bash
    bash bootstrap
```
The bootstrapping script will setup the local Python environment, install the requirements, migrate the database, create a superuser for project, feed the database with data from fixtures and runs the server.

To list all the Book models in the database run
```bash
    python manage.py displaybooks
```
The default order is ascending sorted by `publish_date`. If you want to specify the order, run it with `--sort=asc` or `--sort=desc` arguments.
