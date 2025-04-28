# Contributing to SmartRoverProjects

Thank you for considering contributing to the SmartRoverProjects! We welcome contributions from everyone. By participating in this project, you agree to abide by the following guidelines.

## Table of Contents

1. [Coding Standards](#coding-standards)
2. [Commit Message Conventions](#commit-message-conventions)
3. [Pull Request Submission Process](#pull-request-submission-process)
4. [Code of Conduct](#code-of-conduct)

## Coding Standards

- **Language**: Python
- **Style Guide**: Follow the [PEP 8](https://pep8.org/) style guide.
- **Formatting**:
  - Use 2 spaces for indentation.
  - Limit lines to 79 characters.
  - Use `snake_case` for variable and function names.
  - Use `CamelCase` for class names.
  - Place imports at the top of the file, grouped into standard library, third-party, and local imports.
- **Best Practices**:
  - Write clear, concise comments and docstrings.
  - Use type hints where appropriate.
  - Avoid using global variables.
  - Write unit tests for new features and bug fixes.

## Commit Message Conventions

- **Structure**:
  - Use the present tense ("Add feature" not "Added feature").
  - Capitalize the subject line.
  - Do not end the subject line with a period.
  - Separate the subject from the body with a blank line.
  - Use the body to explain what and why vs. how.
- **Prefixes**:
  - `feat`: A new feature
  - `fix`: A bug fix
  - `docs`: Documentation only changes
  - `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
  - `refactor`: A code change that neither fixes a bug nor adds a feature
  - `perf`: A code change that improves performance
  - `test`: Adding missing or correcting existing tests
  - `chore`: Changes to the build process or auxiliary tools and libraries such as documentation generation
- **Examples**:
  - `feat: add new user registration feature`
  - `fix: resolve issue with login timeout`
  - `docs: update contributing guidelines`

## Pull Request Submission Process

1. **Fork the Repository**:
   - Navigate to the repository and click the "Fork" button to create a copy of the repository in your GitHub account.
2. **Clone your Fork**:
   - Clone your fork to your local machine using `git clone https://github.com/your-username/SmartRoverProjects.git`.
3. **Create a New Branch**:
   - Create a new branch for your feature or bug fix using `git checkout -b feature-branch-name`.
4. **Make Changes**:
   - Implement your changes, following the coding standards.
   - Ensure all tests pass and write new tests if necessary.
5. **Commit Changes**:
   - Stage your changes using `git add .`.
   - Commit your changes using `git commit -m "feat: description of the feature"`.
6. **Push Changes**:
   - Push your changes to your fork using `git push origin feature-branch-name`.
7. **Create Pull Request**:
   - Navigate to the original repository and click the "New pull request" button.
   - Select your fork and branch, then click "Create pull request".
   - Provide a clear and descriptive title for your pull request.
   - Include a detailed description of the changes and any related issues.
8. **Review Process**:
   - Your pull request will be reviewed by maintainers.
   - Make any requested changes and update the pull request.
9. **Merge**:
   - Once approved, your pull request will be merged into the main branch.

## Code of Conduct

This project has adopted the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/). By participating, you are expected to uphold this code. Please report unacceptable behavior to [smartfactorybelievers@deloitte.com].
