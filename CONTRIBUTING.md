# Contributing to Welsh Waterbody Chlorophyll Monitoring

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## 📋 Code of Conduct

This project is committed to providing a welcoming and inclusive environment for all contributors. Please read and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

## 🚀 Getting Started

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub
2. **Clone your fork locally**
   ```bash
   git clone https://github.com/YOUR_USERNAME/wq_package.git
   cd wq_package
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 💡 Types of Contributions

### Bug Reports
- **Check existing issues** before creating a new one
- **Describe the bug** with clear, reproducible steps
- **Include environment details** (Python version, OS, package versions)
- **Add error messages** and logs if available

### Feature Requests
- **Clearly describe** the feature and its benefits
- **Provide use cases** where this feature would be helpful
- **Consider potential drawbacks** or challenges

### Code Contributions
- **Start with an issue** - Discuss your approach before writing code
- **Follow coding standards** - See style guide below
- **Add tests** where applicable
- **Update documentation** for new features
- **Write meaningful commit messages** - See commit guidelines below

### Documentation Improvements
- Fix typos or unclear explanations
- Add examples or clarifications
- Improve methodology explanations
- Add relevant references or citations

## 🎨 Coding Standards

### Python Style Guide
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) conventions
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and reasonably sized

### Jupyter Notebooks
- Clear cell structure with descriptive markdown comments
- Remove output before committing (except meaningful results)
- Include explanations of analysis steps
- Document parameter choices and assumptions

### Comments
```python
# Good: Explains the "why"
# Use NDCI for chlorophyll detection as it's optimized for algal blooms
ndci = (band_5 - band_4) / (band_5 + band_4)

# Avoid: Stating the obvious
# Calculate NDCI
ndci = (band_5 - band_4) / (band_5 + band_4)
```

## 📝 Commit Message Guidelines

Write clear, descriptive commit messages:

```
[Type]: Brief description (50 chars max)

More detailed explanation if needed. Wrap at 72 characters.
- Use bullet points for multiple changes
- Reference issue numbers: fixes #123

Type options:
- feat:     New feature
- fix:      Bug fix
- docs:     Documentation
- refactor: Code restructuring
- test:     Test additions/updates
- chore:    Build, dependencies, etc.
```

### Example
```
feat: Add multi-layer chlorophyll analysis

- Implement analysis for multiple waterbody layers
- Add confidence interval calculations
- Update visualization to show layer comparison

fixes #42
```

## 🔄 Pull Request Process

1. **Update your branch** with latest main
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Run any tests** locally
   ```bash
   pytest tests/  # if applicable
   ```

3. **Push your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request** with:
   - Clear title and description
   - Reference to related issues
   - Summary of changes
   - Any relevant context

5. **Respond to review** feedback promptly

6. **Keep PR focused** - One feature/fix per PR when possible

## 🧪 Testing

If adding new functionality:
- Write tests to verify behavior
- Ensure tests pass locally
- Test edge cases and error conditions
- Document test assumptions

## 📚 Documentation

When adding features:
- Update README.md if applicable
- Add docstrings to new functions
- Include examples of usage
- Document parameters and return values
- Update methodology.md for analytical changes

## 🐛 Reporting Issues

When reporting an issue, include:

```markdown
## Description
Brief description of the issue

## Steps to Reproduce
1. Step one
2. Step two
3. ...

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- Python version: 
- OS: 
- Key package versions: 
- Jupyter/Notebook version: 

## Error Messages
```
paste error/traceback here
```
```

## ✨ Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for major contributions
- GitHub's contributor graph

## Questions?

- Check existing issues and documentation
- Open a discussion issue if unsure
- Reach out to maintainers

---

Thank you for contributing to making water quality monitoring more accessible! 🌊
