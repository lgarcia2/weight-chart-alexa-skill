# Database
The database is structured with the following columns
- Primary Key - PK
    - Example: `USER#{userId}`
    The primary Key is a partition key broken down into four components. 
        - The first component is the user object identifier string, the literal string "USER". This is to identify the DynamoDB row as a belonging to a User.
        - The second component is the user id, this is a key that identifies users uniquely.
        - The third component is the record object identifier string, this is the literal string "RECORD". This is to identify the DynamoDB as a User's record
        - The fourth and final componentis the record's year. This is the year for which the record corresponds to.
- version 
    - Example: `1.0`
    This is a column corresponding to the version information associated with the row. This is helpful if any changes occurr along the way. The version string can keep track of the version of the code the data was associated with, that way the data can remain consistent and stable and won't be lost after version changes
- data
    The 'data' column is where general data about the row is stored. In this case, the data is an object containing a year and an array of JSON objects containing data about a weight records for that year.
    NOTE: The max length of a record in dynamo is 400KB. If this data was stored every day for 12 months, a cursory test puts that at ~33KB. If we store this data in chunks of 'years' we're well within our bounds
    - Example: `{ "year": 2021, "data": [{ "recordTime": "2021-07-27T10:15:23", "weight": 175.5, "units": "pounds" }, { "recordTime": "2021-07-28T10:21:05", "weight": 173.2, "units": "pounds" }]}`

Note on datetimes: Datetimes are formatted according to the ISO 8601 standard without milliseconds (i.e. YYYY-MM-DDTHH:MM:SS).