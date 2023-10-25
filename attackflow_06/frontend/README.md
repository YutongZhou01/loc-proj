# AttackFlow 6 frontend

## Tech Stack

- [Vite](https://vitejs.dev/): A build tool that focuses on fast development and great developer experience.
- [Vue.js](https://vuejs.org/): A progressive JavaScript framework for building user interfaces.

## Project Structure

The project directory structure is as follows:
```
frontend/
|-- node_modules/
|-- public/
|-- src/
| |-- assets/
| |-- components/
| |-- router/
| | |-- index.js
| |-- views/
| |-- App.vue
| |-- main.js
|-- .gitignore
|-- Dockerfile
|-- index.html
|-- package-lock.json
|-- package.json
|-- README.md
|-- vite.config.js
```

- `node_modules/`: Contains project dependencies.
- `public/`: Contains static assets that are directly served.
- `src/`: Contains the source code of the frontend application.
  - `assets/`: Place for static assets like images, fonts, etc.
  - `components/`: Contains Vue components used across the application.
  - `router/`: Contains Vue Router configuration.
  - `views/`: Contains the main views or pages of the application.
  - `App.vue`: Main component that serves as the root of the Vue app.
  - `main.js`: Entry point of the Vue app.
- `.gitignore`: Specifies files and directories that should be ignored by Git.
- `Dockerfile`: Configuration for building a Docker container.
- `index.html`: Main HTML file that hosts the Vue app.
- `package-lock.json`: Lockfile for npm dependencies.
- `package.json`: Lists project dependencies and scripts.
- `README.md`: Documentation for the frontend repository.
- `vite.config.js`: Configuration file for Vite.

## Modules Used

- [axios](https://axios-http.com/): Promise-based HTTP client for making API requests.
- [bootstrap](https://getbootstrap.com/): CSS framework for responsive design and UI components.
- [dotenv](https://www.npmjs.com/package/dotenv): Loads environment variables from a `.env` file.
- [vue](https://vuejs.org/): JavaScript framework for building user interfaces.
- [vue-router](https://router.vuejs.org/): Official router for Vue.js applications.
