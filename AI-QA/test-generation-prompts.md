# AI-Assisted Test Generation Prompts

## Purpose

This document provides reusable prompt templates for AI-assisted quality engineering.
All AI-generated test artifacts should be reviewed by a QA engineer before being accepted into the test suite.
---

## AI Test Generation Workflow

The recommended workflow is:

**Requirement → Risk Analysis → AI-Assisted Test Generation → Human Review → Automation Candidate Selection → Implementation → CI Execution → Failure Analysis**

AI-generated tests should be reviewed for:

* Business relevance
* Requirement coverage
* Correct expected results
* Meaningful assertions
* Negative and boundary coverage
* Duplicate scenarios
* Test independence
* Automation suitability
* Maintainability
* Potential false confidence

---

# 1. Functional Test Generation

## Prompt

You are a Senior Quality Engineer testing a consumer mobile application.

Analyze the requirement below and generate functional test scenarios.

### Requirement

[INSERT REQUIREMENT]

### Generate tests covering

* Happy path
* Negative scenarios
* Boundary conditions
* Input validation
* User experience risks
* Mobile-specific risks
* Integration dependencies

For each scenario provide:

1. Test scenario
2. Preconditions
3. Test steps
4. Expected result
5. Priority: P0 / P1 / P2
6. Risk addressed
7. Recommended test layer: Unit / API / Integration / Mobile UI / E2E
8. Automation recommendation: Automate / Manual / Both

Do not invent application behavior that is not stated in the requirement.

Clearly identify assumptions and unanswered questions.

---

# 2. Risk-Based Test Generation

## Prompt

Act as a QA Manager performing risk-based test analysis for the following feature.

### Feature

[INSERT FEATURE DESCRIPTION]

Identify failures that could negatively affect customers or the business.

Evaluate each risk based on:

* Customer impact
* Business impact
* Probability of failure
* Data integrity impact
* Security/privacy impact
* Recoverability
* Regression potential

Classify each scenario:

**Critical / High / Medium / Low**

Prioritize testing for scenarios where failure could:

* Block a critical user journey
* Cause incorrect or lost data
* Cause application crashes
* Affect authentication or authorization
* Affect payments or subscriptions
* Create inconsistent behavior across devices
* Generate significant customer support volume

Recommend which risks should become release-blocking tests.

Explain the reasoning behind Critical and High classifications.

---

# 3. Mobile Test Scenario Generation

## Prompt

You are a Mobile QA Engineer responsible for an iOS and Android consumer application.

Analyze the following feature:

[INSERT FEATURE]

Generate mobile-specific test scenarios covering:

* iOS and Android behavior
* Supported OS versions
* Screen sizes
* Orientation changes
* App background/foreground transitions
* App termination and relaunch
* Network interruption
* Offline behavior
* Permission handling
* Notifications
* Session expiration
* Device resource constraints
* Upgrade from previous application version
* Fresh installation

Identify scenarios that should be included in the critical mobile regression suite.

Also recommend an efficient device/OS matrix using risk-based coverage rather than testing every possible combination.

Do not assume unsupported device or application behavior.

---

# 4. API Test Generation

## Prompt

Act as a Senior API Test Automation Engineer.

Analyze the following API specification.

### Endpoint

[INSERT ENDPOINT]

### Method

GET / POST / PUT / PATCH / DELETE

### Request

[INSERT REQUEST]

### Expected Response

[INSERT RESPONSE OR CONTRACT]

Generate tests covering:

* Successful requests
* Required fields
* Optional fields
* Invalid input
* Missing input
* Boundary values
* Invalid data types
* Authentication
* Authorization
* HTTP status codes
* Response schema
* Business rules
* Idempotency where applicable
* Duplicate requests


For each test identify:

* Scenario
* Input
* Expected HTTP status
* Expected response
* Business rule validated
* Priority
* Automation suitability

Flag ambiguities in the API contract instead of inventing expected behavior.

---



# 5. Generate Appium Automation

## Prompt

Act as a Senior Mobile Automation Engineer.

Generate an Appium test for the following mobile scenario:

[INSERT SCENARIO]

Technology:

* Python
* pytest
* Appium
* Page Object Model

Requirements:

* Separate page objects from test logic.
* Prefer stable accessibility identifiers.
* Avoid unnecessary XPath selectors.
* Use explicit waits rather than fixed sleeps.
* Keep assertions in the test layer where practical.
* Make the test readable and maintainable.
* Support configuration for different devices and environments.
* Capture useful diagnostic information when the test fails.

Before writing code, identify:

1. Required test data
2. Preconditions
3. Required locators
4. Assumptions
5. External dependencies

Do not invent locator values. Use descriptive placeholders when actual locators are unavailable.

---



Identify any coverage gaps created by the change.

---

# 8. AI Test Review — Preventing False Confidence

## Prompt

You are reviewing AI-generated test automation before it is accepted into a production regression suite.

Review the following test:

[INSERT TEST CODE]

Do NOT assume that a passing test means the feature is correctly tested.

Evaluate:

1. Does the test actually validate the intended business requirement?
2. Are the assertions meaningful?
3. Could the test pass even when the feature is broken?
4. Are important assertions missing?
5. Is the test validating implementation details instead of user-visible behavior?
6. Are test data assumptions valid?
7. Could mocks hide an integration failure?
8. Are waits or timing assumptions creating flakiness?
9. Are selectors stable?
10. Does the test duplicate existing coverage?
11. Is the test independent?
12. Does cleanup occur correctly?
13. Are errors being swallowed?
14. Are there false positives or false negatives?
15. Is this scenario better tested at another layer?

Return:

**VALID TEST**

**NEEDS REVISION**

or

**REDUNDANT TEST**

Then explain the reasoning and recommend improvements.

---

# 9. Shift-Left Requirement Review

## Prompt

Act as a QA Manager participating in refinement before development begins.

Review the following user story:

[INSERT USER STORY]

Identify:

### Requirement gaps

What information is missing or ambiguous?

### Testability concerns

What could make this feature difficult to test?

### Acceptance criteria gaps

Which expected behaviors need clarification?

### Dependencies

Which services, APIs, data, platforms, or third parties could affect the feature?

### Failure scenarios

What can go wrong?

### Observability

What logs, metrics, events, or diagnostic information would help troubleshoot failures?

### Automation

Which tests should developers implement at the unit/component level?

Which tests belong at API/integration level?

Which scenarios require mobile/UI/E2E coverage?

The objective is to identify quality risks before implementation begins.

---

# 10. Release Readiness Analysis

## Prompt

Act as the QA Manager responsible for making a release-readiness recommendation.

Analyze:

### Regression results

[INSERT RESULTS]

### Open defects

[INSERT DEFECTS]

### Automation results

[INSERT RESULTS]

### Known risks

[INSERT RISKS]

### Production
