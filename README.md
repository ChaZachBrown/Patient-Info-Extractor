# Medical Data Parser and Testing Framework for LLMs

## Overview

This tool parses unstructured doctors' notes to populate relevant fields in patient records. Additionally, it features a basic testing framework to evaluate the performance of various language model prompts. The testing framework was the main focus of this project. Because LLMs are not deterministic test driven development is more important than ever. To get the performance and reliability needed for production, testing the prompts and chains hundreds to thousands of times is needed to get an acceptable success rate of 99.99 or greater. This requires parallelizing the testing of multiple different prompts, models and configurations to find the optimal solution for each use case. 

## Features

- **Data Extraction**: Extracts pertinent patient data from unstructured doctors' notes, structuring them for database insertion.
  
- **Testing Framework**: Designed to rigorously test different language model prompts and output performance metrics for business intelligence tools.

## Architecture

### Data Parsing

- **Data Extraction**: Transforms unstructured doctors' notes into structured data objects suitable for database storage.
  
- **JSON Integration**: Utilizes a one-shot prompt to combine existing and new patient data into a structured JSON object.

### Testing Framework

- **Log Generation**: Exports detailed logs containing metrics on the number of tests passed, failed (and reasons), and total runs, for BI tool import.

- **Extended Features**: Planned improvements include more structured logs for BI import, automated data flows, and multiple model testing.

## Note on Installation and Usage

This project is primarily intended for educational purposes and skill demonstration. It is set up to be demoed live during interviews rather than for independent installation and use. The primary focus is to serve as a proof-of-concept to showcase my capabilities and understanding of Large Language Models (LLMs).

---

### Steps to Production-Readiness

While this project serves primarily as an educational endeavor, the following improvements would be necessary for a transition to a production-ready application:

1. **Code Refactoring**: Optimize the existing code for efficiency, readability, and maintainability. Consider implementing design patterns where appropriate.
  
2. **Scalability**: Evaluate and improve the system architecture to ensure it can handle increased load and user concurrency.
  
3. **Security**: Conduct a thorough security audit to identify vulnerabilities. Implement security best practices, including data encryption and secure API design.
  
4. **Testing**: Expand the test suite to cover edge cases, integration tests, and performance tests. Utilize CI/CD pipelines for automated testing.
  
5. **Error Handling and Logging**: Implement robust error handling and logging mechanisms to ensure system reliability and ease of debugging.
  
6. **Documentation**: Complete the API and code documentation to industry standards, making it easier for other developers to understand, use, and contribute to the project.
  
7. **User Experience**: Conduct usability testing and refine the UI/UX based on user feedback.
  
8. **Performance Tuning**: Use profiling tools to identify bottlenecks and optimize the code and database queries accordingly.
  
9. **Legal Compliance**: Ensure that the application complies with relevant laws and regulations, such as GDPR for data protection.


### Performance Enhancement

- **Multi-layered Prompt Strategies**: Includes basic to advanced prompt configurations for better performance and reliability, from multi-shot and chain-of-thought to self-consistency techniques.

- **High-Throughput Testing**: Capable of parallelizing tests on multiple prompts to achieve a high success rate, making it production-ready.
    
- **Model Fine-Tuning**: Create synthetic data for model fine-tuning, along with before-and-after performance comparison.
