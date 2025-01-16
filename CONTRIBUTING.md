## CONTRIBUTING

Thank you for considering contributing to this project! Contributions are welcome and appreciated. Below are the guidelines for contributing effectively.

---

### Table of Contents
1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
3. [Reporting Issues](#reporting-issues)
4. [Submitting Changes](#subbmitting-changes)
5. [Pull Request Checklist](#pull-request-checklist)
6. [Development Setup](#development-setup)
7. [Licensing](#licensing)

---

### 1. Code of Conduct

By participatin in this project, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md). It establishes our standards for creatin a welcoming and inclusive community.

---

### 2. How to Contribute

There are several ways you can contribute:
- Reporting bugs or requesting features.
- Writing and improving documentation.
- Submitting fixes or new features as pull requests.
- Reviewing and providing feedback on existing pull requests.

---

### 3. Reporting Issues

If you find a bug or have a feature request:
1. Search [open issues](../../issues) to ensure it hasn't already been reported.
2. If no existing issue matches, [open a new issue](../../issues/new/choose) using the appropriate issue template.
   - Use the **Bug Report** template for bugs.
   - Use the **Feature Request** template for enhancements or ideas.
3. Include as much detail as possible (steps to reproduce, screenshots, environment details, etc.).
4. Be respectful and patient while the issue is reviewd and discussed.

---

### 4. Submitting Changes

1. **Fork the repository** and create a new branch:
   ```
   git checkout -b feature/your-feature-name
   ```
2. Make your changes, ensureing your code adheres to the project's style and standards.
3. Write or update tests to cover your changes.
4. Commit your chanes with a meaningful message:
   ```
   git commit -m "Add feature X to address Y"
   ```
5. Push your branch to your fork:
   ```
   git push origin feature/your-feature-name
   ```
6. Open a pull request following the Pull request template.

---

### 5. Pull request Checklist

Before submitting a pull request, ensure:
- Your code is functional and adheres to the project standards.
- Tests have been added or updated, and they pass (use pytest or the test framework defined in the project)
- Documentation, if applicable, has been updated.
- You've linked relevant issues or discussions (e.g. Closes #123).
- You've filled out the Pull Request template.

---

### 6. Development Setup

To set up the project locally:
1. Clone the repository
   ```
   git clone https://github.com/BenjaminHupf/repository.git
   cd repository
   ```
2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the project or tests:
   ```
   # Example for running the main script
   python main.py

   # Example for running tests
   pytest
   ```

---

### 7. Licensing

Contributions to this project are licensed under the terms of the [GNU AGPL v3.0](LICENSE.md). 

---

Thank you for contributing! If you have any questions or need clarification, feel free to reach out.
