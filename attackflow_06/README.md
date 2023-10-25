# Attack Flow 6

## Project Vision

Cyber attacks have become an increasingly prevalent fear in the modern age, with numerous businesses
having been targeted and many ordinary people being affected. Given the wide variety of techniques and
procedures employed to compromise a system, there exists a need to catalog the sequence of attack steps.
The Massachusetts Institute of Technology Research and Engineering (MITRE) Center for Threat-Informed
Defense has developed the open-source attack flow framework, Attack Flow. By capturing the sequence of
attack steps, contextual information, and relationships, it bridges the gap between attack behaviors and defender strategies. This improvement in the information available allows for the enhancement of cyber security
measures.

Our vision for this project then is to improve the means in which attacks can be moved into this Attack
Flow framework (both by annotation and movement of information into the standardised format), along with
providing a UI which can better serve to visualise the attack flow after it has been moved into the framework.
The project is restricted to information which belongs in the attack flow framework, with the expectation
being that the information must be brought into a form which is considered of a high enough quality to be
validated and then moved into the MITRE project’s publicly available database.

# Project Objectives

The primary objectives of this project are as follows:

1. **Document Annotation Support**:
   - Users should be able to upload incident report documents, such as MS Word or PDF files.
   - Annotate these documents manually with multiple tags and codes, which can be both pre-defined and user-defined.
   - Annotated documents must be stored for future reference.
   - Implement document version control to track changes made by different users.

2. **Standard Dataset Generation**:
   - Automatically map the annotated data to a standardized format specified by the user.
   - Maintain a record of the incident report document along with the generated data file.
   - The client will provide the standardized format during the initial stages of the project.

3. **Attack Flow Visualization**:
   - Develop a user interface (UI) to effectively visualize attack flows, enabling users to study attack flows in detail.
   - Implement a feature to visualize attack flows using the generated data files.
   - Reference: [Sample Visualization](https://github.com/center-for-threat-informed-defense/attack-flow)

4. **Validation**:
   - Thoroughly validate the system functionalities by creating at least one "to be inserted" attack flow file.
   - Obtain client approval after validating the system's capabilities.

## Coding Standards

Coding standards are defined to provide a unified structure for the code, allowing for easier work between
members by ensuring they are better able to interpret the code developed by others. The areas defined are:

- Style of format of headers for modules:
   * Name of the module.
   * A description of the functionality of each module and its connection with other modules.
   * Contributor’s name followed by student ID.
   * Date of creation.
   * Date of last modification.
- Naming conventions:
   * Keep variable and function names short, meaningful and easy to understand.
   * Mention the scope of the variable where applicable (e.g. Global, local, constant).
   * Snake case for functions (snake case).
   * Camel case for variables (camelCase).
   * Screaming snake case for defines (SCREAMING SNAKE CASE).
- Commenting:
   * Put comments where necessary for others to understand.
   * Keep comments readable and easy to understand; short but precise.
- Code block indentation:
   * Consistent spacing after function arguments (one space).
   * Consistent indentation between code blocks and functions.
   * Braces placed in a new line.

## Tech Stack

- HTML, CSS, JS, Vue.js
- Flask 
- Graphviz
- MongoDB

## How to Contribute

We welcome contributions from the community to help achieve the project's goals. Here's how you can contribute:

1. **Clone the Repository**: Start by cloning this repository to your local machine.

2. **Familiarize Yourself**: Read the documentation and codebase to understand the project's structure and requirements.

3. **Work on Issues**: Check the [Issues](link-to-issues) section for tasks that need attention. Assign yourself to an issue you'd like to work on.

4. **Create a Branch**: Before making changes, create a new branch dedicated to your contribution.

5. **Code and Test**: Implement your changes, following best practices. Make sure to test thoroughly.

6. **Submit Pull Request**: Once your contribution is ready, submit a pull request. Provide a clear description of the changes you've made.

## Getting Started

❗ You must have [Docker](https://docs.docker.com/get-docker/) installed in your computer first.

Open the Docker app to keep the docker engine running before proceeding.
After cloning the repo, open terminal in the repo folder and run docker with this command: 

```
docker compose up
```

✔All done and have fun coding φ(゜▽゜*)♪

🔥 hot reload is implemented, just edit the code and the servers will auto restart

Default frontend: [http://localhost:80](http://localhost:80)

Default backend: [http://localhost:5001](http://localhost:5001)

Default port for MongoDB: `27017`

Stop with `CTRL +C`

Rebuild the container if you have added files with `docker compose up --build`

Delete the containers with volumes and their images (everything in docker) with `docker compose down --volumes --rmi all`


## License

This project is licensed under the [MIT License](LICENSE).
