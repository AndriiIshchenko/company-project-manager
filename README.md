# Company Project Manager

Project to manage the company’s employees and tasks.

## Mission
This completely useless for commercial use project was created to train in the development of a web application based on Django and to blow the minds of my mentors.

The second goal of this project is to demonstrate to future employers that I am capable of writing something more significant than just 'Hello, world'.

## Description

This app created to make life easier for managers.
- Create project and control its execution.
- Add tasks for project and assign workers.

Each project has project manager.
Each task has his own deadline and workers.

You can control:
- how many projects in progress
- tasks finished or not 
- how many tasks has each worker
- and many other things ..




## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Must have:
- a computer with some operating system (maybe mobile phone but
a don't know how to use python on it yet)
- some free time

### Installing

A step by step series of examples that tell you how to get a development env running

1. Say what the step will be
```
git clone the-link-from-forked-repo
```
2. Open the project folder in your IDE
3. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
    ```
    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    pip install -r requirements.txt
    ```

4. Use the following command to load prepared data from fixture to test code:
    ```
    python manage.py loaddata taxi_service_db_data.json
    ```

5. After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin.user`
  - Password: `1qazcde3`


```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

