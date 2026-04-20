1. Overall Purpose of the Code

This program is designed to automate WhatsApp messaging. It performs three major tasks:

Reads contact details from a file
Uses predefined message templates
Sends or schedules personalized messages

In simple terms, it behaves like a bulk messaging + scheduling system for WhatsApp.

🔹 2. Core Concept Behind the System

The system works on data-driven automation:

Data (contacts, templates, schedules) is stored in CSV files
The program reads this data
Processes it
Executes actions (sending messages)

So instead of manually messaging people, the system does it automatically.

🔹 3. Role of External Libraries
✔️ Messaging Automation

A third-party library is used to interact with WhatsApp Web.
It simulates human actions like:

Opening WhatsApp Web
Typing messages
Sending messages
✔️ Data Handling

A data-processing library is used to:

Read CSV files
Store them in table format (rows & columns)
Iterate over data easily
✔️ Time Management

Time-related modules help:

Get current system time
Compare times
Delay execution when needed
🔹 4. Input Files (Data Sources)

The system depends on three structured datasets:

📂 Contacts File
Contains phone numbers and names
Used for identifying recipients
Duplicate entries are removed to avoid repeated messaging
📂 Templates File
Contains message formats
Uses placeholders like {name}
Enables personalization

👉 Example concept:
Instead of writing 100 messages manually, one template is reused and customized for each person.

📂 Scheduled Messages File
Contains messages with specific timestamps
Enables sending messages at a future time
🔹 5. Data Processing Flow
Step 1: Load Data

All CSV files are read and converted into structured data tables.

Step 2: Clean Data

Contacts are cleaned by removing duplicate phone numbers.

Step 3: Iterate Through Data

The system loops through:

Each contact
Each template

This creates combinations of:
👉 (Contact × Template)

🔹 6. Personalization Mechanism

The system uses string replacement logic:

A placeholder like {name} is replaced with the actual contact name

👉 Concept:
This allows one template to generate multiple unique messages.

🔹 7. Message Sending Logic

The system cannot send messages instantly due to WhatsApp constraints.
So it follows this process:

Takes current system time
Adds a small delay (e.g., 1 minute)
Schedules message at that time
Opens WhatsApp Web and sends message

👉 This ensures proper execution without timing issues.

🔹 8. Scheduling System

The scheduling feature is based on time comparison:

The system reads a future timestamp
Compares it with current time
Calculates the difference
Waits until that time
Sends the message

👉 This is a time-triggered execution model

🔹 9. Sequential Execution (Important Concept)

The entire system runs sequentially (one after another):

One message is processed at a time
The program waits before moving to the next task

👉 This means:

Simple logic
But slower performance for large datasets
🔹 10. Automation Workflow Summary

The complete flow looks like this:

Load contacts
Load templates
Send personalized messages to all contacts
Load scheduled messages
Wait until specified times
Send scheduled messages
🔹 11. Key Design Concepts Used
✔️ Automation

Reducing manual work by using code

✔️ Data Abstraction

Using CSV files instead of hardcoding data

✔️ Modularity

Breaking code into functions:

Loading data
Sending messages
Scheduling
✔️ Reusability

Templates allow reuse of message formats

✔️ Personalization

Dynamic replacement of placeholders

✔️ Time-based Execution

Using system clock to trigger actions  
## 📥 Download Project

Click below to download the project:

👉 https://github.com/onkar123/Bulk-Message-Sender/archive/refs/heads/main.zip

Then click on **Code → Download ZIP**
