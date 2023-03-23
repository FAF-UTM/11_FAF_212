<h1 align="center">DOMAIN SPECIFIC LANGUAGE FOR ANALISING MEDICAL RESULTS</h1>

<h2 align="center">Cristisn BRINZA, Felicia LUPASCU, Maria ZAICA, Nichifor POPESCU</h2>

<h2 align="center"><i> GROUP: 11_FAF-212 PBL</i></h2>

---

## Introduction 

&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp; Medical reports often contain large amounts of data that can be overwhelming and difficult to analyze. To address this issue, a Domain Specific Language (DSL) can be developed specifically for analyzing medical results. In this article/presentation, we present a grammar for a DSL that can be used to analyze test results, imaging results, and lab results. The DSL allows for easy identification and extraction of important information from medical reports, making it easier for healthcare professionals to interpret and act upon the results. We demonstrate the use of the DSL through an example medical report, showing how the grammar can be used to extract important information such as the type of test performed, the result value, and the units of measurement. Overall, the development of a DSL for analyzing medical results has the potential to improve the efficiency and accuracy of medical data analysis, ultimately leading to better patient outcomes.



&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;This grammar is like a set of rules that tells a computer how to understand and analyze medical results. It has different parts that describe different types of results, such as tests, imaging, and lab results.

&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;Each type of result has specific information, like the name of the test, the results themselves, and any units or reference ranges that might be important. The grammar also includes a way for users to ask the computer to show specific sets of results, like all the test results for a particular patient or the average imaging results for a certain time frame.

&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;To make things easier for the user, the grammar includes some special words that represent patient data, like the patient's ID or their date of birth. This way, the user can ask the computer to show results for a particular patient without having to type out all of their information every time.

&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;Overall, this grammar helps the computer understand medical results and can provide customized reports based on patient data.


---

## For a markup language, we can define its grammar as follows:

L(G) = (S, P, VN, VT), where:

- S is the start symbol
- P is a finite set of production rules
- VN is a finite set of non-terminal symbols
- VT is a finite set of terminal symbols


```
VN = {medical_results, test_result, imaging_result, lab_result, query, query_type, result_type, patient_data, patient_id, birthday, date, test_name, imaging_type, lab_name, result, unit, reference_range, normal_range, high_range, low_range, image_location, location}
```
<br>

```
VT = {"test", "imaging", "lab", "show", "for", "all", "average", "tests", "imaging", "labs", "patient", "age", "-", ">", "<", "units", "normal range", "high range", "low range"}
```


 &ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp; In a markup language, the terminal symbols represent the actual content of the document or data being marked up. The non-terminal symbols represent the structure or syntax of the markup language itself.

 &ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp; The production rules describe how non-terminal symbols can be replaced or expanded into other non-terminal or terminal symbols. These rules define the syntax and structure of the markup language.

&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;To specify the grammar representation for the markup language we need to use meta notations:

| Symbol | Definition                        |
| ------ | --------------------------------- |
| < >    | Non Terminal symbol               |
|  *     | Zero or more occurrences          |
|  +     | One or more occurrences           |
|  |     | Separates the alternative symbols |
| ->     | Derivation                        |
|  ~     | Except: any character except      |
|  \\    | Comment				   |

The grammar representation for markup language project:

```
<medical_results> -> <test_result> | <imaging_result> | <lab_result> | <query>
<test_result> -> "test" <test_name> ":" <result> ["units" <unit>] [<reference_range>]
<imaging_result> -> "imaging" <imaging_type> ":" <result> ["units" <unit>] [<image_location>]
<lab_result> -> "lab" <lab_name> ":" <result> ["units" <unit>] [<reference_range>]
<query> -> "show" <query_type> "for" <patient_data>
<query_type> -> "all" <result_type> | "average" <result_type> "for" <time_frame>
<result_type> -> "tests" | "imaging" | "labs"
<patient_data> -> "patient" <patient_id> | "age" <birthday>
<patient_id> -> <word>+
<birthday> -> <date>
<date> -> <year> "-" <month> "-" <day>
<year> -> <number>
<month> -> <number>
<day> -> <number>
<test_name> -> <word>+
<imaging_type> -> <word>+
<lab_name> -> <word>+
<result> -> <number>
<unit> -> <word>+
<reference_range> -> "normal range" <normal_range> | "high range" <high_range> | "low range" <low_range>
<normal_range> -> <number> "-" <number> <unit>
<high_range> -> ">" <number> <unit>
<low_range> -> "<" <number> <unit>
<image_location> -> "location" <location>
<location> -> <word>
```


---

  To use the queries, the user must provide the appropriate patient data, either by patient ID or date of birth. The grammar also includes derived expressions such as <patient_id> and <birthday> to simplify the query process.

Overall, this grammar is designed to provide a comprehensive language for analyzing medical results and generating customized reports based on patient data.

---

An example of code using this grammar representation is:


Description { 
	test glucose= 120 
	units= mg/dL 
	stage= normal 
	range= 70-100
}
Setting {
	patient= John Smith, 
	age= 1978-01-01
	gender= male,
	weight= 175 lbs,
	height= 5'11"
}
Response {
    	show all tests for patient age 1978-01-01
   	 // Output: glucose: 120 mg/dL (normal)
}
Response {
    	show average labs for last 6 months for patient John Smith
   	 // Output: No lab results found for patient John Smith in the last 6 months.
}
Response {
    	show all imaging for patient John Smith
   	 // Output: No imaging results found for patient John Smith.
}
Response {
    	length 300 
    	prompt "The patient's glucose test results were higher than normal and indicate the presence of diabetes. The patient is advised to follow up with a healthcare provider for further evaluation and treatment."
}

---

&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;This grammar is like a set of rules for a computer program to understand medical results. It's designed to help doctors and researchers analyze medical data more easily.

Here's what some of the parts of the grammar mean:

<test_result> means a result from a medical test. This could be a blood test, a urine test, or any other kind of test that a doctor might order.
<imaging_result> means a result from a medical imaging test, like an X-ray or a CT scan.
<lab_result> means a result from a medical lab test. This could be a test to check for a certain disease or to monitor a patient's health.
<result> means the actual number that was measured in the test or imaging result.
<unit> means the unit of measurement for the result, like milligrams per deciliter (mg/dL).
<reference_range> means the range of results that are considered normal for a particular test or imaging result.
<query> means a question or request for specific information about medical results. This could be something like "show me all the blood test results for patient X" or "what is the average imaging result for the last six months?"
<patient_data> means information about a patient, like their age or ID number.
<birthday> means the patient's date of birth, which can be used instead of age to make the analysis more precise.




In this code, we first define the glucose test result for the patient, specifying the value, units, stage, and reference range. We then define the patient's data, including their name, birthday (derived from age), gender, weight, and height.

We then use the Response section to generate different queries and responses. In the first response, we show all the test results for the patient with the specified birthday, which returns the glucose test result. In the second response, we show the average of all lab results for the patient John Smith in the last 6 months, but since no lab results were provided in the example, the output is "No lab results found." In the third response, we show all the imaging results for the patient John Smith, but since no imaging results were provided in the example, the output is "No imaging results found."

Finally, we provide a response that includes a message about the patient's glucose test result, using the length and prompt keywords to specify the length of the message and the message itself.

---








Parsing algorithm: 

A common approach for parsing context-free grammars like this one is to use a technique called recursive descent parsing. Here is how it could be done for this grammar:

1. Start with the <medical_results> rule.
2. Check if the next token matches <test_result>, <imaging_result>, <lab_result>, or <query>.
3. If it matches one of those rules, call the corresponding parsing function.
4. If it doesn't match any of those rules, return an error.
5. The parsing function for <test_result> would look for the "test" keyword, then call the <test_name>, <result>, and <unit> parsing functions in order. It would also check if there is a <reference_range> and parse it if it's there.
6. The parsing function for <imaging_result> would look for the "imaging" keyword, then call the <imaging_type>, <result>, and <unit> parsing functions in order. It would also check if there is an <image_location> and parse it if it's there.
7. The parsing function for <lab_result> would look for the "lab" keyword, then call the <lab_name>, <result>, and <unit> parsing functions in order. It would also check if there is a <reference_range> and parse it if it's there.
8. The parsing function for <query> would look for the "show" keyword, then call the <query_type> and <patient_data> parsing functions in order.
9. The parsing function for <query_type> would look for either "all tests", "imaging", "labs", "average tests", or "average imaging", and parse the associated data if necessary.
10. The parsing function for <patient_data> would look for either "patient" and a patient ID, or "age" and a date of birth.
11. The parsing function for <patient_id> would parse any string of alphanumeric characters.
12. The parsing function for <birthday> would look for a date in the format "YYYY-MM-DD".
13. The parsing function for <test_name>, <imaging_type>, <lab_name>, <number>, <unit>, <normal_range>, <high_range>, and <low_range> would all parse their respective data according to the grammar rules.

&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;Recursive descent parsing works by recursively calling parsing functions for each rule in the grammar until the entire input is parsed. If the input is valid according to the grammar, a parse tree is constructed that represents the structure of the input. If the input is not valid, an error is returned.

---

## Parser

&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;Parsing is the process of taking some text and figuring out what it means according to a set of rules. In this case, we have a grammar that describes the structure of medical test results, and we want to be able to read in some text and figure out what kinds of results are being reported, what the values are, and what the reference ranges are.

&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;The algorithm I described is called "recursive descent parsing." This means that we start at the top level of the grammar (the <medical_results> rule) and recursively call parsing functions for each sub-rule until we have fully parsed the input.

&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;To do this, we start by checking the first word or symbol in the input to see if it matches any of the rules we have defined. If it does, we call the corresponding parsing function. For example, if the input starts with "test," we know we need to call the parsing function for <test_result>. That parsing function will then look for the "test" keyword, followed by the name of the test, the result value, and any reference range information.

&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;If the input doesn't match any of our defined rules, we know there is a problem with the input and we report an error.

&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;We can use this approach to parse any text that conforms to our grammar. This could be a single test result, a series of results, or even a full report that includes results from multiple patients.


<hr>
